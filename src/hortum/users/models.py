from django.db import models

class User(models.Model):
    class Meta:
        abstract = True
        
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)