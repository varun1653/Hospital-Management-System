from tkinter import Widget
from django.forms import ClearableFileInput, ModelForm
from .models import MedicalReport

class MedicalReportForm(ModelForm):
    class Meta: 
        model = MedicalReport
        fields = '__all__'
        widgets = {
            'report' : ClearableFileInput(attrs={'multiple':True})
        }   