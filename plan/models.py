from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator
from django.db import models

class Title(models.Model):
    name=models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"
        
class Tag(models.Model):
    name=models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"
       

class User(AbstractUser):
    img=models.ImageField(upload_to='profile_pic',blank=True,default='blank-profile-picture.png')
    about=models.TextField(max_length=1000,blank=True)
    jobs=models.ForeignKey(Title,on_delete=models.CASCADE,null=True)
    experience=models.TextField(max_length=1000,blank=True)
    invites=models.ManyToManyField('Project',blank=True)

    def serialize(self):
        return{
            "username":self.username,
            "img":self.img.url
        }

class Project(models.Model):
    name=models.CharField(max_length=64)
    budget=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateTimeField(auto_now=True)
    description=models.TextField(max_length=1000)
    headline=models.TextField(max_length=64,null=True)
    est_length=models.DecimalField(max_digits=3,decimal_places=0,null=True)
    required=models.ManyToManyField(Title)
    manager=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='manager')
    members=models.ManyToManyField(User, related_name='members')
    img=models.ImageField(upload_to='project_imgs',blank=True,default='plan/no_image.png')
    applications=models.ManyToManyField(User,related_name='applications',blank=True)

    def __str__(self):
        return f"{self.name}"

    def serialize(self):
        return{
            "name":self.name,
            "headline":self.headline,
            "img":self.img.url
        }    

class Message(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_messages')
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    recipient=models.ForeignKey(User,on_delete=models.CASCADE,related_name="reciver",null=True)

    def __str__(self):
        return f"{self.author.username}"
      


class Task(models.Model):
    name=models.CharField(max_length=32)
    body=models.CharField(max_length=128)
    assigned=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    col=models.ForeignKey(Tag,on_delete=models.CASCADE,null=True)


    def serialize(self):
        return{
            "id":self.id,
            "title":self.name,
            "body":self.body,
            "assigned_first_name":self.assigned.first_name,
            "assigned_last_name":self.assigned.last_name,
            "assigned_img":self.assigned.img.url,
            "col":self.col.name,
            "timestamp":self.timestamp.strftime("%b %d %Y")
        }

    def __str__(self):
        return f"{self.name}"     