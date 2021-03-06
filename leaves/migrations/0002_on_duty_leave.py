# Generated by Django 4.0.3 on 2022-05-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ON_Duty_Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('dept', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('whether_HOD', models.BooleanField(default=False)),
                ('From_date', models.CharField(max_length=10)),
                ('To_date', models.CharField(max_length=10)),
                ('proof', models.FileField(null=True, upload_to='onduty')),
                ('Hod_approval', models.CharField(max_length=100, null=True)),
                ('Principal_approval', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
