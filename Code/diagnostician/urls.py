from . import views
from django.urls import path
urlpatterns = [
    path('diagnosisinfo/', views.diagnosisinfo),
    path('show_pdf/', views.show_pdf,name='dr'),
    path('show_pdf/<int:id>/',views.show_pdf),
]

