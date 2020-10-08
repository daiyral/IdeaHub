
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
    path("chat",views.chat,name="chat"),
    path("chat/<str:room_name>/",views.chatroom,name="chatroom"),

    #api
    path("info/<str:username>/<str:mission>",views.info,name="info")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)