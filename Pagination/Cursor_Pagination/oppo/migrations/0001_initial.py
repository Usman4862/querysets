# Generated by Django 4.1.7 on 2023-04-08 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OppoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50, verbose_name='Mobile Model')),
                ('battery', models.CharField(max_length=50)),
                ('screen_size', models.CharField(help_text='Please Enter size in inches.', max_length=50, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
    ]
