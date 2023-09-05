from . import views
from django.urls import path
urlpatterns = [
    path('allappointments/',views.allappointments),
    path('viewdetails/',views.viewdetails),
    path('show_pdf/', views.show_pdf,name='mr'),
    path('show_pdf/<int:id>/',views.show_pdf),
    path('diagnosis_pdf/', views.diagnosis_pdf,name='dr'),
    path('diagnosis_pdf/<int:id>/',views.diagnosis_pdf),
]
