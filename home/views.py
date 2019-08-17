from django.shortcuts import render,HttpResponse
from classes.models import Classes
from professional.models import Stage,Professional

# Create your views here.
# 公共阶段
pub_id1 = Professional.objects.filter(name='督导')[0].id
pub_id2 = Professional.objects.filter(name='就业')[0].id
pub_stage1 = Stage.objects.filter(p_id=pub_id1)
pub_stage2 = Stage.objects.filter(p_id=pub_id2)
pub_stage=pub_stage1|pub_stage2





def home(request):
    classes=Classes.objects.all()
    if request.method=='GET':
        return render(request, 'home/index.html',{'classes':classes})
    else:
        cla_name=request.POST.get('cla_name',None)
        classes=classes.filter(name=cla_name)
        pid=classes[0].p_id
        stage=Stage.objects.filter(p_id=pid)
        stages=stage|pub_stage
        hours=classes.first().now_stage.hours
        print(classes.first().now_stage.hours)
        res={'classes':classes,'begin':True,'stages':stages,'hours':hours}

        return render(request, 'home/index.html',res)
