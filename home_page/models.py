from django.db import models

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    pwd = models.CharField(max_length=6)
    
    