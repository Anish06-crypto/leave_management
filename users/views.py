from django.shortcuts import render

from leaves.models import Half_day, Leave, ON_Duty_Leave
from users.filters import DepartmentFilter, HalfFilter
from .resources import PersonDetailsResource
from .models import PersonalDetail
from tablib import Dataset
from django.shortcuts import redirect, render
from .resources import PersonDetailsResource
from users.models import PersonalDetail
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from datetime import date, datetime

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


def simple_upload(request):
    if request.method == 'POST':
            person_resource = PersonDetailsResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read(),format='xlsx')
            #print(imported_data)
            for data in imported_data:
                print(data[1])
                value = PersonalDetail(
                            data[0],
                            data[1],
                            data[2],
                            data[3],
                            data[4],
                            data[5],
                            data[6],
                            data[7],
                            data[8],
                            data[9],
                            data[10],
                            data[11],
                            data[12],
                            data[13],
                            )
                value.save()       
            
            #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

            #if not result.has_errors():
            #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'input.html')

def grade_pdf(request):
     if request.session.get('principal',False):
        principal_id = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=principal_id).exists():
            tle = Leave.objects.all()
            template_path = 'all_faculty_list_pdf.html'
            context = { 'tle' : tle }
            
            response = HttpResponse(content_type='applicaton/pdf')

            response['Content-Disposition'] = 'attachment; filename="leave_report.pdf"'

            template = get_template(template_path)
            html = template.render(context)

            pisa_status = pisa.CreatePDF(
                html, dest=response
            )

            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        staff_id = request.POST['Staff_ID']
        password = request.POST['Password']
        if PersonalDetail.objects.filter(Staff_ID=staff_id).exists():
            faculty = PersonalDetail.objects.filter(Staff_ID=staff_id)[0]
            if faculty.Password == password and (PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Assistant Professor').exists() 
                or PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Associate Professor').exists()) or PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Professor').exists():  
                    request.session['faculty'] = faculty.Staff_ID
                    faculty = PersonalDetail.objects.get(Staff_ID=request.session['faculty'])
            
                    context = { "faculty":faculty }
                    return redirect('/leaves/apply_leave',context)
            elif faculty.Password == password and PersonalDetail.objects.filter(Staff_ID=staff_id,Whether_HOD=True).exists():
                    request.session['hod'] = faculty.Staff_ID
                    request.session.set_expiry(3000)
                    return redirect('/staff')
            elif faculty.Password == password and PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Principal').exists():
                request.session['principal'] = faculty.Staff_ID
                return redirect('/staff_P')
            elif faculty.Password == password and PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Admin').exists():
                request.session['admin'] = faculty.Staff_ID
                return redirect('/adminmit')
            else:
                return_obj = {"isPasswordInvalid": True, "email": staff_id}
                return render(request, "login.html", return_obj)
        else:
            return_obj = {"isEmailInvalid": True}
            return render(request, "login.html", return_obj)
        return redirect('/')

def logOut(request):
    request.session.flush()
    return redirect('/log-in')

def admin(request):
    return render(request,'admin.html')


