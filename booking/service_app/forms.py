from django import forms
from .models import Service
from django.forms import Textarea, TextInput
 
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields =('service_name', 'service_desc', 'service_image')
        labels={
            'service_image':'serrvice file',
            'service_desc':'description',
            'service_name':'service name',
        }
        widgets={
            'service_name': TextInput(attrs={'class':'form-control'}) ,
            
        }