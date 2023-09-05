from django.http import HttpResponseRedirect,FileResponse
from django.shortcuts import render
from diagnostician.models import Diagnosis,Diagnostician
from receptionist.models import DoctorPatientAssignment
from billing_desk.models import HospitalBills
import os
from django.core.files.storage import FileSystemStorage
def diagnosisinfo(request):
    if request.method == 'POST':
        if 'drfile' in request.FILES and request.FILES['drfile']:
            app = DoctorPatientAssignment.objects.filter(id = request.POST["id"]).first()
            diag = Diagnosis.objects.filter(Appointment = app).first()
            d = Diagnostician.objects.filter(DiagnosticianID = request.session['DiagnosticianID']).first()
            diag.labreport = True
            diag.Diagnostician = d
            diag.save()
            uploaded_file = request.FILES['drfile']
            fs = FileSystemStorage()
            if fs.exists("dr"+str(app.id)):
                fs.delete("dr"+str(app.id))
            fs.save("dr"+str(app.id),uploaded_file)
        if 'dbfile' in request.FILES and request.FILES['dbfile']:
            app = DoctorPatientAssignment.objects.filter(id = request.POST["id"]).first()
            diag = Diagnosis.objects.filter(Appointment = app).first()
            diag.bill = True
            d = Diagnostician.objects.filter(DiagnosticianID = request.session['DiagnosticianID']).first()
            diag.Diagnostician = d
            diag.save()
            uploaded_file = request.FILES['dbfile']
            fs = FileSystemStorage()
            if fs.exists("db"+str(app.id)):
                fs.delete("db"+str(app.id))
            fs.save("dr"+str(app.id),uploaded_file)
        if 'totalbill' in request.POST and request.POST['totalbill'] :
            app = DoctorPatientAssignment.objects.filter(id = request.POST["id"]).first()
            dg = Diagnosis.objects.filter(Appointment = app).first()
            hb = HospitalBills.objects.filter(Appointment = app).first()
            hb.TotalBill = hb.TotalBill - dg.totalbill
            hb.save()
            dg.totalbill = request.POST['totalbill']
            d = Diagnostician.objects.filter(DiagnosticianID = request.session['DiagnosticianID']).first()
            diag.Diagnostician = d
            dg.save()
            hb.TotalBill = hb.TotalBill + dg.totalbill
            hb.save()
        return HttpResponseRedirect('/diagnostician/diagnosisinfo')
    elif 'DiagnosticianID' in request.session :
        diagnosis = Diagnosis.objects.all()
        return render(request,'diagnostician/diagnosisinfo.html',{'Diagnosis':diagnosis})
    else:
        return HttpResponseRedirect('/stafflogin')

def show_pdf(request,id):
    k ='dr'+str(id)
    filepath = os.path.join('uploads',k )
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
