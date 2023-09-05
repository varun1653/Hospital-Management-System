from django.db import models

# Create your models here.
class Administrator(models.Model):
    AdministratorID = models.IntegerField(primary_key=True)
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