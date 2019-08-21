from django.shortcuts import render,HttpResponse,redirect,reverse
from classes.models import Classes
from professional.models import Stage,Professional,StageOrder
from orderclasses.order_classes import model
from teacher.models import Teachstage,Teacher
import numpy as np
import json
from .models import Course_week
from django.http import JsonResponse
# Create your views here.



def home(request,id=0):
    classes=Classes.objects.all()
    courseweek=Course_week.objects.all()
    id=int(id)
    print(id)
    data=None
    if not courseweek:
        return render(request, 'home/index.html', {'data': data})
    if id==1:
        data=courseweek[0].first_week
    elif id==2:
        data = courseweek[0].second_week
    elif id==3:
        data = courseweek[0].third_week
    return render(request, 'home/index.html',{'data':data})
    

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
    today3 = datetime.date.today()
    today4 = datetime.date.today()
    today5 = datetime.date.today()
    today6 = datetime.date.today()
    today7 = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    m1 = calendar.MONDAY
    m2 = calendar.TUESDAY
    m3 = calendar.WEDNESDAY
    m4 = calendar.THURSDAY
    m5 = calendar.FRIDAY
    m6 = calendar.SATURDAY
    m7 = calendar.SUNDAY

    while today1.weekday() != m1:
        today1 += oneday
    while today2.weekday() != m2:
        today2 += oneday
    while today3.weekday() != m3:
        today3 += oneday
    today3 += oneday
    while today3.weekday() != m3:
        today3 += oneday
    while today4.weekday() != m4:
        today4 += oneday
    today4 += oneday
    while today4.weekday() != m4:
        today4 += oneday
    while today5.weekday() != m5:
        today5 += oneday
    today5 += oneday
    while today5.weekday() != m5:
        today5 += oneday
    while today6.weekday() != m6:
        today6 += oneday
    today6 += oneday
    while today6.weekday() != m6:
        today6 += oneday
    while today7.weekday() != m7:
        today7 += oneday
    today7 += oneday
    while today7.weekday() != m7:
        today7 += oneday

    nextMonday = today1.strftime('%Y%m%d')
    nextTuesday = today2.strftime('%Y%m%d')
    nextWEDNESDAY  = today3.strftime('%Y%m%d')
    nextTHURSDAY= today4.strftime('%Y%m%d')
    nextFRIDAY = today5.strftime('%Y%m%d')
    nextSATURDAY = today6.strftime('%Y%m%d')
    nextSunday = today7.strftime('%Y%m%d')

    return [nextMonday,nextTuesday,nextWEDNESDAY,nextTHURSDAY,nextFRIDAY,nextSATURDAY,nextSunday]

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

    return [nextMonday,int(nextMonday)+1,int(nextMonday)+2,int(nextMonday)+3,int(nextMonday)+4,int(nextMonday)+5,nextSunday]


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

    return [nextMonday,int(nextMonday)+1,int(nextMonday)+2,int(nextMonday)+3,int(nextMonday)+4,int(nextMonday)+5,nextSunday]


def ordercla():
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
                print('前',classes[i].long_time)
                classes[i].long_time += 48
                print('后',classes[i].long_time)
                # Classes.objects
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
                    class_sheet['stage']=stages[i].afterstage.name
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
                    class_sheet['stage']=stages[i].afterstage.name
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
    # print(class_sheet_list)



    return class_sheet_list

class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y/%m/%d')



def getcourse(request,id):
    courseweek=Course_week.objects.all()
    if request.method=='GET':
        id=int(id)
        if id==1:
            if courseweek:
                # print(type(courseweek[0].first_week))
                course1=json.loads(courseweek[0].first_week)
                print("asdfaetwet",course1)
            else:
                course1 = {"time":getNextday(),"data":ordercla()}
                course1 = json.dumps(course1)
                courseweek.create(first_week=course1)

            return JsonResponse(course1)
        elif id==2:
            if courseweek[0].second_week:
                course2 = courseweek[0].second_week
                course2=json.dumps(course2)
                return JsonResponse(course2)
            else:
                course2 = {"time": getN_N_day(), "data": ordercla()}
                # courseweek[0].second_week=course2
                course2=json.dumps(course2)
                courseweek.update(second_week=course2)
                return HttpResponse(json.dumps(course2, cls=DateEnconding))
        elif id==3:
            if courseweek[0].third_week:
                course3 = courseweek[0].third_week
                course3 = json.dumps(course3)
                return JsonResponse(course3)
            else:
                course3 = {"time": getN_N_N_day(), "data": ordercla()}
                course3 = json.dumps(course3)
                courseweek.update(third_week=course3)
                return HttpResponse(json.dumps(course3, cls=DateEnconding))

def changecourse(request,id):
    courseweek=Course_week.objects.all()
    data=request.POST.get('data',None)
    data = json.dumps(data)
    if id==1:
        courseweek.update(first_week=data)
    elif id==2:
        courseweek.update(second_week=data)
    else:
        courseweek.update(third_week=data)
    return redirect(reverse('home:home'))