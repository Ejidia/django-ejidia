from django.db import models

# Create your models here.
class TodoList(models.Model):
    task_name = models.TextField()
    description =models.TextField()
    due_date =  models.DateField()
    priority = models.CharField(max_length=8)
    is_complete = models.BooleanField()