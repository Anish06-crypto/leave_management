from django.core.validators import MaxLengthValidator
from django.db.models.deletion import CASCADE
from django.db import models
from django.db.models.fields import CharField
from datetime import datetime

# Create your models here.
    
class PersonalDetail(models.Model):


    Name = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    Present_Designation = models.CharField(max_length=200)
    Whether_HOD = models.BooleanField(default=False)
    Highest_Qualification = models.CharField(max_length=200)
    Recognized_as_a_Research_Guide = models.CharField(max_length=100)
    Years_of_Service_at_MITM = models.CharField(max_length=10,null=True,default=0)
    Staff_ID = models.CharField(max_length=20, unique=True)
    Password = models.CharField(max_length=50)
    Mail_Id = models.EmailField()
    Contact_No = models.CharField(max_length=10)
    Date_of_joining = models.CharField(max_length=20,null=True)
    Specialization = models.CharField(max_length=100)
    If_yes_Number_of_candidates_being_supervised = models.CharField(max_length=100, null=True)
    total_years = models.IntegerField(null=True)

    def __str__(self):
        return self.Staff_ID
    
    def save(self,*args, **kwargs):
        self.calculateAge()
        super(PersonalDetail, self).save(*args, **kwargs)
    
 
    def calculateAge(self):
        currentDate = datetime.now()
        join = datetime.strptime(str(self.Date_of_joining), "%Y-%m-%d %H:%M:%S")
        daysLeft = currentDate - join

        years = ((daysLeft.total_seconds())/(365.242*24*3600))
        yearsInt=int(years)

        months=(years-yearsInt)*12
        monthsInt=int(months)

        self.Years_of_Service_at_MITM = str(yearsInt) + ":" + str(monthsInt)

        return self.Years_of_Service_at_MITM
                

    
    
    
