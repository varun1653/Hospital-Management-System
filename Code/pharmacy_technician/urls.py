from . import views
from django.urls import path
urlpatterns = [
    path('pharmacyinfo/', views.pharmacyinfo),
    path('show_pdf/', views.show_pdf,name='pb'),
    path('show_pdf/<int:id>/',views.show_pdf),
]

