from django.db import models

from employee.models import Employee


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)  # for example: 'pending', 'in progress', 'completed'
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
