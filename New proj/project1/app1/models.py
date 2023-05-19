from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField()
    phone=models.CharField(max_length=10)

class employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=25)
    place=models.CharField(max_length=25)
    company_name=models.CharField(max_length=25)
    designation=models.CharField(max_length=25)
    salary=models.IntegerField()