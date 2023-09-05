import datetime
from pydoc import Doc
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
def allappointments(request):
    if request.method == 'POST':
        if 'viewdetails' in request.POST:
            request.session['allapptoviewdetails']=request.POST['viewdetails']
            return HttpResponseRedirect('/doctor/viewdetails')
    elif request.session.has_key('DoctorID'):
        d = Doctor.objects.get(DoctorID=request.session['DoctorID'])
        appointments = DoctorPatientAssignment.objects.all().filter(Doctor = d )    
        return render(request,'doctor/allappointments.html',{'appointments':appointments})
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
        return render(request,'doctor/appointmentdetails.html',{'appointmentVisists': details,'appointment':appointment,'look':look,'book':book })
    else:
        error="Sorry there was a problem from our side try again later"
        return HttpResponseRedirect('/doctor/allappointments',{'error':error})
