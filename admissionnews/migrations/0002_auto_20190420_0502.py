# Generated by Django 2.2 on 2019-04-19 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionnews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionnews',
            name='end_time',
            field=models.DateTimeField(default='2015-04-20 05:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionnews',
            name='start_time',
            field=models.DateTimeField(default='2015-04-20 05:00'),
            preserve_default=False,
        ),
    ]
