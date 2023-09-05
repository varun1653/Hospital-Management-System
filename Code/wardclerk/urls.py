from . import views
from django.urls import path
urlpatterns = [
    path('wardinfo/', views.wardinfo),
    path('show_pdf/', views.show_pdf,name='wb'),
    path('show_pdf/<int:id>/',views.show_pdf),
]

