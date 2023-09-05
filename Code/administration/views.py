from django.shortcuts import render
from wardclerk.models import Ward
from doctor.models import Doctor
from patient.models import Patient
from medical_assistant.models import MedicalAssistant
from billing_desk.models import Biller
from diagnostician.models import Diagnostician
from receptionist.models import Receptionist
from pharmacy_technician.models import PharmacyTechnician
from wardclerk.models import WardClerk
from django.http import HttpResponseRedirect
# Create your views here.

def adminhome(request):
    if request.method=="POST":
        if request.POST["staffCategory"] == "Doctor":
            return HttpResponseRedirect('/administration/addDoctor/') 
        elif request.POST["staffCategory"] == "MedicalAssistant":
            return HttpResponseRedirect('/administration/addMedicalAssistant/') 
        elif request.POST["staffCategory"] == "Biller":
            return HttpResponseRedirect('/administration/addbiller/') 
        elif request.POST["staffCategory"] == "Diagnostician":
            return HttpResponseRedirect('/administration/addDiagnostician/') 
        elif request.POST["staffCategory"] == "Receptionist":
            return HttpResponseRedirect('/administration/addReceptionist/') 
        elif request.POST["staffCategory"] == "PharmacyTechnician":
            return HttpResponseRedirect('/administration/addPharmacyTechnician/') 
        elif request.POST["staffCategory"] == "WardClerk":
            return HttpResponseRedirect('/administration/addWardClerk/')
        else:
            return HttpResponseRedirect('/administration/adminhome/')
    if 'AdministratorID'  in request.session :
        patients = Patient.objects.all()
        doctors = Doctor.objects.all()
        medicalAssistants = MedicalAssistant.objects.all()
        billers= Biller.objects.all()
        diagnosticians= Diagnostician.objects.all()
        receptionists= Receptionist.objects.all()
        pharmacyTechnicians=PharmacyTechnician.objects.all()
        wardClerks=WardClerk.objects.all()
        allD={
            'patients' : patients,
            'doctors' : doctors,
            'medicalAssistants' : medicalAssistants,
            'billers' : billers,
            'diagnosticians' : diagnosticians,
            'receptionists' : receptionists,
            'pharmacyTechnicians' : pharmacyTechnicians,
            'wardClerks' :wardClerks ,
        }
        return render(request,'administration/adminhome.html',allD)
    else:
        return HttpResponseRedirect('/stafflogin')
def addbiller(request):
    if request.method == "POST":
        staff=Biller.objects.create(
            BillerID = Biller.objects.all().count()+1,
            FirstName = request.POST["FirstName"],
            password =  request.POST["password"],
            LastName =  request.POST["LastName"],
            EmailAddress =  request.POST["EmailAddress"],
            PermantAddress =  request.POST["PermantAddress"],
            Age =  request.POST["Age"],
            Salary =  request.POST["Salary"],
            Shift =  request.POST["Shift"],
            BloodGroup =  request.POST["BloodGroup"],
            contact = request.POST["contact"],
        )
        staff.save()
        return HttpResponseRedirect('/administration/adminhome/') 
    else:
        return render(request,'administration/REGISTER_BILLER.html')

def addDoctor(request):
    if request.method == "POST":
        staff=Doctor.objects.create(
            DoctorID = Doctor.objects.all().count()+1,
            FirstName = request.POST["FirstName"],
            password = request.POST["password"],
            LastName = request.POST["LastName"],
            EmailAddress = request.POST["EmailAddress"],
            PermantAddress = request.POST["PermantAddress"],
            Age = request.POST["Age"],
            Salary = request.POST["Salary"],
            Shift = request.POST["Shift"],
            BloodGroup = request.POST["BloodGroup"],
            Department = request.POST["Department"],
            status = request.POST["Status"],
            contact = request.POST["contact"],
        )
        staff.save()
        return HttpResponseRedirect('/administration/adminhome/') 
    else:
        return render(request,'administration/REGISTER_DOCTOR.html')


