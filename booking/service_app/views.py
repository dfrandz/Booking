from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import ServiceForm
from django import forms
from .models import Service

# Create your views here.


def service_form(request, id=0):
    if request.method == 'POST':
        form=ServiceForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            #img_obj = ServiceForm.instance
        return render(request,'service_list.html')
    else:
        if id==0:
            form=ServiceForm()
        else:
            service= Service.objects.get(pk=id)
            form= ServiceForm(instance=service)
    return render(request, 'service_form.html',{'form': form})
    #return render(request, 'service_form.html',{'form': form})


def service_dona(request, id=0):
    if request.method == 'GET':
        if id==0:
            form=ServiceForm()
        else:
            service= Service.objects.get(pk=id)
            form= ServiceForm(instance=service)
        return render(request, 'service_form.html',{'form': form})
    else:
        if id==0:   
            form=ServiceForm(request.POST, request.FILES)
        else:
            service= Service.objects.get(pk=id)
            form= ServiceForm(request.POST, request.FILES, instance=service)
            
        if(form.is_valid()):
            form.save()
        return render(request,'service_list.html')
       
            
def service_list(request):
    services = Service.objects.all()
    context = {
        'list_service' : services
    }
    return render(request, 'service_list.html', context)


def service_store(request, id=0):
    if request.method == 'POST':
        if id==0:
            form = ServiceForm(request.POST, request.FILES)
        else:
            service = Service.objects.get(pk=id)
            form = ServiceForm(request.POST, request.FILES, instance=service)
        #form=ServiceForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            img_obj = ServiceForm.instance
        return render(request, 'service_list.html',{'form': form, 'img_obj': img_obj})
    else:
        form=ServiceForm()
    return render(request, 'service_list.html',{'form': form})



def service_update(request):
    return

def service_delete(request, id):
    service = Service.objects.get(pk=id)
    service.delete()
    return render(request, 'service_list.html')

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
