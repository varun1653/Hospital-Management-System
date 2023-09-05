
from venv import create
from django.http import HttpResponseRedirect,FileResponse
from django.shortcuts import render
from patient.models import Patient
from medical_assistant.models import MedicalAssistant,MedicalReport
from receptionist.models import DoctorPatientAssignment
from administration.models import Administrator
from billing_desk.models import Biller,HospitalBills
from doctor.models import Doctor
from diagnostician.models import Diagnostician,Diagnosis
from pharmacy_technician.models import PharmacyTechnician,PharmacyBill
from receptionist.models import Receptionist
from wardclerk.models import WardClerk,WardDetails
# Create your views here.

def login(request):
    if request.method == 'POST':
        patientID = request.POST['patientID']
        password = request.POST['password']
        if Patient.objects.filter(PatientID=patientID,password=password).count()!=0 :
            pat = Patient.objects.filter(PatientID=patientID,password=password).first()
            request.session['patientID'] = pat.PatientID
            return HttpResponseRedirect('/')
        else:
            return render(request,'patient/login.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' })

    return render(request,'patient/login.html')
def logout(request):
    if 'patientID' in request.session :
        del request.session['patientID']
    if 'MedicalAssistantID' in request.session :
        del request.session['MedicalAssistantID']
    if 'AdministratorID' in request.session :
        del request.session['AdministratorID']
    if 'BillerID' in request.session :
        del request.session['BillerID']
    if 'DiagnosticianID' in request.session :
        del request.session['DiagnosticianID']
    if 'DoctorID' in request.session :
        del request.session['DoctorID']
    if 'PharmacyTechnicianID' in request.session :
        del request.session['PharmacyTechnicianID']
    if 'ReceptionistID' in request.session :
        del request.session['ReceptionistID']
    if 'WardClerkID' in request.session :
        del request.session['WardClerkID']
    return HttpResponseRedirect('/')
def stafflogin(request):
    if request.method == 'POST':
        ids = request.POST['id']
        password = request.POST['password']
        if request.POST['stafftype'] == 'MedicalAssistant' :
            if MedicalAssistant.objects.filter(MedicalAssistantID=ids,password=password).count()!=0 :
                request.session['MedicalAssistantID'] = ids
            else:
                return render(request,'patient/stafflogin.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' })
        elif request.POST['stafftype'] == 'Admin' :
            if Administrator.objects.filter(AdministratorID=ids,password=password).count()!=0 :
                request.session['AdministratorID'] = ids
            else:
                return render(request,'patient/stafflogin.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' })
        elif request.POST['stafftype'] == 'Biller' :
            if Biller.objects.filter(BillerID=ids,password=password).count()!=0 :
                request.session['BillerID'] = ids     
            else:
                return render(request,'patient/stafflogin.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' }) 
        elif request.POST['stafftype'] == 'Diagnostician' :
            if Diagnostician.objects.filter(DiagnosticianID=ids,password=password).count()!=0 :
                request.session['DiagnosticianID'] = ids 
            else:
                return render(request,'patient/stafflogin.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' })
        elif request.POST['stafftype'] == 'Doctor' :
            if Doctor.objects.filter(DoctorID=ids,password=password).count()!=0 :
                request.session['DoctorID'] = ids  
            else:
                return render(request,'patient/stafflogin.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' })
        elif request.POST['stafftype'] == 'Pharmacist' :
            if PharmacyTechnician.objects.filter(PharmacyTechnicianID=ids,password=password).count()!=0 :
                request.session['PharmacyTechnicianID'] = ids  
            else:
                return render(request,'patient/stafflogin.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' })
        elif request.POST['stafftype'] == 'Receptionist' :
            if Receptionist.objects.filter(ReceptionistID=ids,password=password).count()!=0 :
                request.session['ReceptionistID'] = ids  
            else:
                return render(request,'patient/stafflogin.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' })
        elif request.POST['stafftype'] == 'WardAssistant' :
            if WardClerk.objects.filter(WardClerkID=ids,password=password).count()!=0 :
                request.session['WardClerkID'] = ids 
            else:
                return render(request,'patient/stafflogin.html',{'error': 'Sorry your ID or Password are incorrect Try again!!' })
        return HttpResponseRedirect('/')
    return render(request,'patient/stafflogin.html')
def patientinfo(request):
    if 'patientID' in request.session:
        patient = Patient.objects.filter(PatientID = request.session['patientID']).first()
        appointmentVisists = DoctorPatientAssignment.objects.filter(Patient=patient)
        appointmentVisists = appointmentVisists.reverse()
        mr=[]
        for visit in appointmentVisists :
            checker = MedicalReport.objects.filter(Appointment = visit).first()
            if checker and checker.report == True :
                mr.append(visit.id)
        dr = []
        for visit in appointmentVisists :
            checker = Diagnosis.objects.filter(Appointment = visit).first()
            if checker and checker.labreport == True :
                dr.append(visit.id)
        pb = []
        for visit in appointmentVisists :
            checker = PharmacyBill.objects.filter(Appointment = visit).first()
            if checker and checker.bill == True :
                pb.append(visit.id)
        db = []
        for visit in appointmentVisists :
            checker = Diagnosis.objects.filter(Appointment = visit).first()
            if checker and checker.bill == True :
                db.append(visit.id)
        wb = []
        for visit in appointmentVisists :
            checker = WardDetails.objects.filter(Appointment = visit).first()
            if checker and checker.wardbill == True :
                wb.append(visit.id)
        tb = HospitalBills.objects.all()
        return render(request,'patient/patient_info.html',{'Patient': patient,'appointmentVisists':appointmentVisists,'mr':mr,'dr':dr,'pb':pb,'db':db,'wb':wb,'tb':tb})
    else:
        return HttpResponseRedirect('/login')
def home(request):
    return render(request,'patient/home.html',)
import os
def show_pdf(request,id):
    k ='mr'+str(id)
    filepath = os.path.join('uploads',k )
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
def diagnosis_pdf(request,id):
    k ='dr'+str(id)
    filepath = os.path.join('uploads',k)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def wb_pdf(request,id):
    k ='wb'+str(id)
    filepath = os.path.join('uploads',k )
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
def db_pdf(request,id):
    k ='db'+str(id)
    filepath = os.path.join('uploads',k )
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def pb_pdf(request,id):
    k ='pb'+str(id)
    filepath = os.path.join('uploads',k )
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

