from django.db import models

from ..productor.models import Productor


class Announcement(models.Model):

    TYPE_OF_PRODUCTS_CHOICES = [
        ('Artesanato', 'Artesanato'),
        ('Açúcar', 'Açúcar'),
        ('Bebidas', 'Bebidas'),
        ('Café', 'Café'),
        ('Carnes', 'Carnes'),
        ('Cogumelos', 'Cogumelos'),
        ('Derivados de trigo', 'Derivados de trigo'),
        ('Derivados de mandioca', 'Derivados de mandioca'),
        ('Derivados de cana', 'Derivados de cana'),
        ('Desidatrados', 'Desidratados'),
        ('Doces', 'Doces'),    
        ('Flores', 'Flores'),
        ('Frango Caipira', 'Frango Caipira'),
        ('Frutas', 'Frutas'),
        ('Graos', 'Graos'),
        ('Hortaliças', 'Hortaliças'),
        ('Laticinios', 'Laticinios'),
        ('Legumes', 'Legumes'),
        ('Ovos de Galinha', 'Ovos de Galinha'),
        ('Peixes', 'Peixes'),
        ('Polpa de frutas', 'Polpa de frutas'),
        ('Pratos congelados', 'Pratos congelados'),
        ('Sorvetes', 'Sorvetes'),
        ('Outros', 'Outros'),
    ]

    idProductor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='announcements')
    likes = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    type_of_product = models.CharField(max_length=200, choices=TYPE_OF_PRODUCTS_CHOICES, default='Outros')
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    inventory = models.BooleanField(default=True)
    publicationDate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publicationDate']

class Localization(models.Model):
    idAnnoun = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='localizations')
    adress = models.CharField(max_length=100)

class AnnouncementImage(models.Model):
    def upload_image_announ(instance, filename):
        return f"{instance.idImage}-{filename}"

    idImage = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='images')
    picture = models.ImageField(upload_to=upload_image_announ, null=True)