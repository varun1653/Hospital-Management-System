import datetime
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render
from billing_desk.models import HospitalBills
from receptionist.models import DoctorPatientAssignment
from wardclerk.models import WardDetails,Ward,WardClerk
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
def show_pdf(request,id):
    k ='wb'+str(id)
    filepath = os.path.join('uploads',k )
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def wardinfo(request):
    if request.method == 'POST':
        if 'yes' in request.POST and  request.POST['yes'] !='yes' :
            appid = request.POST['yes']
            app = DoctorPatientAssignment.objects.filter(id = appid).first()
            wardd = WardDetails.objects.filter(Appointment = app).first()
            wardd.LeftDate = datetime.datetime.now()
            wardd.save()
        if 'files' in request.FILES and request.FILES['files']:
            app = DoctorPatientAssignment.objects.filter(id = request.POST["id"]).first()
            wrd = WardDetails.objects.filter(Appointment = app).first()
            wrd.wardbill = True
            wrd.save()
            uploaded_file = request.FILES['files']
            fs = FileSystemStorage()
            if fs.exists("wb"+str(app.id)):
                fs.delete("wb"+str(app.id))
            fs.save("wb"+str(app.id),uploaded_file)
        if 'totalbill' in request.POST and request.POST['totalbill'] :
            app = DoctorPatientAssignment.objects.filter(id = request.POST["id"]).first()
            wrd = WardDetails.objects.filter(Appointment = app).first()
            hb = HospitalBills.objects.filter(Appointment = app).first()
            hb.TotalBill = hb.TotalBill - wrd.totalbill
            hb.save()
            wrd.totalbill = request.POST['totalbill']
            wrd.save()
            hb.TotalBill = hb.TotalBill + wrd.totalbill
            hb.save()
        return HttpResponseRedirect('/wardclerk/wardinfo')
    elif 'WardClerkID' in request.session:
        wc = WardClerk.objects.filter(WardClerkID = request.session['WardClerkID']).first()
        hisward = Ward.objects.filter(WardType = wc.Ward.WardType).first()
        warddetails = WardDetails.objects.filter(Ward = wc.Ward)
        return render(request,'wardclerk/wardinfo.html',{'wc':wc,'hisward':hisward,'WardDetails':warddetails})
    else:
        return HttpResponseRedirect('/stafflogin')