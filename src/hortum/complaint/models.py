from django.db import models
from hortum.productor.models import Productor

class Complaint(models.Model):
    def upload_image(instance, filename):
        return f"{instance.author}-{filename}"

    author = models.CharField(max_length=30)
    description = models.CharField(max_length=450)
    idProductor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='reclamations')
    image = models.ImageField(upload_to=upload_image, null=True)
    emailCustomer = models.EmailField(max_length=100)