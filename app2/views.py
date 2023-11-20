from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from app2.models import *
from django.contrib import messages
from .models import LeaveRequest
#from e.models import Department, Position, Employees
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
import json


# Create your views here

employees = [

    {
        'code':1,
        'name':"John D Smith",
        'contact':'09123456789',
        'address':'Sample Address only'
    },{
        'code':2,
        'name':"Claire C Blake",
        'contact':'09456123789',
        'address':'Sample Address2 only'
    }

]


#user login 
def welcome(request):
    return render(request,'welcome.html')

def about(request):
    return render(request,'about.html')

def leave(request):
    return render(request,'leavelog.html')

def leavedash(request):
    context = {
        'page_title':'Home',
        'total_LeaveRequest':len(LeaveRequest.objects.all()),
    }
    return render(request,'employedash.html',context)

def userprofile(request):
    return render(request,'employe_profile.html')
    #user=request.user
    #if user.is_authenticated:
        #employee = Employees.objects.filter(user=user).first()
        #dataset = dict()
        #dataset['employee'] = employee
        #return render(request,"employe_profile.html",dataset)
    #return HttpResponse("Sorry , not authenticated for this,admin or whoever you are :)")
    #return render(request,"employedash.html",{"employee":user_details})
    #print(employee)
    #if email in employee:
        #user_details = Employees.objects.filter(email=email)
    #return render(request,"employedash.html",{"employee":user_details})
    #return HttpResponse()
    #employee = Employees.objects.filter(email=email)
    #return render(request,"employe_profile.html",{"employee":employee})


    #user = Employees.objects.filter(email = email)
    #return render(request,'employe_profile.html',{"registerDetails":user})
    #return HttpResponse()

    #return HttpResponse("Sorry , not authenticated for this,admin or whoever you are :)")





#def a(request):
    #all_data = LeaveRequest.objects.all()
    #return render(request, 'a.html', {'all_data':all_data})
        

#dashboard_app
 
def register(request):
    return render(request,'log.html')


#user login
def submit(request): 
    email = request.POST.get('email')
    code = request.POST.get('code')
    user_list = Employees.objects.values_list('email',flat=True)
    print(user_list)
    if email in user_list:
        user_details = Employees.objects.filter(email=email)
        messages.info(request,'invalid credentials')
        return render(request,"employe_profile.html",{"registerDetails":user_details})
        return HttpResponse()

          
def admin_login(request):
    error=""
    if request.method =="POST":
        u=request.POST['username']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        if user.is_staff:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request,'admin_login.html',locals())


def homes(request):
    context = {
        'page_title':'Home',
        'employees':employees,
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(Employees.objects.all()),
        'total_LeaveRequest':len(LeaveRequest.objects.all()),
    }
    return render(request,'home2.html',context) 




#def login_user(request):
 
         


def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    context = {
        'page_title':'Home',
        'employees':employees,
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(Employees.objects.all()),
        'total_LeaveRequest':len(LeaveRequest.objects.all()),
    }
    return render(request,'home.html',context) 


 


def departments(request):
    department_list = Department.objects.all()
    context = {
        'page_title':'Departments',
        'departments':department_list,
    }
    return render(request, 'departments.html',context) 


def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'manage_department.html',context)

#@login_required
def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_department = Department(name=data['name'], description = data['description'],status = data['status'])
            save_department.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

#@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")




# Employees
def employees(request):
    employee_list = Employees.objects.all()
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    return render(request, 'employees.html',context)

def manage_employees(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'manage_employee.html',context)

#@login_required
def save_employee(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Employees.objects.exclude(id = data['id']).filter(code = data['code'])
    else:
        check  = Employees.objects.filter(code = data['code'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dept = Department.objects.filter(id=data['department_id']).first()
            pos = Position.objects.filter(id=data['position_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employees.objects.filter(id = data['id']).update(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
            else:
                save_employee = Employees(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
                save_employee.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"code":data['code'], "firstname" : data['firstname'],"middlename" : data['middlename'],"lastname" : data['lastname'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department_id" : data['department_id'],"position_id" : data['position_id'],"date_hired" : data['date_hired'],"salary" : data['salary'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

#@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

#@login_required
def view_employee(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'view_employee.html',context)


 





def positions(request):
    position_list = Position.objects.all()
    context = {
        'page_title':'Positions',
        'positions':position_list,
    }
    return render(request, 'positions.html',context)


def manage_positions(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'manage_position.html',context)

def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_position = Position(name=data['name'], description = data['description'],status = data['status'])
            save_position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")





#leave module
def a(request):
    LeaveRequest_list= LeaveRequest.objects.all()
    context = {
        'page_title':'LeaveRequest',
        'employeess':LeaveRequest_list,
    

    }
    return render(request, 'leavelist.html',context)

def delete_leave(request):
    data =  request.POST
    resp = {'status':''}
    try:
        LeaveRequest.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

 
def sub(request):
    code = request.POST.get('code')
    leave_type = request.POST.get('leave_type')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    reason = request.POST.get('reason')
    user = LeaveRequest.objects.values_list("leave_type",flat=True)
    LeaveRequest(leave_type=leave_type, start_date=start_date, end_date=end_date, reason=reason, code=code).save()
    return render(request,"leavelog.html",{'error':'leave applied SUCESSFUL'})


def approve_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id'])
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


def unapprove_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id'])
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")



#def approve_employee(request):
    #data = request.POST
    #resp = {'status': ''}
    #try:
        #employee = Employees.objects.get(id=data['id'])
        #employee.approved = True
        #employee.save()
        #resp['status'] = 'success'
    #except Employees.DoesNotExist:
        #resp['status'] = 'failed'
    #return HttpResponse(json.dumps(resp), content_type="application/json")


#def unapprove_employee(request):
    #data = request.POST
    #resp = {'status': ''}
    #try:
        #employee = Employees.objects.get(id=data['id'])
        #employee.approved = False
        #employee.save()
        #resp['status'] = 'success'
    #except Employees.DoesNotExist:
        #resp['status'] = 'failed'
    #return HttpResponse(json.dumps(resp), content_type="application/json")



