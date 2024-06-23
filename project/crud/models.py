from django.db import models
from project.cust_auth.models import User
# Create your models here.


"""
- Create "Todo" Model that contains fields:

      - Task Name
      - Task Description
      - File Field
      - Image Field
      - Start date.
      - End date.
      - Status of task.
"""


class Todo(models.Model):
    STATUS_CHOICE = [
        ('pending', 'pending'),
        ('progress', 'progress'),
        ('completed', 'completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=254)
    task_description = models.TextField()
    file = models.FileField(upload_to='static/file/')
    image = models.ImageField(upload_to='static/image/')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICE)


    def __self__(self):
        return self.task_name