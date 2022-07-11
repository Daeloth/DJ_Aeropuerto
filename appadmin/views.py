from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'appadmin/index.html')

def registrochofer(request):
    return render(request, 'appadmin/registrochofer.html')