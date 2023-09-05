from django.db import models

# Create your models here.
  
class Doctor(models.Model):
    DoctorID = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50,default=None)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField(default=0)
    Salary = models.IntegerField(default=0)
    Shift = models.IntegerField(default=0)
    BloodGroup = models.CharField(max_length=45)
    Department = models.CharField(max_length=45,default=None)
    status = models.CharField(max_length=45,default=None) 
    contact = models.CharField(max_length=15,default=None)