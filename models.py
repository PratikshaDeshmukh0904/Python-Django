from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.TextField(max_length=191)
    password = models.TextField(max_length=50)
    
class branch(models.Model):
    id = models.IntegerField(primary_key=True)
    branch_name = models.CharField(max_length=255)
    def __str__(self):
            return self.branch_name
    class Meta:
        db_table = 'branch'


class StandardMaster(models.Model):
    SrNumber = models.IntegerField(primary_key=True)
    standardname = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'StandardMaster'

class StaffRegstration(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length = 25)
    MobileNo = models.IntegerField(max_length=10)
    Subject = models.CharField(max_length=20)
