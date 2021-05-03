from django.db import models

from ..productor.models import Productor


class Announcement(models.Model):
    AVICULTURA = [
        ('Frango Caipira', 'Frango Caipira'),
        ('Galinhas', 'Galinhas'),
        ('Ovos de Galinha', 'Ovos de Galinha'),
        ('Ovos férteis', 'Ovos férteis'),
    ]

    CARNE = [
        ('Carne bovina', 'Carne bovina'),
        ('Carne suína', 'Carne suína'),
        ('Carne Caprina/Ovina', 'Carne Caprina/Ovina'),
        ('Carne de Frango', 'Carne de Frango'),
        ('Carne de Outras Aves', 'Carne de Outras Aves'),
        ('Peixes', 'Peixes'),
    ]

    CONGELADOS = [
        ('Polpa de frutas', 'Polpa de frutas'),
        ('Pratos congelados', 'Pratos congelados'),
        ('Sorvetes', 'Sorvetes'),
    ]

    DERIVADOS_DE_CANA = [
        ('Açúcar', 'Açúcar'),
        ('Melado', 'Melado'),
        ('Rapadura', 'Rapadura'),
    ]

    DERIVADOS_DE_MANDIOCA = [
        ('Farinha de Mandioca', 'Farinha de Mandioca'),
        ('Farinha de Tapioca', 'Farinha de Tapioca'),
        ('Massa de Tapioca', 'Massa de Tapioca'),
        ('Massa para Bolos', 'Massa para Bolos'),
    ]

    LATICINIOS = [
        ('Iogurte', 'Iogurte'),
        ('Queijo', 'Queijo'),
        ('Leite', 'Leite'),
    ]

    OTHERS = [
        ('Artesanato', 'Artesanato'),
        ('Bebidas', 'Bebidas'),
        ('Café', 'Café'),
        ('Cogumelos', 'Cogumelos'),
        ('Derivados de trigo', 'Derivados de trigo'),
        ('Desidatrados', 'Desidratados'),
        ('Doces', 'Doces'),    
        ('Flores', 'Flores'),
        ('Frutas', 'Frutas'),
        ('Graos', 'Graos'),
        ('Hortaliças', 'Hortaliças'),
        ('Legumes', 'Legumes'),
        ('Outros', 'Outros'),
    ]

    TYPE_OF_PRODUCTS_CHOICES = AVICULTURA + CARNE + CONGELADOS + DERIVADOS_DE_CANA + DERIVADOS_DE_MANDIOCA + LATICINIOS + OTHERS

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