from django.db import models
from hortum.productor.models import Productor
from hortum.picture.models import Picture
from hortum.announcement.models import Announcement
from hortum.users.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idPicture = models.OneToOneField(Picture, on_delete=models.CASCADE, null=True)
    idAnunFav = models.ManyToManyField(Announcement)
    idProdFav = models.ForeignKey(Productor, on_delete=models.CASCADE, null=True)
