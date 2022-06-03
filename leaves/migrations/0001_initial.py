# Generated by Django 4.0.3 on 2022-05-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('dept', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('whether_HOD', models.BooleanField(default=False)),
                ('From_date', models.CharField(max_length=10)),
                ('To_date', models.CharField(max_length=10)),
                ('Leave_type', models.CharField(max_length=100, null=True)),
                ('Hod_approval', models.CharField(max_length=100, null=True)),
                ('Principal_approval', models.CharField(max_length=100, null=True)),
                ('cl', models.IntegerField(null=True)),
                ('scl', models.IntegerField(null=True)),
                ('ood', models.IntegerField(null=True)),
            ],
        ),
    ]
