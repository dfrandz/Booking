from django import forms
from django.forms import Textarea, TextInput
from service_app.models import Vehicule


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields =('vehicule_marque','vehicule_model','vehicule_titre', 'nombre_passager', 'nombre_baguage','vehicuile_image', 'service')
        
    def __init__(self,*args,**kwargs):
        super(VehiculeForm, self).__init__(*args, **kwargs)
        self.fields['service'].empty_label="Select a service"
       