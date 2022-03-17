from django.db import models

# Create your models here.

class Router_Details(models.Model):
    Sapid = models.CharField(unique=True,max_length=500)
    Hostname = models.CharField(unique=True,max_length=500)
    Loopback = models.CharField(unique=True,max_length=500)
    Mac_address = models.CharField(unique=True,max_length=500)
    is_delete = models.BooleanField(default=False)