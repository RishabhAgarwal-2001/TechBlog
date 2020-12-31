from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254)
    fname = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    
