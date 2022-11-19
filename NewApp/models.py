from django.db import models

# Create your models here.
class addcategory(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=255)
     
    class Meta:
        db_table='addcategory'