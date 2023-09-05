"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('patient.urls')),
    path('receptionist/',include('receptionist.urls')),
    path('medical_assistant/',include('medical_assistant.urls')),
    path('doctor/',include('doctor.urls')),
    path('billing_desk/',include('billing_desk.urls')),
    path('administration/',include('administration.urls')),
    path('wardclerk/',include('wardclerk.urls')),
    path('diagnostician/',include('diagnostician.urls')),
    path('pharmacy_technician/',include('pharmacy_technician.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)