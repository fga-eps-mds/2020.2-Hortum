from django.db import models
from rest_framework import serializers

class Picture(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='uploaded')
