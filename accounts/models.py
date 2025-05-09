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
    Age = models.IntegerField()
    Number = models.CharField(max_length=10, blank = True)
    Gender = models .CharField(max_length=1, choices = gender_choices, default = 'U')

    def __str__(self):
        return f'{self.Name}'
