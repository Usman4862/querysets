# Generated by Django 4.1.7 on 2023-04-05 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_throttle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fakethrottle',
            name='phone',
        ),
    ]