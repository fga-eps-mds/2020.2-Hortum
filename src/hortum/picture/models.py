from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='uploaded')
