from django.shortcuts import render,HttpResponse
from classes.models import Classes
from professional.models import Stage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.


@csrf_exempt
def getstage(request):
    if request.is_ajax():
        p=request.POST.get('p',None)
        res=Stage.objects.filter(p_id=p).values_list('id','name')
        obj={}
        for i in res:
            obj[i[0]]=i[1]
        return JsonResponse(obj)
    return HttpResponse('OK')