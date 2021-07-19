
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:name>",views.profile,name="profile"),
    path("projects",views.projects,name="projects"),
    path("project/<str:project_name>",views.project,name="project"),
    path("create_project",views.create_project,name="create_project"),
    path("apply/<str:project_name>",views.apply,name="apply"),
    path("manage/<str:project_name>",views.manage,name="manage"),
    path("update_task/<int:task_id>/<str:project_name>",views.update_task,name="update_task"),
    path("delete_task/<int:task_id>/<str:project_name>",views.delete_task,name="delete_task"),
    path("send_message/<str:recipient>",views.send_message,name="send_message"),
    path("invite/<str:username>",views.invite,name="invite"),
    
    #api
    path("info/<str:username>/<str:mission>",views.info,name="info"),
    path("tasks/<str:project_name>",views.tasks,name="tasks"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)