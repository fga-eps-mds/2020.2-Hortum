# Generated by Django 3.1.7 on 2021-03-24 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('productor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='idProdFav',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productor.productor'),
        ),
    ]
