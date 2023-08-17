from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)                  # Add the Date without manually entering
    
    def __str__(self):
        return self.name
    

