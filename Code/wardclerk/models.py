from email.policy import default
from django.db import models
from patient.models import Patient
from receptionist.models import DoctorPatientAssignment
class Ward(models.Model):
    WardType = models.CharField(max_length=45,default="usual",primary_key=True)
    WardCapacity=models.IntegerField()
    Population = models.IntegerField()  
class WardClerk(models.Model):
    WardClerkID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Ward = models.ForeignKey(Ward,default=None,on_delete=models.CASCADE)
    Age = models.IntegerField(default=None)
    Salary = models.IntegerField(default=None)
    Shift = models.IntegerField(default=None)
    BloodGroup = models.CharField(max_length=45)
    contact = models.CharField(max_length=13,default=None)
    password = models.CharField(max_length=50,default=None,blank=True,null=True)



class WardDetails(models.Model):
    Appointment = models.ForeignKey(DoctorPatientAssignment,primary_key=True,default=None,unique=True,on_delete=models.CASCADE)
    wardbill = models.BooleanField(default=False)
    totalbill = models.IntegerField(default=0)
    Ward = models.ForeignKey(Ward,default=None,on_delete=models.CASCADE)
    BedNo = models.IntegerField(default=None)
    Description = models.CharField(max_length=500)
    JoinedDate = models.DateTimeField()
    LeftDate = models.DateTimeField(default=None,blank=True,null=True)