from django.shortcuts import render,HttpResponse


# Create your views here.

def index(request):
    print(123)
    return render(request,'home/index.html')
