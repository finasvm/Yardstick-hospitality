from django.db import models

# Create your models here.

class Contacts(models.Model):
    fullname=models.CharField(max_length=500,null=True,blank=True)
    email=models.CharField(max_length=500,null=True,blank=True)
    subject=models.CharField(max_length=500,null=True,blank=True)
    message=models.CharField(max_length=2000,null=True,blank=True)