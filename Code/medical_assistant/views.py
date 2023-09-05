import datetime
from urllib import response 
from django.http import HttpResponseRedirect
from django.db.models import F
from django.shortcuts import render
from medical_assistant.models import MedicalAssistant,MedicalReport
from receptionist.models import DoctorPatientAssignment
from doctor.models import Doctor
from wardclerk.models import WardDetails,Ward
from diagnostician.models import Diagnosis
from billing_desk.models import HospitalBills
from pharmacy_technician.models import PharmacyBill
from django.core.files.storage import FileSystemStorage

import os.path
# Create your views here.

from django.http import FileResponse
import os
 
def show_pdf(request,id):
    k ='mr'+str(id)
    filepath = os.path.join('uploads',k )
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
def diagnosis_pdf(request,id):
    k ='dr'+str(id)
    filepath = os.path.join('uploads',k)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def logout(request):
    del request.session['medical_assistant']
    return HttpResponseRedirect('/stafflogin')

def allappointments(request):
    if request.method == 'POST':
        if 'viewdetails' in request.POST:
            request.session['allapptoviewdetails']=request.POST['viewdetails']
            return HttpResponseRedirect('/medical_assistant/viewdetails')
        elif 'edit' in request.POST:
            request.session['allapptoedit']=request.POST['edit']
            return HttpResponseRedirect('/medical_assistant/edit')
    if request.session.has_key('MedicalAssistantID'):
        ma = MedicalAssistant.objects.get(MedicalAssistantID=request.session['MedicalAssistantID'])
        appointments = DoctorPatientAssignment.objects.all().filter(Doctor = ma.underDoctor )    
        return render(request,'medical_assistant/allappointments.html',{'appointments':appointments})
    else:
        return HttpResponseRedirect('/stafflogin')
def viewdetails(request):
    if 'allapptoviewdetails' in request.session :
        details=list(DoctorPatientAssignment.objects.filter(AppointmentID=request.session['allapptoviewdetails']))
        appointment=DoctorPatientAssignment.objects.filter(AppointmentID=request.session['allapptoviewdetails']).first()
        look=[]
        book = []
        for visit in details :
            if Diagnosis.objects.filter(Appointment = visit).count()!=0 :
                if Diagnosis.objects.get(Appointment = visit).labreport == True :
                    book.append(visit.id)
        for visit in details :
            if MedicalReport.objects.filter(Appointment = visit).count()!=0:
                if MedicalReport.objects.get(Appointment = visit).report == True :
                    look.append(visit.id)
        return render(request,'medical_assistant/appointmentdetails.html',{'appointmentVisists': details,'appointment':appointment,'look':look,'book':book })
    else:
        error="Sorry there was a problem from our side try again later"
        return HttpResponseRedirect('/medical_assistant/allappointments',{'error':error})

def turnsave(appid):
    apt = DoctorPatientAssignment.objects.filter(id = appid).first()
    apt.status='Open'
    apt.save()
    hb = HospitalBills.objects.create(
        Appointment = apt,
        TotalBill = 100,
        AmountPaid = 0,
        BillID = HospitalBills.objects.count()+1
    )
    hb.save()
    pharmacy_bill = PharmacyBill.objects.create(
        Appointment = apt,
        PharmacyBillID = PharmacyBill.objects.count()+1,
        bill = False,
        totalbill = 0,
    )
    pharmacy_bill.save()
def edit(request):
    appid = DoctorPatientAssignment.objects.filter(id=request.session['allapptoedit']).first()
    warddetails=WardDetails.objects.filter(Appointment=appid).first()
    ward = Ward.objects.filter(WardCapacity__gt = F('Population'))
    labreport = Diagnosis.objects.filter(Appointment=appid).first()
    medicalreport = MedicalReport.objects.filter(Appointment=appid).first()
    if request.method == "POST":
        if 'files' in request.FILES and request.FILES['files']:
            if medicalreport :
                uploaded_file = request.FILES['files']
                fs = FileSystemStorage()
                if fs.exists("mr"+str(appid.id)):
                    fs.delete("mr"+str(appid.id))
                fs.save("mr"+str(appid.id),uploaded_file)
            else:
                if appid.status == 'Unattended':
                    turnsave(appid.id)
                mr=MedicalReport.objects.create(
                    ReportID = int(MedicalReport.objects.all().count())+1,
                    report = True,
                    Appointment = appid,
                    MedicalAssistant = MedicalAssistant.objects.get(MedicalAssistantID=request.session['MedicalAssistantID'])
                )
                mr.save()
                uploaded_file = request.FILES['files']
                fs = FileSystemStorage()
                fs.save("mr"+str(appid.id),uploaded_file)
        if 'wardtype' in request.POST and request.POST['wardtype']!=None and request.POST['wardtype']!='' :
            if appid.status == 'Unattended':
                turnsave(appid.id)
            wrd=Ward.objects.all().get(WardType = request.POST['wardtype'])
            i=1
            allw = WardDetails.objects.filter(Ward = wrd)
            assignno = 0
            while i <= wrd.WardCapacity:
                exist = False
                for j in allw:
                    if j.BedNo == i:
                        i+=1
                        exist=True
                        break
                if exist ==False :
                    assignno = i
                    break
            curward = Ward.objects.get(WardType = request.POST['wardtype'] )
            curward.Population = curward.Population+1
            curward.save()
            dt = datetime.datetime.now()
            details=WardDetails.objects.create(
                Ward = curward,
                BedNo= assignno,
                Appointment = appid,
                Description = request.POST['wardreportDescription'],
                JoinedDate= dt,
                LeftDate= dt,
            )
            details.save()
        if 'diagnosis' in request.POST and request.POST['diagnosis'] == 'Yes' :
            if appid.status == 'Unattended':
                turnsave(appid.id)
            diag = Diagnosis.objects.create(
                DiagnosticReportID = int(Diagnosis.objects.all().count())+1,
                description = request.POST['labreportDescription'],
                Appointment = appid
            )
            diag.save()
        if 'appointment_status' in request.POST and request.POST['appointment_status']!='':
            if appid.status == 'Unattended':
                turnsave(appid.id)
            appid.status=request.POST['appointment_status']
            appid.save()
        return HttpResponseRedirect('/medical_assistant/edit')
    else:
        if request.session.has_key('allapptoedit'):
            return render(request,'medical_assistant/editreport.html',{'appointment':appid,'medicalreport':medicalreport,'warddetails':warddetails,'ward':ward,'labreport':labreport})
        else:
            error="Sorry there was a problem from our side try again later"
            return HttpResponseRedirect('/medical_assistant/allappointments',{'error':error})
