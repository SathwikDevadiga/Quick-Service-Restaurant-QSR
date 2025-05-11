
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you want to include in your custom user model
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)  
    email = models.EmailField(unique=True)
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email
