from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255 )
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255 )
    dateofbirth = models.CharField(max_length=255 )

    def __str__(self):
        return self.name + " " + self.mobile
    

 

