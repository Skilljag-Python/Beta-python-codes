# Generated by Django 3.1.5 on 2021-02-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210131_1450'),
        ('profiles', '0010_auto_20210203_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='askills',
            field=models.ManyToManyField(blank=True, related_name='ausers', to='core.Skill'),
        ),
    ]