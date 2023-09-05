from . import views
from django.urls import path
urlpatterns = [
    path('patientinfo', views.patientinfo),
    path('login', views.login),
    path('logout', views.logout),
    path('', views.home),
    path('stafflogin', views.stafflogin),
    path('show_pdf/', views.show_pdf,name='mr'),
    path('show_pdf/<int:id>/',views.show_pdf),
    path('diagnosis_pdf/', views.diagnosis_pdf,name='dr'),
    path('diagnosis_pdf/<int:id>/',views.diagnosis_pdf),
    path('wb_pdf/', views.wb_pdf,name='wb'),
    path('wb_pdf/<int:id>/',views.wb_pdf),
    path('db_pdf/', views.db_pdf,name='db'),
    path('db_pdf/<int:id>/',views.db_pdf),
    path('pb_pdf/', views.pb_pdf,name='pb'),
    path('pb_pdf/<int:id>/',views.pb_pdf),
]
