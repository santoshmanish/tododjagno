from django.db import models

# Create your models here.



class TaskManager(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task
