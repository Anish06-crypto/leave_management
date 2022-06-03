from email.policy import default
from django.db import models
from django.forms import DateField

# Create your models here.


class Leave(models.Model):

    user = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=200,null=True)
    dept = models.CharField(max_length=200,null=True)
    designation = models.CharField(max_length=200,null=True)
    whether_HOD = models.BooleanField(default=False)
    From_date = models.CharField(max_length=10)
    To_date = models.CharField(max_length=10)
    Leave_type = models.CharField(max_length=100, null=True)
    Hod_approval = models.CharField(max_length=100, null=True)
    Principal_approval = models.CharField(max_length=100, null=True)
    cl = models.IntegerField(null=True)
    scl = models.IntegerField(null=True)
    ood = models.IntegerField(null=True)

    def __str__(self):
        return self.user