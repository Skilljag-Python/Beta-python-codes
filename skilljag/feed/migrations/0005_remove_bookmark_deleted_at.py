# Generated by Django 3.1.5 on 2021-01-28 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20210128_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='deleted_at',
        ),
    ]
