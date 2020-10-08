from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json
from .models import User,Project
# Create your views here.

def index(request):
    return render(request,"plan/index.html")

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
    return render(request,"plan/profile.html",{
        "profile":user
    })

def info(request,username,mission):
    user=User.objects.get(username__iexact=username)
    if mission == 'overview':
        return JsonResponse([user.about],safe=False)
    elif mission == 'projects':
        return JsonResponse([user.projects],safe=False)
    elif mission == 'experience':
        return JsonResponse([user.experience],safe=False)   

def chat(request):
    return render(request,'plan/chat.html')  

@login_required
def chatroom(request,room_name):
    return render(request,'plan/chatroom.html',{
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })


def projects(request):
    projects=Project.objects.all()
    return render(request,'plan/projects.html',{
        'projects':projects
    })

def project(request,project_name):
    pass