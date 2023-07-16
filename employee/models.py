from django.db import models

from department.models import Department


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    identification_document = models.FileField(upload_to='documents/')

