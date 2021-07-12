from django.urls import path
from. views import factura, boleta

urlpatterns = [
    path('', boleta, name= "boleta"),
    path('factura/', factura, name="factura"),
]