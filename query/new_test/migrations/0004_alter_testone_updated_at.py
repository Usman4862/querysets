# Generated by Django 4.1.7 on 2023-03-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_test', '0003_rename_full_name_testone_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testone',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]