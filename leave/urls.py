from functools import partial
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from leave import views
from leave.views import *

# urlpatterns = [
#     path('apply_leave',views.apply_leave),
#     path('apply_ODleave',views.apply_ODleave),
#     path('apply_leave_hod',views.apply_leave_hod),
#     path('hod_approval/<int:id>',views.HOD_approval,name='staff_edit'),
#     path('p_approval/<int:id>',views.P_approval,name='staff_edit_P'),
#     path('p_approval_hod/<int:id>',views.P_approval_hod,name='staff_edit_hod')
    
#     ]