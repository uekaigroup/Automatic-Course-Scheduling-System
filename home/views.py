from django.shortcuts import render,HttpResponse
from classes.models import Classes
from professional.models import Stage,Professional,StageOrder
from orderclasses.order_classes import model
from teacher.models import Teachstage,Teacher
import numpy as np
import json
# Create your views here.



def home(request):
    classes=Classes.objects.all()
    if request.method=='GET':
        return render(request, 'home/index.html',{'classes':classes})
    

# 根据前置课程获取阶段优先级排序列表
def bToA(nowsatge):
    satges=StageOrder.objects.filter(beforstage=nowsatge)
    levelarr=[]
    for i in satges:
        levelarr.append(i.level)
    nparr=np.array(levelarr)
    sortarr=list(reversed(np.argsort(nparr)))
    return satges,sortarr

# 阶段代课老师优先排序下标
def teacherorder(ts):
    arr1=[]
    for i in ts:
        arr1.append(i.level)
    nparr=np.array(arr1)
    sortteacher=list(reversed(np.argsort(nparr)))
    return sortteacher

# 获取下周时间范围
import calendar
import datetime


def getNextday():
    today1 = datetime.date.today()
    today2 = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    m1 = calendar.MONDAY
    m2 = calendar.SUNDAY

    while today1.weekday() != m1:
        today1 += oneday
    while today2.weekday() != m2:
        today2 += oneday
    today2 += oneday
    while today2.weekday() != m2:
        today2 += oneday

    nextMonday = today1.strftime('%Y%m%d')
    nextSunday = today2.strftime('%Y%m%d')

    return nextMonday+'-'+nextSunday

def getN_N_day():
    today1 = datetime.date.today()
    today2 = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    m1 = calendar.MONDAY
    m2 = calendar.SUNDAY

    while today1.weekday() != m1:
        today1 += oneday
    today1 += oneday
    while today1.weekday() != m1:
        today1 += oneday


    while today2.weekday() != m2:
        today2 += oneday
    today2 += oneday
    while today2.weekday() != m2:
        today2 += oneday
    today2 += oneday
    while today2.weekday() != m2:
        today2 += oneday

    nextMonday = today1.strftime('%Y%m%d')
    nextSunday = today2.strftime('%Y%m%d')

    return nextMonday+'-'+nextSunday


def getN_N_N_day():
    today1 = datetime.date.today()
    today2 = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    m1 = calendar.MONDAY
    m2 = calendar.SUNDAY

    while today1.weekday() != m1:
        today1 += oneday
    today1 += oneday
    while today1.weekday() != m1:
        today1 += oneday
    today1 += oneday
    while today1.weekday() != m1:
        today1 += oneday

    while today2.weekday() != m2:
        today2 += oneday
    today2 += oneday
    while today2.weekday() != m2:
        today2 += oneday
    today2 += oneday
    while today2.weekday() != m2:
        today2 += oneday
    today2 += oneday
    while today2.weekday() != m2:
        today2 += oneday

    nextMonday = today1.strftime('%Y%m%d')
    nextSunday = today2.strftime('%Y%m%d')

    return nextMonday + '-' + nextSunday

