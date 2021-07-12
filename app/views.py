from django.shortcuts import render

# Create your views here.

def boleta(request):
    return render(request, 'app/boleta.html')

def factura(request):
    return render(request, 'app/factura.html')