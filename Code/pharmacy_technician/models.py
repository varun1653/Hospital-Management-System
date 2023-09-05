from django.db import models
from receptionist.models import DoctorPatientAssignment
# # Create your models here.


class PharmacyTechnician(models.Model):
    PharmacyTechnicianID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField(default=None)
    Salary = models.IntegerField(default=None)
    Shift = models.IntegerField(default=None)
    BloodGroup = models.CharField(max_length=45)
    contact = models.CharField(max_length=45,default=None)
    password = models.CharField(max_length=50,default=None)

class PharmacyBill(models.Model):
    PharmacyBillID = models.IntegerField(primary_key=True)
    PharmacyTechnician = models.ForeignKey(PharmacyTechnician,default=None,blank=True,null=True,on_delete=models.CASCADE)
    bill = models.BooleanField(default=False)
    totalbill = models.IntegerField(default=0)
    Appointment = models.ForeignKey(DoctorPatientAssignment,default=None,on_delete=models.CASCADE)