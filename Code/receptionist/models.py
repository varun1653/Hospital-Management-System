from django.db import models
from patient.models import Patient
from doctor.models import Doctor

class Receptionist(models.Model):
    ReceptionistID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField(default=None)
    Salary = models.IntegerField(default=None)
    Shift = models.IntegerField(default=None)
    BloodGroup = models.CharField(max_length=45)
    password = models.CharField(max_length=50,default=None)
    contact = models.CharField(max_length=45,default=None)

class DoctorPatientAssignment(models.Model):
    class Meta:
        unique_together = (('AppointmentID','VisitNo'),)
    Doctor = models.ForeignKey(Doctor,default=None,on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient,default=None,on_delete=models.CASCADE)
    Receptionist = models.ForeignKey(Receptionist,default=None,on_delete=models.CASCADE)
    AppointmentID = models.IntegerField(default=None)
    VisitNo = models.IntegerField(default=None)
    datetime = models.DateTimeField(default=None)
    status = models.CharField(max_length=50,default='Unattended')

    


