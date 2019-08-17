from django.shortcuts import render,HttpResponse
from classes.models import Classes
from professional.models import Stage


# Create your views here.

def index(request):
    classes=Classes.objects.name

    print(classes)
    return render(request,'classes/index.html')
