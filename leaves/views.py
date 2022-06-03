from django.shortcuts import render
from users.models import *
from django.shortcuts import render
from leaves.models import Half_day, Leave, ON_Duty_Leave
from tablib import Dataset
from django.shortcuts import redirect, render
from users.models import PersonalDetail
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from datetime import date, datetime

from django.http import HttpResponse
from django.template.loader import get_template


# Create your views here.

def apply_leave(request):
    if request.session.get('faculty', False):
        Staff_ID = request.session['faculty']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if Leave.objects.filter(user=Staff_ID).exists(): 
            clfull = float(Leave.objects.filter(user=Staff_ID,Leave_type="CL").count())
        else:
            clfull = 0.0
        if Half_day.objects.filter(user=Staff_ID).exists():
            clhalf = float(Half_day.objects.filter(user=Staff_ID,Leave_type="HL").count())
        else:
            clhalf = 0.0
        clcount = clfull + (clhalf/2)
        context = {'check':check,
                    'staff': staff,
                    'staff_id':Staff_ID,
                    'clcount': clcount }
        
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if request.method == "GET":
                    return render(request, "apply_leave_faculty.html",context)
                if request.method == "POST":

                    todate = request.POST['todate']
                    to = todate.split('/')
                    fromdate = request.POST['fromdate']
                    fr = fromdate.split('/')
                    if int(fr[2])>=int(to[2]):
                        if int(fr[1])>=int(to[1]):
                            if int(fr[0])>=int(to[0]):

                                typeof = request.POST['typeof']  
                                ha = request.POST['ha']
                                pa = request.POST['pa']

                                l=Leave(user=Staff_ID,name=check.Name,dept=check.Department,designation=check.Present_Designation,whether_HOD=False,From_date=fromdate,To_date=todate,Leave_type=typeof,Hod_approval=ha,Principal_approval=pa)
                                l.save()
                        
                                return redirect('/my_leaves')
                            else:
                                messages.warning(request, 'Invalid input')
                                return redirect('/leaves/apply_leave')
                        else:
                            messages.warning(request, 'Invalid input')
                            return redirect('/leaves/apply_leave')
                    else:
                        messages.warning(request, 'Invalid input')
                        return redirect('/leaves/apply_leave')
            except:
                messages.warning(request, 'Fill all details to apply leave.')
                return redirect('/leaves/apply_leave')
        else:
            messages.warning(request, 'existence part')
            return redirect('/log-in')
    else:
        messages.warning(request, 'session part')
        return redirect('/log-in')

def apply_half_leave(request):
    if request.session.get('faculty', False):
        Staff_ID = request.session['faculty']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if Leave.objects.filter(user=Staff_ID).exists(): 
            clfull = float(Leave.objects.filter(user=Staff_ID,Leave_type="CL").count())
        else:
            clfull = 0.0
        if Half_day.objects.filter(user=Staff_ID).exists():
            clhalf = float(Half_day.objects.filter(user=Staff_ID,Leave_type="HL").count())
        else:
            clhalf = 0.0
        clcount = clfull + (clhalf/2)
        context = {'check':check,
                    'staff': staff,
                    'staff_id':Staff_ID,
                    'clcount':clcount }
        
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if request.method == "GET":
                    return render(request, "apply_half_leave_faculty.html",context)
                if request.method == "POST":

                    todate = request.POST['todate']
                    to = todate.split('/')
                    fromdate = request.POST['fromdate']
                    fr = fromdate.split('/')
                    if int(fr[2])==int(to[2]):
                        if int(fr[1])==int(to[1]):
                            if int(fr[0])==int(to[0]):
                                
                                time = request.POST['time']
                                typeof = request.POST['typeof'] 
                                ha = request.POST['ha']
                                pa = request.POST['pa']
                                

                                l=Half_day(user=Staff_ID,name=check.Name,dept=check.Department,designation=check.Present_Designation,whether_HOD=False,From_date=fromdate,To_date=todate,Leave_type=typeof,Time=time,Hod_approval=ha,Principal_approval=pa)
                                l.save()
                        
                                return redirect('/my_leaves')
                            else:
                                messages.warning(request, 'Invalid input')
                                return redirect('/leaves/apply_half_leave')
                        else:
                            messages.warning(request, 'Invalid input')
                            return redirect('/leaves/apply_half_leave')
                    else:
                        messages.warning(request, 'Invalid input')
                        return redirect('/leaves/apply_half_leave')
            except:
                messages.warning(request, 'Fill all details to apply leave.')
                return redirect('/leaves/apply_half_leave')
        else:
            messages.warning(request, 'existence part')
            return redirect('/log-in')
    else:
        messages.warning(request, 'session part')
        return redirect('/log-in')

