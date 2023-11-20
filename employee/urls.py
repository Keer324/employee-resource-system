"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app2.views import *
#from django.contrib import admin
from django.contrib.auth import views as auth_views
#from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls,name="admin-site"),
    path('',welcome,name='welcome'),
    path('leave',leave,name='leave'),
    path('about',about,name="about"),
    path('leavedash',leavedash,name='leavedash'),
    path('a-page',a,name='a-page'),
    path('submit',submit),
    path('register',register,name='register'),
    path('admin_login',admin_login,name="admin_login"),
    #path('leavedas',leavedas,name="leavedas"),
    #path('dashboard',dashboard,name="dashboard"),
    #path('login/', include('django.contrib.auth.urls')),
    #path('login',login,name="login"),
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    #path('login', auth_views.LoginView.as_view(template_name = 'login.html',redirect_authenticated_user=True), name="login"),
    #path('userlogin',login_user, name="login-user"),
    path('home',home, name="home-page"),
    path('homes',homes, name="homes-page"),
    path('logout',logoutuser, name="logout"),
    path('userprofile',userprofile, name="userprofile"),
    path('employees',employees, name="employee-page"),
    path('manage_employees',manage_employees, name="manage_employees-page"),
    path('save_employee',save_employee, name="save-employee-page"),
    path('delete_employee',delete_employee, name="delete-employee"),
    path('view_employee',view_employee, name="view-employee-page"),
    path('departments',departments, name="department-page"),
    path('manage_departments',manage_departments, name="manage_departments-page"),
    path('save_department',save_department, name="save-department-page"),
    path('delete_department',delete_department, name="delete-department"),
    path('positions', positions, name="position-page"),
    path('manage_positions', manage_positions, name="manage_positions-page"),
    path('save_position', save_position, name="save-position-page"),
    path('delete_position',delete_position, name="delete-position"),
    path('delete_leave',delete_leave, name="delete_leave"),
    path('approve_employee',approve_employee,name="approve_employee"),
    path('unapprove_employee',unapprove_employee,name="unapprove_employee"),
    #path('approve_leave',approve_leave, name="approve_leave"),
    path('sub',sub),



     
]
