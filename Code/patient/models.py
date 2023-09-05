from django.db import models

# Create your models here.
class Patient(models.Model):
    PatientID = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50,default=None)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    Age = models.CharField(max_length=40,default=None)
    BloodGroup = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    gender = models.CharField(max_length=40,default=None)
    contact = models.CharField(max_length=40,default=None)
    Height = models.CharField(max_length=40,default=None)
    Weight = models.CharField(max_length=40,default=None)