def ordercla(request):
    classes=Classes.objects.all()
    teachstage=Teachstage.objects.all()
    teacher=Teacher.objects.all()
    order=[]
    for i in classes:
        order.append(model.predict([[i.isprofessional,i.education,i.stu_num]])[0][0])
    nd=np.array(order)
    order_index=list(reversed(np.argsort(nd)))   #获得班级优先级的排序下标
    class_sheet_list=[]
    used_teachers=None
    for i in order_index:        #对每一个班进行排课
        i=int(i)
        class_sheet = {}
        class_sheet['classname']=classes[i].name
        class_sheet['area']=classes[i].area
        # class_sheet['time']=getNextday()
        drection=classes[i].p_id
        now_stage=classes[i].now_stage
        long_time=Stage.objects.filter(name=now_stage.name).first().hours
        now_long_time=classes[i].long_time
        if classes[i].is_six:
            if long_time-now_long_time>=48:
                class_sheet['stage']=[now_stage.name]
                class_sheet['long_time'] = [48]
                classes[i].long_time += 48
                ts=teachstage.filter(stage=now_stage)
                sortteacher=teacherorder(ts)
                for i in sortteacher:
                    i=int(i)
                    teacherone=teacher.filter(name=ts[i].teacher.name)
                    if teacherone[0].teachtime==0:
                        class_sheet['teacher']=[teacherone[0].name]
                        teacherone.update(teachtime=1)
                        if used_teachers:
                            used_teachers = used_teachers | teacherone
                        else:
                            used_teachers = teacherone
                        break
                    else:
                        continue
            # elif 0<long_time-now_long_time<48:
            #     class_sheet['stage'] = [now_stage.name]
            #     class_sheet['long_time'] = [long_time-now_long_time]
            #     classes[i].long_time += long_time-now_long_time
            #     stages, sortarr = bToA(now_stage)
            else:
                stages, sortarr = bToA(now_stage)
                for i in sortarr:
                    i=int(i)
                    class_sheet['stage']=stages[i].afterstage
                    class_sheet['long_time'] = [48]
                    classes[i].long_time = 48
                    classes[i].now_stage = stages[i].afterstage
                    ts = teachstage.filter(stage=stages[i].afterstage)
                    sortteacher = teacherorder(ts)
                    for i in sortteacher:
                        i = int(i)
                        teacherone = teacher.filter(name=ts[i].teacher.name)
                        if teacherone[0].teachtime == 0:
                            class_sheet['teacher'] = [teacherone[0].name]
                            if used_teachers:
                                used_teachers = used_teachers | teacherone
                            else:
                                used_teachers = teacherone
                            teacherone.update(teachtime=1)
                            break
                        else:
                            continue
        else:
            if long_time-now_long_time>=40:
                class_sheet['stage']=[now_stage.name]
                class_sheet['long_time'] = [40]
                classes[i].long_time += 40
                ts=teachstage.filter(stage=now_stage)
                sortteacher=teacherorder(ts)
                for i in sortteacher:
                    i=int(i)
                    teacherone=teacher.filter(name=ts[i].teacher.name)
                    if teacherone[0].teachtime==0:
                        class_sheet['teacher']=[teacherone[0].name]
                        if used_teachers:
                            used_teachers = used_teachers | teacherone
                        else:
                            used_teachers = teacherone
                        teacherone.update(teachtime=1)
                        break
                    else:
                        continue
            # elif 0<long_time-now_long_time<48:
            #     class_sheet['stage'] = [now_stage.name]
            #     class_sheet['long_time'] = [long_time-now_long_time]
            #     classes[i].long_time += long_time-now_long_time
            #     stages, sortarr = bToA(now_stage)
            else:
                stages, sortarr = bToA(now_stage)
                for i in sortarr:
                    i=int(i)
                    class_sheet['stage']=stages[i].afterstage
                    class_sheet['long_time'] = [40]
                    classes[i].long_time = 40
                    classes[i].now_stage = stages[i].afterstage
                    ts = teachstage.filter(stage=stages[i].afterstage)
                    sortteacher = teacherorder(ts)
                    for i in sortteacher:
                        i = int(i)
                        teacherone = teacher.filter(name=ts[i].teacher.name)
                        if teacherone[0].teachtime == 0:
                            class_sheet['teacher'] = [teacherone[0].name]
                            if used_teachers:
                                used_teachers = used_teachers | teacherone
                            else:
                                used_teachers = teacherone
                            teacherone.update(teachtime=1)
                            break
                        else:
                            continue
        # 所有老师和已选中老师的差集,并选择助教
        # if classes[i].is_teacher2:
        # # print('teacher:',teacher)
        # # print('used_teachers:',used_teachers)
        #     teacher2=teacher.difference(used_teachers)
        # # print(teacher2)
        #     sortteacher2=[]
        #     for i in teacher2:
        #         sortteacher2.append(i.classesed)
        #     sortteacher2=np.argsort(np.array(sortteacher2))
        #     for i in sortteacher2:
        #         print(teacher2)
        #         class_sheet['teacher2']=[teacher2[i].name]
        #         teacher2[i].update(teachtime=1)



            


        classes[i].save()
        class_sheet_list.append(class_sheet)
    Teacher.objects.all().update(teachtime=0)
    print(class_sheet_list)



    return class_sheet_list


def getcourse(request,id):
    if request.method=='GET':
        id=int(id)
        course1={getNextday():ordercla(request)}
        course2={getN_N_day():ordercla(request)}
        course3={getN_N_N_day():ordercla(request)}
        if id==1:
            print(1)
            return HttpResponse(str(course1))
        elif id==2:
            print(2)
            return HttpResponse(str(course2))
        elif id==3:
            print(3)
            return HttpResponse(str(course3))