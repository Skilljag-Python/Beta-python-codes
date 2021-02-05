# Generated by Django 3.1.6 on 2021-02-05 11:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='allowed',
            field=models.ManyToManyField(related_name='allowed_rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
