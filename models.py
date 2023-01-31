from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

    
class Details(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    address = models.TextField(max_length = 30)
    def __str__(self):
        return str(self.name) 
   
     



    
