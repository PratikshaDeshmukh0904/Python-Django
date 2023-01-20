from django.db import models
from enum import unique
from operator import truediv
from re import T
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

# Create your models here.
#1.AdminLogin
class admin(models.Model):
    User = models.CharField(max_length=191)
    Pass= models.CharField(max_length=50)
    
    class Meta:
        db_table = 'admin'

#2.Add Category
class addcategory(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=255)
     
    class Meta:
        db_table='addcategory'