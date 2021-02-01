# Generated by Django 3.1.5 on 2021-01-28 18:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0002_auto_20210128_1638'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('post', 'created_by', 'deleted_at')},
        ),
        migrations.AlterUniqueTogether(
            name='interest',
            unique_together={('post', 'created_by')},
        ),
        migrations.RemoveField(
            model_name='interest',
            name='deleted_at',
        ),
    ]