from django.db import models
from hortum.productor.models import Productor
from hortum.announcement.models import Announcement
from hortum.users.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idAnunFav = models.ManyToManyField(Announcement)
    idProdFav = models.ManyToManyField(Productor)