def self_list(request):
    if request.session.get('faculty',False):
        faculty_id = request.session['faculty']
        if PersonalDetail.objects.filter(Staff_ID=faculty_id).exists():
            faculty = PersonalDetail.objects.filter(Staff_ID=faculty_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = Leave.objects.all()
            ole = Half_day.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=faculty_id)
            if Leave.objects.filter(user=faculty_id).exists(): 
                clfull = float(Leave.objects.filter(user=faculty,Leave_type="CL").count())
            else:
                clfull = 0.0
            if Half_day.objects.filter(user=faculty_id).exists():
                clhalf = float(Half_day.objects.filter(user=faculty_id,Leave_type="HL").count())
            else:
                clhalf = 0.0
            clcount = clfull + (clhalf/2)
            sclcount = Leave.objects.filter(user=faculty,Leave_type="SCL").count()
            oodcount = Leave.objects.filter(user=faculty,Leave_type="OOD").count()
            staff.save()
            context = {'staffs': staffs, 
                        'faculty': faculty,
                        'tle' : tle,
                        'ole' : ole,
                        'sclcount' : sclcount,
                        'clcount' : clcount,
                        'oodcount' : oodcount,
                        "staff":staff }
            return render(request, 'faculty_self_leaves.html', context)
    elif request.session.get('hod',False):
        hod_id = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=hod_id).exists():
            hod = PersonalDetail.objects.filter(Staff_ID=hod_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = Leave.objects.all()
            ole = Half_day.objects.all()    
            staff = PersonalDetail.objects.get(Staff_ID=hod_id)
            if Leave.objects.filter(user=hod_id).exists(): 
                clfull = float(Leave.objects.filter(user=hod,Leave_type="CL").count())
            else:
                clfull = 0.0
            if Half_day.objects.filter(user=hod_id).exists():
                clhalf = float(Half_day.objects.filter(user=hod_id,Leave_type="HL").count())
            else:
                clhalf = 0.0
            clcount = clfull + (clhalf/2)
            sclcount = Leave.objects.filter(user=hod_id,Leave_type="SCL").count()
            oodcount = Leave.objects.filter(user=hod_id,Leave_type="OOD").count()
            staff.save()
            context = {'staffs': staffs, 
                        'hod': hod,
                        'tle' : tle,
                        'ole' : ole,
                        'sclcount' : sclcount,
                        'clcount' : clcount,
                        'oodcount' : oodcount,
                        "staff":staff }
            return render(request, 'hod_self_leaves.html', context)

def staff_list(request):
    if request.session.get('hod',False):
        hod_id = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=hod_id).exists():
            hod = PersonalDetail.objects.filter(Staff_ID=hod_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = Leave.objects.all()
            ole = Half_day.objects.all()
            if Leave.objects.filter(user=hod_id).exists(): 
                clfull = float(Leave.objects.filter(user=hod,Leave_type="CL").count())
            else:
                clfull = 0.0
            if Half_day.objects.filter(user=hod_id).exists():
                clhalf = float(Half_day.objects.filter(user=hod_id,Leave_type="HL").count())
            else:
                clhalf = 0.0
            clcount = clfull + (clhalf/2)
            staff = PersonalDetail.objects.get(Staff_ID=hod_id)
            tlecount = Leave.objects.filter(dept=hod.Department,whether_HOD=False).count()
            hlecount = Half_day.objects.filter(dept=hod.Department,whether_HOD=False).count()
            context = {'staffs': staffs, 
                        'hod': hod,
                        'tle' : tle,
                        'ole' : ole,
                        'tlecount' : tlecount,
                        'hlecount' : hlecount,
                        "staff":staff,
                        'clcount':clcount }
            return render(request, 'department_faculty_list.html', context)

def staff_list_P(request):
    if request.session.get('principal',False):
        p_id = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=p_id).exists():
            p = PersonalDetail.objects.filter(Staff_ID=p_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = Leave.objects.all()
            ole = Half_day.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=p_id)
            myFilter = DepartmentFilter(request.GET, queryset=tle)
            tle = myFilter.qs
            tlecount = Leave.objects.filter(whether_HOD=False).count()
            myFilterhalf = HalfFilter(request.GET, queryset=ole)
            ole = myFilterhalf.qs
            hlecount = Half_day.objects.filter(whether_HOD=False).count()
            context = {'staffs': staffs, 
                        'p': p,
                        'tle' : tle,
                        'ole' : ole,
                        'filter':myFilter,
                        'filterhalf':myFilterhalf,
                        'tlecount' : tlecount,
                        'hlecount' : hlecount,
                        "staff":staff }
            return render(request, 'all_faculty_list.html', context)

def staff_list_hod_P(request):
    if request.session.get('principal',False):
        p_id = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=p_id).exists():
            p = PersonalDetail.objects.filter(Staff_ID=p_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = Leave.objects.all()
            ole = Half_day.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=p_id)
            myFilter = DepartmentFilter(request.GET, queryset=tle)
            tle = myFilter.qs
            tlecount = Leave.objects.filter(whether_HOD=True).count()
            myFilterhalf = HalfFilter(request.GET, queryset=ole)
            ole = myFilterhalf.qs
            hlecount = Half_day.objects.filter(whether_HOD=False).count()
            context = {'staffs': staffs, 
                        'p': p,
                        'tle' : tle,
                        'ole' : ole,
                        'filter': myFilter,
                        'filterhalf': myFilterhalf,
                        'tlecount' : tlecount,
                        'hlecount' : hlecount,
                        "staff":staff }
            return render(request, 'all_hod_list.html', context)