# Generated by Django 4.0.3 on 2022-06-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0005_remove_half_day_cl_half_day_leave_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='half_day',
            name='Time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
