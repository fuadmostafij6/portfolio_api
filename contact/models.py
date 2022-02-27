import email
from email import message
from django.db import models

# Create your models here.
class Contact( models.Model):
    name = models.CharField(max_length=100,blank=True, null = True )
    email = models.EmailField()
    phone = models.CharField(max_length=100,blank=True, null = True )
    message = models.CharField(max_length=10000,blank=True, null = True)

    def __str__(self):
        return self.name