# Generated by Django 4.0.3 on 2022-05-14 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leaves',
            new_name='Leave',
        ),
    ]
