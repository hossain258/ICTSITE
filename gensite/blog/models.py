from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Dynamicslider(models.Model):    
    title = models.CharField( max_length=200, )
    image = models.ImageField(blank=True, null = True, upload_to ='dynamic_slider_images')
    
    
    def __str__(self) :
        return self.title
    
    
class aboutus(models.Model):
    title = models.CharField(max_length=300)
    #heading = models.CharField(max_length=300)
    # description = models.TextField(max_length=1200)
    image = models.ImageField(blank=True, null = True, upload_to ='about')
    
    description = RichTextField( blank =True, null = True)
    
    def __str__(self) :
        return self.title
    
class contactus(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=20)
    phone_Number =  models.CharField(max_length=20, null =True)
    message = models.TextField(max_length=1200)
    date_created= models.DateTimeField(auto_now_add=True)
    
    
class services(models.Model):
    title =models.CharField(max_length=100)
    # description = models.TextField(max_length=1200)
    description = RichTextField( blank =True, null = True)
    image = models.ImageField(blank=True, null = True, upload_to ='services_images')
    thumbnail_image =models.ImageField(blank=True, null = True, upload_to ='servicesDeatils')
    
    
    def __str__(self) :
        return self.title
    
    
    
class clientdata(models.Model):
    title =models.CharField(max_length=100)
    
    image = models.ImageField(blank=True, null = True, upload_to ='client_images')
    
    
    def __str__(self) :
        return self.title
    
    
class Portfolio(models.Model):
    title =models.CharField(max_length=100)
    
    image = models.ImageField(blank=True, null = True, upload_to ='portfolio')
    
    
    def __str__(self) :
        return self.title
    


    
   



    
    
 