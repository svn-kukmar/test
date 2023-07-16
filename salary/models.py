from django.db import models

from employee.models import Employee


# Create your models here.
class Salary(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
