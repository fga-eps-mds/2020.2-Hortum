# Generated by Django 3.1.7 on 2021-04-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_announcement_idproductor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-publicationDate']},
        ),
        migrations.AddField(
            model_name='announcement',
            name='publicationDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
