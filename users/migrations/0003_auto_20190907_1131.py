# Generated by Django 2.2.5 on 2019-09-07 05:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20190907_1125'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='studentProfile',
            new_name='Profile',
        ),
    ]
