from leaves.models import Half_day, Leave
import django_filters
from django_filters import DateFilter, CharFilter
from django_filters.filters import BooleanFilter

from .models import *

class DepartmentFilter(django_filters.FilterSet):
    
    class Meta:
        model = Leave
        fields = ['dept','designation','From_date','To_date','Hod_approval']

class HalfFilter(django_filters.FilterSet):
    
    class Meta:
        model = Half_day
        fields = ['dept','designation','From_date','To_date','Hod_approval']
        