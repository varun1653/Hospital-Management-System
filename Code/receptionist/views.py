import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from patient.models import Patient
from receptionist.models import DoctorPatientAssignment, Receptionist
from wardclerk.models import Ward,WardDetails
from doctor.models import Doctor
from billing_desk.models import HospitalBills
from pharmacy_technician.models import PharmacyBill
# # Create your views here.
def allPatientDetails(request):
    if request.method == 'POST':
        if 'patientId' in request.POST and request.POST['patientId']!='':
            patientId = request.POST['patientId']
        else:
            patientId = 0
        if 'patientName' in request.POST and request.POST['patientName']!='':
            patientName = request.POST['patientName']
        else:
            patientName = None
        if patientId!=0:
            specificPatientDetails ={'patients':list(Patient.objects.filter(PatientID=patientId))}
            return render(request,'receptionist/allPatients.html',specificPatientDetails)
        elif patientName!=None :
            specificPatientDetails ={'patients':list(Patient.objects.filter(FirstName=patientName))}
            return render(request,'receptionist/allPatients.html',specificPatientDetails)
        else:
            allPatientDetails={'patients':list(Patient.objects.all())}
            return render(request,'receptionist/allPatients.html',allPatientDetails)
    else:
        if 'ReceptionistID' in request.session :
            allPatientDetails={'patients':list(Patient.objects.all())}
            return render(request,'receptionist/allPatients.html',allPatientDetails)
        else:
            return HttpResponseRedirect('/stafflogin')


def wardDoctorDetails(request):
    if 'ReceptionistID' in request.session :
        Details={'Ward':list(Ward.objects.all()),
                'WardDetails':list(WardDetails.objects.all()),
                'DoctorDetails':list(Doctor.objects.all())}
        return render(request,'receptionist/wardDoctorDetails.html',Details)
    else:
        return HttpResponseRedirect('/stafflogin')

def registration(request):
    if request.method=='POST':
        p=Patient.objects.create(
            PatientID = len(Patient.objects.all())+1,
            FirstName = request.POST['fname'],
            LastName = request.POST['lname'],
            contact = request.POST['Contact'],
            gender = request.POST['gender'],
            Age = request.POST['Age'],
            Height = request.POST['Height'],
            Weight = request.POST['Weight'],
            BloodGroup = request.POST['Blood_group'],
            EmailAddress = request.POST['Email'],
            PermantAddress = request.POST['Address-line1']+","+request.POST['Address-line2']+","+request.POST['city']+","+request.POST['state']+","+request.POST['postal'],
            password = request.POST['password']
        )
        p.save()
        return HttpResponseRedirect('/receptionist/allPatients/') 
    elif 'ReceptionistID' in request.session :
        return render(request,'receptionist/registration.html')
    else:
        return HttpResponseRedirect('/stafflogin')
def appointment(request):
    appointment=list(DoctorPatientAssignment.objects.only('AppointmentID','Doctor','Patient','datetime','status'))
    if request.method=='POST':
        neworold = request.POST['neworold']
        appointmentID = 0
        if neworold == "new" :
            appointmentID = int(DoctorPatientAssignment.objects.all().count())+1
        else:
            appointmentID = request.POST['appointmentID']
            if(DoctorPatientAssignment.objects.filter(AppointmentID=appointmentID).count()==0):
                return render(request,'receptionist/appointment.html',{'appointment':appointment,'error':"Appointment with that id does not exists"})

        patientID = request.POST['patientID']
        if(Patient.objects.filter(PatientID=patientID).count()==0):
            return render(request,'receptionist/appointment.html',{'appointment':appointment,'error':"patient with that id does not exists"})

        doctorID = request.POST['doctorID']
        if(Doctor.objects.filter(DoctorID=doctorID).count()==0):
            return render(request,'receptionist/appointment.html',{'appointment':appointment,'error':"Doctor with that id does not exists"})    
        visitno = DoctorPatientAssignment.objects.filter(AppointmentID = appointmentID).count()+1
        dt = datetime.datetime.now()
        apt=DoctorPatientAssignment.objects.create(
            Doctor = Doctor.objects.get(DoctorID=doctorID),
            Patient = Patient.objects.get(PatientID=patientID),
            Receptionist = Receptionist.objects.get(ReceptionistID=request.session['receptionistID']),
            AppointmentID = appointmentID,
            VisitNo = visitno,
            datetime = dt
        )
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
        return HttpResponseRedirect('/receptionist/allPatients/')
    elif 'ReceptionistID' in request.session :
        return render(request,'receptionist/appointment.html',{'appointment':appointment}) 
    else:
        return HttpResponseRedirect('/stafflogin')

def patientDetails(request):
    if request.method== 'POST':
        if 'patientId' in request.POST and request.POST['patientId']!='':
            patientId = request.POST['patientId']
            PatientDetails={'appointments':list(DoctorPatientAssignment.objects.filter(Patient_id=patientId))}
            return render(request,'receptionist/patientDetails.html',PatientDetails)
        else:
            return HttpResponseRedirect('/receptionist/allPatients/')
    else:
        return HttpResponseRedirect('/receptionist/allPatients/')
