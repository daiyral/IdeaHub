from django.contrib import admin
from .models import User,Project,Title,Tag,Message,Task
# Register your models here.

admin.site.register(User),
admin.site.register(Title),
admin.site.register(Project),
admin.site.register(Message),
admin.site.register(Task),
admin.site.register(Tag)