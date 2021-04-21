from django.db import models
from hortum.picture.models import Picture
from hortum.productor.models import Productor

class Reclamation(models.Model):
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=450)
    idProductor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='reclamations')
    idPicture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)
    emailCustomer = models.EmailField(max_length=100)