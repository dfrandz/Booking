from django.shortcuts import render,redirect
from .forms import VehiculeForm
from service_app.models import Vehicule
# Create your views here.

def Car_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form=VehiculeForm()
        else:
            vehicule= Vehicule.objects.get(pk=id)
            form= VehiculeForm(instance=vehicule)
        return render(request, 'car_form.html',{'form': form})
    else:
        if id==0:   
            form=VehiculeForm(request.POST, request.FILES)
        else:
            vehicule= Vehicule.objects.get(pk=id)
            form= VehiculeForm(request.POST, request.FILES, instance=vehicule)
        if(form.is_valid()):
            form.save()
    form=VehiculeForm()
    return render(request,'car_form.html',{'form': form})



def car_list(request):
    vehicule = Vehicule.objects.all()
    context = {
        'vehicules' : vehicule
    }
    return render(request, 'car_list.html', context)

def car_delete(request, id):
    vehicule = Vehicule.objects.get(pk=id)
    vehicule.delete()
    return render(request, 'car_list.html')