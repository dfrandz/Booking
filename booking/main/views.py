from django.shortcuts import render
from service_app.models import Service
from service_app.models import Vehicule
# Create your views here.

def Index(request):
    service = Service.objects.all().count
    vehicule = Vehicule.objects.all().count
    context = {
        'serviceNombre' : service,
        'vehiculeNombre' : vehicule
    }
    return render(request,'dashboard.html', context)