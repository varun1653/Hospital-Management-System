from django.db import models
from receptionist.models import DoctorPatientAssignment
# # Create your models here.

class Biller(models.Model):
    BillerID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    password = models.CharField(max_length=45,default=None)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField(default=None)
    Salary = models.IntegerField(default=None)
    Shift = models.IntegerField(default=None)
    BloodGroup = models.CharField(max_length=45)
    contact = models.CharField(max_length=45,default=None)

class HospitalBills(models.Model):
    Appointment = models.ForeignKey(DoctorPatientAssignment,default=None,on_delete=models.CASCADE)
    Biller = models.ForeignKey(Biller,default=None,blank=True,null=True,on_delete=models.CASCADE)
    TotalBill = models.IntegerField(default=0)
    AmountPaid = models.IntegerField(default=0)
    FullyPaidDate = models.DateTimeField(blank=True, null=True)
    BillID = models.IntegerField(primary_key=True)
