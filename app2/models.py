from django.db import models
#from django.db import models
from django.utils import timezone
from datetime import datetime
#from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Employees(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '


class LeaveRequest(models.Model):
    LEAVE_TYPES = [
        ('vacation', 'Vacation'),
        ('sick_leave', 'Sick Leave'),
        ('personal_leave', 'Personal Leave'),
    ]
    #user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    code = models.CharField(max_length=100,blank=True) 
    leave_type = models.CharField(max_length=50, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    #status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')))
    #is_approved = models.BooleanField(default=False) #hide


    #def leave_approved(self):
        #return self.is_approved == True




    
    #def approve_leave(self):
        #if not self.is_approved:
            #self.is_approved = True
            #self.status = 'approved'
            #self.save()




    
    #def unapprove_leave(self):
        #if self.is_approved:
            #self.is_approved = False
            #self.status = 'pending'
            #self.save()
