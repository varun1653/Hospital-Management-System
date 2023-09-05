from . import views
from django.urls import path
urlpatterns = [
    path('allPatients/', views.allPatientDetails),
    path('patientDetails/', views.patientDetails),
    path('wardDoctorDetails/',views.wardDoctorDetails),
    path('registration/',views.registration),
    path('appointement/',views.appointment),
]
