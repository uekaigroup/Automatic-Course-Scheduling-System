from django.shortcuts import render,HttpResponse,redirect,reverse
from professional.models import Professional

# Create your views here.
def index(request):
    val=Professional.objects.filter(name='UI')[0]
    print(val)
    return render(request,'professional/addprofessional.html')

def addpro(request):
    name=request.POST.get('name',None)
    if name:
        Professional.objects.create(name=name)
        return HttpResponse('添加成功')
    else:
        return redirect(reverse('professional:index'))

