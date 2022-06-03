from django.contrib import admin
from .models import PersonalDetail
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User

# Register your models here.

# admin.site.register(PersonalDetails)

@admin.register(PersonalDetail)
class PersonDetailsAdmin(ImportExportModelAdmin):
    list_display = ('Staff_ID','Name','Mail_Id','Contact_No','Department', 'Present_Designation','Highest_Qualification','Specialization','total_years','Date_of_joining', 'Recognized_as_a_Research_Guide','If_yes_Number_of_candidates_being_supervised','Password')