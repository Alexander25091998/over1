# Generated by Django 4.2.2 on 2023-06-28 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='photo',
        ),
    ]
