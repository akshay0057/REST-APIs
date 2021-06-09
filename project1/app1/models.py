from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=50)
    emp_sal = models.IntegerField()