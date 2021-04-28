# Generated by Django 3.1.7 on 2021-04-28 21:36

from django.db import migrations, models
import hortum.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='src/hortum/img/person-male.png', null=True, upload_to=hortum.users.models.upload_image),
        ),
    ]
