from django.urls import path, include
from . import views

urlpatterns = [
    path('form/', views.Car_form, name="car_form"),
    path('<int:id>/', views.Car_form, name='car_update'),
    path('list/', views.car_list, name="car_list"),
    path('delete/<int:id>/',views.car_delete, name='car_delete')
]