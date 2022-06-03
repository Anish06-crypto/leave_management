from functools import partial
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
   
    path('input',views.simple_upload),
    path('log-in',views.login),
    path('adminmit',views.admin),
    path('log-out',views.logOut),
    path('my_leaves',views.self_list),
    path('staff',views.staff_list),
    path('staff_P',views.staff_list_P),
    path('staff_hod',views.staff_list_hod_P),
    path('leave_pdf', views.grade_pdf, name='leave_pdf'),
    

    ]