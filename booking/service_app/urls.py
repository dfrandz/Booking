
from django.urls import path, include
from . import views

urlpatterns = [
    path('form/',views.service_dona, name='service_form'),
    path('<int:id>/', views.service_dona, name='service_update'),
    path('list/', views.service_list, name='service_list'),
    path('store/', views.service_store, name='service_store'),
    path('delete/<int:id>/',views.service_delete, name='service_delete')

]
