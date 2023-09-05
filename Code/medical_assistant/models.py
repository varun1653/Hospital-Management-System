from django.db import models
from receptionist.models import DoctorPatientAssignment
from doctor.models import Doctor
# # Create your models here.

class MedicalAssistant(models.Model):
    MedicalAssistantID = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=45,default=None)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField(default=None)
    Salary = models.IntegerField(default=None)
    Shift = models.IntegerField(default=None)
    BloodGroup = models.CharField(max_length=45)
    underDoctor = models.ForeignKey(Doctor,default=None,on_delete=models.CASCADE)
    contact = models.CharField(max_length=45,default=None)

class MedicalReport(models.Model):
    ReportID = models.IntegerField(primary_key=True)
    report = models.BooleanField(default=False)
    Appointment = models.ForeignKey(DoctorPatientAssignment,default=None,on_delete=models.CASCADE)
    MedicalAssistant = models.ForeignKey(MedicalAssistant,default=None,on_delete=models.CASCADE)
