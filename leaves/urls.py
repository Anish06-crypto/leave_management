from functools import partial
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from leaves import views
from leaves.views import *

urlpatterns = [
    path('apply_leave',views.apply_leave),
    path('apply_half_leave',views.apply_half_leave),
    path('apply_ODleave',views.apply_ODleave),
    path('apply_leave_hod',views.apply_leave_hod),
    path('apply_leave_hod_half',views.apply_leave_hod_half),
    path('hod_approval/<int:id>',views.HOD_approval,name='staff_edit'),
    path('hod_approval_half/<int:id>',views.HOD_approval_half,name='staff_edit_half'),
    path('p_approval/<int:id>',views.P_approval,name='staff_edit_P'),
    path('p_approval_half/<int:id>',views.P_approval_half,name='staff_edit_P_half'),
    path('p_approval_hod/<int:id>',views.P_approval_hod,name='staff_edit_hod'),
    path('p_approval_hod_half/<int:id>',views.P_approval_hod_half,name='staff_edit_hod_half')
    
    ]