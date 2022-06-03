from django.contrib import admin

from leaves.models import Half_day, Leave, ON_Duty_Leave

# Register your models here.

admin.site.register(Leave)
admin.site.register(ON_Duty_Leave)
admin.site.register(Half_day)