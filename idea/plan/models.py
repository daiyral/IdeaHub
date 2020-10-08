from django.contrib.auth.models import AbstractUser
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
    img=models.ImageField(upload_to='profile_pic',blank=True)
    about=models.TextField(max_length=1000,blank=True)
    projects=models.ManyToManyField('Project',blank=True)
    jobs=models.ForeignKey(Title,on_delete=models.CASCADE,null=True)
    experience=models.TextField(max_length=1000,blank=True)

class Project(models.Model):
    name=models.CharField(max_length=64)
    budget=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateTimeField(auto_now=True)
    description=models.TextField(max_length=1000)
    required=models.ManyToManyField(Title)
    members=models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_messages')
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}"

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]        