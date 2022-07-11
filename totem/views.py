from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'totem/index.html')

def ingreso(request):
    return render(request, 'totem/ingreso.html')

def registro(request):
    return render(request, 'totem/registro.html')

def transfer(request):
    return render(request, 'totem/transfer.html')

def pago(request):
    return render(request, 'totem/pago.html')

def pagof(request):
    return render(request, 'totem/pagof.html')