from django.contrib import admin
from .models import User,Project,Title,Tag,Message
# Register your models here.

admin.site.register(User),
admin.site.register(Title),
admin.site.register(Project),
admin.site.register(Message)