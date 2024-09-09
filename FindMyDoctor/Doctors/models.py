from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Doctors(models.Model):
    Name = models.CharField(max_length=50 , default='Unknown')
    Phone = models.CharField(max_length=11,  default=1 )
    Adress = models.CharField(max_length=100, default='Unknown')
    Specialization= models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return self.Name