def apply_ODleave(request):
    if request.session.get('faculty', False):
        Staff_ID = request.session['faculty']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        context = {'check':check,
                    'staff': staff,
                    'staff_id':Staff_ID,
                     }
        
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if request.method == "GET":
                    return render(request, "apply_on_duty_leave_faculty.html",context)
                if request.method == "POST":

                    todate = request.POST['todate']
                    to = todate.split('/')
                    fromdate = request.POST['fromdate']
                    fr = fromdate.split('/')
                    if int(fr[2])>=int(to[2]):
                        if int(fr[1])>=int(to[1]):
                            if int(fr[0])>=int(to[0]):

                                pro = request.FILES['proof']  
                                ha = request.POST['ha']
                                pa = request.POST['pa']

                                l=ON_Duty_Leave(user=Staff_ID,name=check.Name,dept=check.Department,designation=check.Present_Designation,whether_HOD=False,From_date=fromdate,To_date=todate,proof=pro,Hod_approval=ha,Principal_approval=pa)
                                l.save()
                        
                                return redirect('/my_leaves')
                            else:
                                messages.warning(request, 'Invalid input')
                                return redirect('/leaves/apply_ODleave')
                        else:
                            messages.warning(request, 'Invalid input')
                            return redirect('/leaves/apply_ODleave')
                    else:
                        messages.warning(request, 'Invalid input')
                        return redirect('/leaves/apply_ODleave')
            except:
                messages.warning(request, 'Fill all details to apply leave.')
                return redirect('/leaves/apply_ODleave')
        else:
            messages.warning(request, 'existence part')
            return redirect('/log-in')
    else:
        messages.warning(request, 'session part')
        return redirect('/log-in')

def apply_leave_hod(request):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if Leave.objects.filter(user=Staff_ID).exists(): 
            clfull = float(Leave.objects.filter(user=Staff_ID,Leave_type="CL").count())
        else:
            clfull = 0.0
        if Half_day.objects.filter(user=Staff_ID).exists():
            clhalf = float(Half_day.objects.filter(user=Staff_ID,Leave_type="HL").count())
        else:
            clhalf = 0.0
        clcount = clfull + (clhalf/2)
        context = {'check':check,
                    'staff': staff,
                    'staff_id':Staff_ID,
                    'clcount':clcount }
        
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if request.method == "GET":
                    return render(request, "apply_leave_hod.html",context)
                if request.method == "POST":

                    todate = request.POST['todate']
                    to = todate.split('/')
                    fromdate = request.POST['fromdate']
                    fr = fromdate.split('/')
                    if int(fr[2])>=int(to[2]):
                        if int(fr[1])>=int(to[1]):
                            if int(fr[0])>=int(to[0]):
                                
                                typeof = request.POST['typeof']  
                                ha = request.POST['ha']
                                pa = request.POST['pa']

                                l=Leave(user=Staff_ID,name=check.Name,dept=check.Department,designation=check.Present_Designation,whether_HOD=True,From_date=fromdate,To_date=todate,Leave_type=typeof,Hod_approval=ha,Principal_approval=pa)
                                l.save()
                        
                                return redirect('/my_leaves')
                            else:
                                messages.warning(request, 'Invalid input')
                                return redirect('/leaves/apply_leave_hod')
                        else:
                            messages.warning(request, 'Invalid input')
                            return redirect('/leaves/apply_leave_hod')
                    else:
                        messages.warning(request, 'Invalid input')
                        return redirect('/leaves/apply_leave_hod')
            except:
                messages.warning(request, 'Fill all details to apply leave.')
                return redirect('/leaves/apply_leave_hod')
        else:
            messages.warning(request, 'existence part')
            return redirect('/log-in')
    else:
        messages.warning(request, 'session part')
        return redirect('/log-in')

