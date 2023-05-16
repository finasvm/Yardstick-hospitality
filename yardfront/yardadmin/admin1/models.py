from django.db import models

# Create your models here.

class Clients(models.Model):
    Title=models.CharField(max_length=100,null=True,blank=True)
    profimage = models.ImageField(upload_to='profile_pictures',null=True,blank=True)

    def __str__(self):
        return self.Title

class ClientImages(models.Model):
    images=models.ImageField(upload_to='main_pictures',null=True,blank=True)
    clienttitle=models.ForeignKey(Clients,on_delete=models.CASCADE,related_name='title')

    def __str__(self):
        return self.clienttitle

class SiteDetails(models.Model):
    email=models.CharField(max_length=100,null=True,blank=True)
    ph_number=models.IntegerField(null=True,blank=True)
    whatsapp_link=models.CharField(max_length=500,null=True,blank=True)
    insta_link=models.CharField(max_length=500,null=True,blank=True)
    facebook_link=models.CharField(max_length=500,null=True,blank=True)
    twitter_link=models.CharField(max_length=500,null=True,blank=True)
    utube_link=models.CharField(max_length=500,null=True,blank=True)
    footer_copyright=models.CharField(max_length=500,null=True,blank=True)
 
    
class Banner(models.Model):
    Banner_images=models.ImageField(upload_to='banner_pictures',null=True,blank=True)
    Banner_title=models.CharField(max_length=100,null=True,blank=True)
