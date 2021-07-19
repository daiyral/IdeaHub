from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User,Project,Task,Tag,Message
from .forms import ProjectForm
# Create your views here.

def index(request):
    user_count=User.objects.all().count()
    project_count=Project.objects.all().count()
    task_count=Task.objects.all().count()
    return render(request,"plan/index.html",{
        "user_count":user_count,"project_count":project_count,"task_count":task_count
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "plan/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "plan/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first"]
        last_name=request.POST["last"] 
        if "picture" in request.FILES:
           picture=request.FILES["picture"]
           fs=FileSystemStorage()
           picture_name=fs.save(picture.name,picture)

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "plan/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            if "picture" in request.FILES:
               user = User.objects.create_user(username, email, password,picture=picture_name)
            else:
                user = User.objects.create_user(username, email, password)
            user.first_name=first_name
            user.last_name=last_name    
            user.save()
        except IntegrityError:
            return render(request, "plan/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "plan/register.html")        

def profile(request,name):
    user=User.objects.get(username__iexact=name)
    project_managed=Project.objects.filter(manager__username=request.user)
    return render(request,"plan/profile.html",{
        "profile":user,
        "viewer":request.user,
        "project_managed":project_managed

    })

def info(request,username,mission):
    user=User.objects.get(username__iexact=username)
    if mission == 'overview':
        return JsonResponse([user.about],safe=False)
    elif mission == 'projects':
        projects=Project.objects.filter(members__username=username)
        return JsonResponse([project.serialize() for project in projects],safe=False)
    elif mission == 'experience':
        return JsonResponse([user.experience],safe=False)   
    elif mission =='user_info':
        sender=User.objects.get(username=request.user)
        return JsonResponse([sender.serialize()],safe=False)    



def projects(request):
    projects=Project.objects.all()
    projects=projects.order_by("-date").all()
    return render(request,'plan/projects.html',{
        'projects':projects
    })

def project(request,project_name):
    project=Project.objects.get(name=project_name)
    return render(request,'plan/project.html',{
        'project':project
    })
def create_project(request):
    if request.method=="POST":
        user=User.objects.get(username=request.user)
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():#check form 
            instance=form.save(commit=False)
            instance.save()
            instance.members.add(request.user)
            instance.manager=request.user
            required=form.cleaned_data['required']
            instance.required.set(required)
            instance.save()
            return HttpResponseRedirect(reverse('projects'))
        else:#return form back in case of an error
            return render(request,"plan/create_project.html",{
                "form":form
            })
    return render(request,"plan/create_project.html",{
        "form":ProjectForm()#render our form
    })   
@csrf_exempt#not secure
def apply(request,project_name):
    project=Project.objects.get(name=project_name)
   
    if request.method=="GET":
           if project.applications.filter(username=request.user).exists():
                return JsonResponse([1],safe=False)
           return JsonResponse([0],safe=False)    

    if request.method=="POST":
        if project.members.filter(username=request.user).exists():
            return JsonResponse([-1],safe=False) 
        elif project.applications.filter(username=request.user).exists():
            project.applications.remove(request.user)
            return JsonResponse([0],safe=False)
        else:    
            project.applications.add(request.user)
            return JsonResponse([1],safe=False)
        

def manage(request,project_name):
    project=Project.objects.get(name=project_name)
    return render(request,'plan/manage_project.html',{
            'project':project
    })

@csrf_exempt#not secure
def tasks(request,project_name):
    if request.method == "GET":
        tasks=Task.objects.filter(project__name=project_name)
        return JsonResponse([task.serialize() for task in tasks],safe=False)
    elif request.method == "POST":
        data=json.loads(request.body)
        title=data.get("title","")
        body=data.get("body","")
        username=data.get("assigned","")
        assigned=User.objects.get(username=username)
        project=Project.objects.get(name=project_name)
        task=Task(
            name=title,
            body=body,
            assigned=assigned,
            project=project,
            col=Tag.objects.get(name="todo")
        )
        task.save()
        return JsonResponse(task.serialize(),safe=False)
    else:
         return JsonResponse({"Error":"Method must be POST or GET"},status=401)       

@csrf_exempt#not secure
def update_task(request,task_id,project_name):
    if request.method=="POST":
        project=Project.objects.get(name=project_name)
        if project.members.filter(username=request.user).exists():
            task=Task.objects.get(pk=task_id)
            data=json.loads(request.body)
            col=data.get("col","")
            task.col=Tag.objects.get(name=col)
            task.save()
            return JsonResponse({"Success":"Updated col"})
        else:
            return JsonResponse({"Error":"Cannot move tasks in other projects"})    

@csrf_exempt#not secure
def delete_task(request,task_id,project_name):
    if request.method=="POST":
        try:
            task=Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return HttpResponse('Task does not exist')
        project=Project.objects.get(name=project_name)
        if project.members.filter(username=request.user).exists():        
            task.delete()
            return JsonResponse({"Success":"Deleted task"})   
        else:
            return JsonResponse({"Error":"Cannot delete tasks in other projects"})

def send_message(request,recipient):
    if request.method=="POST":
        message=request.POST["message"]
        message_reciver=User.objects.get(username=recipient)
        message_sender=User.objects.get(username=request.user)
        message=Message(
            author=message_sender,
            recipient=message_reciver,
            content=message
        )
        message.save()
        return HttpResponseRedirect(reverse('profile',args=[recipient]))
@csrf_exempt
def invite(request,username):
    if request.method=="POST":
        user=User.objects.get(username=username)
        data=json.loads(request.body)
        project_invite=data.get("invite","")
        project=Project.objects.get(name=project_invite)
        if project.members.filter(username=username).exists():
            return JsonResponse([0],safe=False) 
        user.invites.add(project)
        return JsonResponse([1],safe=False)