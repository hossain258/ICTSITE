from django.db import models

# Create your models here.
class aboutus(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=300)
    description =models.TextField(max_length=700)
    
    def __str__(self) :
        return self.title
    
class contactus(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=20)
    phone_Number =  models.CharField(max_length=20, null =True)
    message = models.TextField()
    date_created= models.DateTimeField(auto_now_add=True)
    
    
class services(models.Model):
    title =models.CharField(max_length=100)
    description =models.TextField(max_length=700)
    
    def __str__(self) :
        return self.title

    
    
 