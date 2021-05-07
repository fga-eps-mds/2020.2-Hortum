from django.db import models
from django.contrib.auth.models import AbstractUser

def upload_image(instance, filename):
    return f"Profile-{instance.username}-{filename}"

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=120)
    phone_number = models.CharField(unique=True, blank=False, null=True, max_length=13)
    is_productor = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to=upload_image, null=True, default="person-male.png")

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
