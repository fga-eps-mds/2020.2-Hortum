# Generated by Django 3.1.7 on 2021-04-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productor', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='idProdFav',
            field=models.ManyToManyField(to='productor.Productor'),
        ),
    ]
