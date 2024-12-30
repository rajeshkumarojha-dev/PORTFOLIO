from django.db import models

# Create your models here.
class Portfolio(models.Model):
    first_name=models.CharField(max_length=20,blank=True)
    last_name=models.CharField(max_length=20,blank=True)
    email=models.CharField(max_length=60,blank=True)
    description=models.CharField(max_length=100,blank=True)