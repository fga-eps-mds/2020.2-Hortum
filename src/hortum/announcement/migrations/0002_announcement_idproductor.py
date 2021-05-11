# Generated by Django 3.1.7 on 2021-05-11 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('announcement', '0001_initial'),
        ('productor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='idProductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='productor.productor'),
        ),
    ]
