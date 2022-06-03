from django.db import models
from import_export import resources
from .models import PersonalDetail

class PersonDetailsResource(resources.ModelResource):
    class meta:
        model = PersonalDetail