def addMedicalAssistant(request):
    if request.method == "POST":
        staff=MedicalAssistant.objects.create(
            MedicalAssistantID = MedicalAssistant.objects.all().count()+1,
            FirstName = request.POST["FirstName"],
            password = request.POST["password"],
            LastName = request.POST["LastName"],
            EmailAddress = request.POST["EmailAddress"],
            PermantAddress = request.POST["PermantAddress"],
            Age = request.POST["Age"],
            Salary = request.POST["Salary"],
            Shift = request.POST["Shift"],
            BloodGroup = request.POST["BloodGroup"],
            contact = request.POST["contact"],
            underDoctor = Doctor.objects.filter(DoctorID = request.POST["underDoctor"]).first()
        )
        staff.save()
        return HttpResponseRedirect('/administration/adminhome/') 
    else:
        return render(request,'administration/REGISTER_MEDICAL_ASSISTANT.html')


def addDiagnostician(request):
    if request.method == "POST":
        staff=Diagnostician.objects.create(
            DiagnosticianID = Diagnostician.objects.all().count()+1,
            FirstName = request.POST["FirstName"],
            password = request.POST["password"],
            LastName = request.POST["LastName"],
            EmailAddress = request.POST["EmailAddress"],
            PermantAddress = request.POST["PermantAddress"],
            Age = request.POST["Age"],
            Salary = request.POST["Salary"],
            Shift = request.POST["Shift"],
            contact = request.POST["contact"],
            BloodGroup = request.POST["BloodGroup"],
        )
        staff.save()
        return HttpResponseRedirect('/administration/adminhome/') 
    else:
        return render(request,'administration/REGISTER_DIAGNOSTICIAN.html')

def addReceptionist(request):
    if request.method == "POST":
        staff=Receptionist.objects.create(
            ReceptionistID = Receptionist.objects.all().count()+1,
            FirstName = request.POST["FirstName"],
            password = request.POST["password"],
            LastName = request.POST["LastName"],
            EmailAddress = request.POST["EmailAddress"],
            PermantAddress = request.POST["PermantAddress"],
            Age = request.POST["Age"],
            Salary = request.POST["Salary"],
            Shift = request.POST["Shift"],
            contact = request.POST["contact"],
            BloodGroup = request.POST["BloodGroup"],
        )
        staff.save()
        return HttpResponseRedirect('/administration/adminhome/') 
    else:
        return render(request,'administration/REGISTER_RECEPTIONIST.html')

def addPharmacyTechnician(request):
    if request.method == "POST":
        staff=PharmacyTechnician.objects.create(
            PharmacyTechnicianID = PharmacyTechnician.objects.all().count()+1,
            FirstName = request.POST["FirstName"],
            password = request.POST["password"],
            LastName = request.POST["LastName"],
            EmailAddress = request.POST["EmailAddress"],
            PermantAddress = request.POST["PermantAddress"],
            Age = request.POST["Age"],
            Salary = request.POST["Salary"],
            Shift = request.POST["Shift"],
            BloodGroup = request.POST["BloodGroup"],
            contact = request.POST["contact"],
        )
        staff.save()
        return HttpResponseRedirect('/administration/adminhome/') 
    else:
        return render(request,'administration/REGISTER_PHARMACY_TECHNICIAN.html')


def addWardClerk(request):
    if request.method == "POST":
        staff=WardClerk.objects.create(
            WardClerkID = WardClerk.objects.all().count()+1,
            FirstName = request.POST["FirstName"],
            password = request.POST["password"],
            LastName = request.POST["LastName"],
            EmailAddress = request.POST["EmailAddress"],
            PermantAddress = request.POST["PermantAddress"],
            Age = request.POST["Age"],
            Salary = request.POST["Salary"],
            Shift = request.POST["Shift"],
            BloodGroup = request.POST["BloodGroup"],
            contact = request.POST["contact"],
            Ward = Ward.objects.filter(WardType = request.POST["Ward"]).first()
        )
        staff.save()
        return HttpResponseRedirect('/administration/adminhome/') 
    else:
        return render(request,'administration/REGISTER_WARD_CLERK.html')