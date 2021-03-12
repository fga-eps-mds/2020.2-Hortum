from django.db import models
from rest_framework import serializers

from hortum.productor.models import Productor
from hortum.picture.models import Picture
from hortum.announcement.models import Announcement
from hortum.users.models import User

class Customer(User):
    idPicture = models.OneToOneField(Picture, on_delete=models.CASCADE, null=True)
    idAnunFav = models.ForeignKey(Announcement, on_delete=models.CASCADE, null=True)
    idProdFav = models.ForeignKey(Productor, on_delete=models.CASCADE, null=True) 