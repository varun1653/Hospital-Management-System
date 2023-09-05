import datetime
import imp
from django.http import HttpResponseRedirect,FileResponse
from pharmacy_technician.models import PharmacyBill
from billing_desk.models import HospitalBills
from django.shortcuts import render
from diagnostician.models import Diagnosis
from receptionist.models import DoctorPatientAssignment
from wardclerk.models import WardDetails
from billing_desk.models import Biller
# Create your views here.
import os

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

def bills(request):
    if request.method == 'POST':
        request.session['billstoindivbills'] = request.POST["appid"]
        return HttpResponseRedirect('/billing_desk/indivbills/')
    if 'BillerID' in request.session :
        hb = HospitalBills.objects.all()
        return render(request,'billing_desk/bills.html',{'HospitalBills':hb})
    else:
        return HttpResponseRedirect('/stafflogin')
def indivbills(request):
    if request.method == 'POST':
        if 'ok' in request.POST:
            payed = int(request.POST["amount_paid"])
            appid = request.session['billstoindivbills']
            app = DoctorPatientAssignment.objects.filter(id = appid).first()
            hb = HospitalBills.objects.filter(Appointment = app).first()
            hb.AmountPaid = hb.AmountPaid + payed
            hb.Biller = Biller.objects.filter(BillerID=request.session['BillerID']).first()
            if hb.AmountPaid == hb.TotalBill :
                hb.FullyPaidDate = datetime.datetime.now()
            hb.save()
        return HttpResponseRedirect('/billing_desk/indivbills/')
    elif 'billstoindivbills' in request.session and 'BillerID' in request.session:
        appid = request.session['billstoindivbills']
        app = DoctorPatientAssignment.objects.filter(id = appid).first()
        hb = HospitalBills.objects.filter(Appointment = app).first()
        diagnosisbill = Diagnosis.objects.filter(Appointment = app).first()
        wardbill = WardDetails.objects.filter(Appointment = app).first()
        pharmacybill = PharmacyBill.objects.filter(Appointment = app).first()
        return render(request,'billing_desk/individualbills.html',{'app':app ,'diagnosisbill':diagnosisbill,'wardbill':wardbill,'pharmacybill':pharmacybill,'hb':hb})
    else:
        return HttpResponseRedirect('/billing_desk/bills/',{'error':"Sorry your request was not registered try again"})
    
