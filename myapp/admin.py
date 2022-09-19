from django.contrib import admin
from . import models


# Register your models here.

class TaskManagerAdmin(admin.ModelAdmin):
    list_display = ('task','description', 'completed', 'created')
    
    
admin.site.register(models.TaskManager, TaskManagerAdmin)