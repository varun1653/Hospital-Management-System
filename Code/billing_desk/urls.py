from . import views
from django.urls import path
urlpatterns = [
    path('bills/',views.bills),
    path('indivbills/',views.indivbills),
    path('wb_pdf/', views.wb_pdf,name='wb'),
    path('wb_pdf/<int:id>/',views.wb_pdf),
    path('db_pdf/', views.db_pdf,name='db'),
    path('db_pdf/<int:id>/',views.db_pdf),
    path('pb_pdf/', views.pb_pdf,name='pb'),
    path('pb_pdf/<int:id>/',views.pb_pdf),
]
