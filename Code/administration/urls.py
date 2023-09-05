from . import views
from django.urls import path
urlpatterns = [
    path('adminhome/', views.adminhome),
    path('addbiller/', views.addbiller),
    path('addWardClerk/', views.addWardClerk),
    path('addDoctor/', views.addDoctor),
    path('addMedicalAssistant/', views.addMedicalAssistant),
    path('addDiagnostician/', views.addDiagnostician),
    path('addReceptionist/', views.addReceptionist),
    path('addPharmacyTechnician/', views.addPharmacyTechnician),
]

