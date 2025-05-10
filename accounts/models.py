from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

"""User successfully imported as django user"""

"""making gender choices"""
gender_choices = [
    ("M", 'Male'),
    ("F", 'Female'),
    ('U', 'Unknown'),
]
class User(AbstractUser):
    Name = models.CharField(max_length=30, blank = True)
    Age = models.IntegerField(default = 10)
    Number = models.CharField(max_length=10, blank = True)
    Gender = models .CharField(max_length=1, choices = gender_choices, default = 'U')

    def __str__(self):
        return f'{self.Name}'

class Resturant(models.Model):
    Name = models.CharField(max_length=50, blank = True)
    location = models.CharField(max_length=30)
    district = models.CharField(max_length=20)
    latitude = models.FloatField(default= False)
    longitude = models.FloatField(default= False)
    phone = models.CharField(max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        return self.Name

