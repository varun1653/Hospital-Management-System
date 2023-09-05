from django.http import HttpResponseRedirect,FileResponse
from django.shortcuts import render
from receptionist.models import DoctorPatientAssignment
from pharmacy_technician.models import PharmacyBill,PharmacyTechnician
from billing_desk.models import HospitalBills
# Create your views here.
import os
from django.core.files.storage import FileSystemStorage
def show_pdf(request,id):
    k ='fb'+str(id)
    filepath = os.path.join('uploads',k )
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def pharmacyinfo(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            app = DoctorPatientAssignment.objects.filter(id = request.POST['id'])
            pharm = PharmacyBill.objects.filter(Appointment = appointment).first()
            pt = PharmacyTechnician.objects.filter(PharmacyTechnicianID = request.session['PharmacyTechnicianID']).first()
            if 'pbfile' in request.FILES and request.FILES['pbfile']:
                pharm.bill = True
                pharm.PharmacyTechnician = pt
                pharm.save()
                uploaded_file = request.FILES['dbfile']
                fs = FileSystemStorage()
                if fs.exists("pb"+str(app.id)):
                    fs.delete("pb"+str(app.id))
                fs.save("dr"+str(app.id),uploaded_file)
            if 'totalbill' in request.POST and request.POST['totalbill'] :
                hb = HospitalBills.objects.filter(Appointment = app).first()
                hb.TotalBill = hb.TotalBill - pharm.totalbill
                hb.save()
                pharm.totalbill = request.POST['totalbill']
                pharm.PharmacyTechnician = pt
                pharm.save()
                hb.TotalBill = hb.TotalBill + pharm.totalbill
                hb.save()
        else:
            App_Id = request.POST['pp_id']
            visit = request.POST['visit']
            appointment = DoctorPatientAssignment.objects.filter(AppointmentID =App_Id,VisitNo = visit).first()
            pharm = PharmacyBill.objects.filter(Appointment = appointment).first()
            return render(request,'pharmacy_technician/pharmacyinfo.html',{'appointment':appointment,'pharm':pharm,'makeitlook':True})
    else:
        if 'PharmacyTechnicianID'in request.session:
            return render(request,'pharmacy_technician/pharmacyinfo.html',{'makeitlook':False})
        else:
            return HttpResponseRedirect('/stafflogin')

