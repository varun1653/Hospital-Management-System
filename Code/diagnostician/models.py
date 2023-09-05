from django.db import models
from receptionist.models import DoctorPatientAssignment


class Diagnostician(models.Model):
    DiagnosticianID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100,default="None")
    BloodGroup = models.CharField(max_length=45)
    Salary = models.IntegerField(default=0)
    Age = models.IntegerField(default=0)
    Shift = models.IntegerField(default=0)
    password = models.CharField(max_length=50,default=None,blank=True,null=True)
    contact = models.CharField(max_length=45,default=None)

class Diagnosis(models.Model):
    DiagnosticReportID = models.IntegerField(primary_key=True)
    labreport = models.BooleanField(default=False)
    bill = models.BooleanField(default=False)
    totalbill = models.IntegerField(default=0)
    description = models.CharField(max_length=500,default=None)
    Diagnostician = models.ForeignKey(Diagnostician,on_delete=models.CASCADE,blank=True,null=True)
    Appointment = models.ForeignKey(DoctorPatientAssignment,default=None,on_delete=models.CASCADE)