def apply_leave_hod_half(request):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if Leave.objects.filter(user=Staff_ID).exists(): 
            clfull = float(Leave.objects.filter(user=Staff_ID,Leave_type="CL").count())
        else:
            clfull = 0.0
        if Half_day.objects.filter(user=Staff_ID).exists():
            clhalf = float(Half_day.objects.filter(user=Staff_ID,Leave_type="HL").count())
        else:
            clhalf = 0.0
        clcount = clfull + (clhalf/2)
        context = {'check':check,
                    'staff': staff,
                    'staff_id':Staff_ID,
                    'clcount':clcount }
        
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if request.method == "GET":
                    return render(request, "apply_half_leave_hod.html",context)
                if request.method == "POST":

                    todate = request.POST['todate']
                    to = todate.split('/')
                    fromdate = request.POST['fromdate']
                    fr = fromdate.split('/')
                    if int(fr[2])>=int(to[2]):
                        if int(fr[1])>=int(to[1]):
                            if int(fr[0])>=int(to[0]):

                                time = request.POST['time']
                                typeof = request.POST['typeof'] 
                                ha = request.POST['ha']
                                pa = request.POST['pa']

                                l=Half_day(user=Staff_ID,name=check.Name,dept=check.Department,designation=check.Present_Designation,whether_HOD=True,From_date=fromdate,To_date=todate,Leave_type=typeof,Time=time,Hod_approval=ha,Principal_approval=pa)
                                l.save()
                        
                                return redirect('/my_leaves')
                            else:
                                messages.warning(request, 'Invalid input')
                                return redirect('/leaves/apply_leave_hod_half')
                        else:
                            messages.warning(request, 'Invalid input')
                            return redirect('/leaves/apply_leave_hod_half')
                    else:
                        messages.warning(request, 'Invalid input')
                        return redirect('/leaves/apply_leave_hod_half')
            except:
                messages.warning(request, 'Fill all details to apply leave.')
                return redirect('/leaves/apply_leave_hod_half')
        else:
            messages.warning(request, 'existence part')
            return redirect('/log-in')
    else:
        messages.warning(request, 'session part')
        return redirect('/log-in')


def HOD_approval(request, id):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        dept = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if Leave.objects.filter(id=id).exists():
                form = Leave.objects.get(id=id)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'hod_approval.html', context)
                if request.method == "POST":

                    ha = request.POST['typeof']

                    form.Hod_approval = ha

                    form.save()
                    return redirect('/staff')

def HOD_approval_half(request, id):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        dept = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if Half_day.objects.filter(id=id).exists():
                form = Half_day.objects.get(id=id)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'hod_approval_half.html', context)
                if request.method == "POST":

                    ha = request.POST['typeof']

                    form.Hod_approval = ha

                    form.save()
                    return redirect('/staff')

def P_approval(request, id):
    if request.session.get('principal', False):
        Staff_ID = request.session['principal']
        dept = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if Leave.objects.filter(id=id).exists():
                form = Leave.objects.get(id=id)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'p_approval.html', context)
                if request.method == "POST":

                    pa = request.POST['typeof']

                    form.Principal_approval = pa

                    form.save()
                    return redirect('/staff_P')

def P_approval_half(request, id):
    if request.session.get('principal', False):
        Staff_ID = request.session['principal']
        dept = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if Half_day.objects.filter(id=id).exists():
                form = Half_day.objects.get(id=id)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'p_approval_half.html', context)
                if request.method == "POST":

                    pa = request.POST['typeof']

                    form.Principal_approval = pa

                    form.save()
                    return redirect('/staff_P')

def P_approval_hod(request, id):
    if request.session.get('principal', False):
        Staff_ID = request.session['principal']
        dept = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if Leave.objects.filter(id=id).exists():
                form = Leave.objects.get(id=id)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'p_approval_hod.html', context)
                if request.method == "POST":

                    pa = request.POST['typeof']

                    form.Principal_approval = pa

                    form.save()
                    return redirect('/staff_hod')

def P_approval_hod_half(request, id):
    if request.session.get('principal', False):
        Staff_ID = request.session['principal']
        dept = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if Leave.objects.filter(id=id).exists():
                form = Half_day.objects.get(id=id)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'p_approval_hod_half.html', context)
                if request.method == "POST":

                    pa = request.POST['typeof']

                    form.Principal_approval = pa

                    form.save()
                    return redirect('/staff_hod')