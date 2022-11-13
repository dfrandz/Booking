from django.db import models

# Create your models here.


class Service(models.Model):
    service_name= models.CharField(max_length=100)
    service_image= models.ImageField(upload_to='imagesService/')
    service_desc= models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return self.service_name


class Vehicule(models.Model):
    vehicule_marque = models.CharField(max_length=100)
    vehicule_model = models.CharField(max_length=100)
    vehicule_titre = models.CharField(max_length=100)
    nombre_passager = models.CharField(max_length=10)
    nombre_baguage = models.CharField(max_length=10)
    vehicuile_image= models.ImageField(upload_to='imagesVehicule')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
