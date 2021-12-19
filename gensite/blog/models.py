from django.db import models

# Create your models here.
class aboutus(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=300)
    description =models.TextField(max_length=700)
    
    def __str__(self) :
        return self.title