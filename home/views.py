from django.shortcuts import render,HttpResponse,redirect,reverse
from classes.models import Classes
from professional.models import Stage,Professional,StageOrder
from orderclasses.order_classes import model
from teacher.models import Teachstage,Teacher
import json,calendar,datetime,pandas as pd,numpy as np
from .models import Course_week
from django.http import JsonResponse
# Create your views here.



def home(request):
    classes=Classes.objects.all()
    courseweek=Course_week.objects.all()
    data=courseweek
    return render(request, 'home/index.html',{'data':data})
    

# 根据前置课程获取阶段优先级排序列表stages,sortarr
def bToA(nowstage):
    stages=StageOrder.objects.filter(beforstage=nowstage)
    levelarr=[i.level for i in stages]
    nparr=np.array(levelarr)
    sortarr=list(reversed(np.argsort(nparr)))
    print(stages)
    print(sortarr)
    return stages,sortarr

# 阶段代课老师优先排序下标
def teacherorder(ts):
    arr1=[]
    for i in ts:
        arr1.append(i.level)
    nparr=np.array(arr1)
    sortteacher = list(reversed(np.argsort(nparr)))
    print(nparr)
    print(sortteacher)
    return sortteacher

# 获取下周时间范围
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
    date_list = [d.strftime("%Y%m%d") for d in pd.date_range(nextMonday, nextSunday, freq="D")]
    return date_list

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

    date_list = [d.strftime("%Y%m%d") for d in pd.date_range(nextMonday, nextSunday, freq="D")]
    return date_list

# 排班级优先级
# def ordercla():
#     classes=Classes.objects.all()
#     teachstage=Teachstage.objects.all()
#     teacher=Teacher.objects.all()
#     order=[]
#     for i in classes:
#         order.append(model.predict([[i.isprofessional,i.education,i.stu_num]])[0][0])
#     nd=np.array(order)
#     order_index=list(reversed(np.argsort(nd)))   #获得班级优先级的排序下标
#     class_sheet_list=[]
#     used_teachers=None
#     for i in order_index:        #对每一个班进行排课
#         i=int(i)
#         class_sheet = {}
#         class_sheet['classname']=classes[i].name
#         class_sheet['area']=classes[i].area
#         # class_sheet['time']=getNextday()
#         drection=classes[i].p_id
#         now_stage=classes[i].now_stage
#         long_time=Stage.objects.filter(name=now_stage.name).first().hours
#         now_long_time=classes[i].long_time
#         if classes[i].is_six:
#             if long_time-now_long_time>=48:
#                 class_sheet['stage']=[now_stage.name]
#                 class_sheet['long_time'] = [48]
#                 print('前',classes[i].long_time)
#                 classes[i].long_time += 48
#                 print('后',classes[i].long_time)
#                 # Classes.objects
#                 ts=teachstage.filter(stage=now_stage)
#                 sortteacher=teacherorder(ts)
#                 for i in sortteacher:
#                     i=int(i)
#                     teacherone=teacher.filter(name=ts[i].teacher.name)
#                     if teacherone[0].teachtime==0:
#                         class_sheet['teacher']=[teacherone[0].name]
#                         teacherone.update(teachtime=1)
#                         if used_teachers:
#                             used_teachers = used_teachers | teacherone
#                         else:
#                             used_teachers = teacherone
#                         break
#                     else:
#                         continue
#             # elif 0<long_time-now_long_time<48:
#             #     class_sheet['stage'] = [now_stage.name]
#             #     class_sheet['long_time'] = [long_time-now_long_time]
#             #     classes[i].long_time += long_time-now_long_time
#             #     stages, sortarr = bToA(now_stage)
#             else:
#                 stages, sortarr = bToA(now_stage)
#                 for i in sortarr:
#                     i=int(i)
#                     class_sheet['stage']=stages[i].afterstage.name
#                     class_sheet['long_time'] = [48]
#                     classes[i].long_time = 48
#                     classes[i].now_stage = stages[i].afterstage
#                     ts = teachstage.filter(stage=stages[i].afterstage)
#                     sortteacher = teacherorder(ts)
#                     for i in sortteacher:
#                         i = int(i)
#                         teacherone = teacher.filter(name=ts[i].teacher.name)
#                         if teacherone[0].teachtime == 0:
#                             class_sheet['teacher'] = [teacherone[0].name]
#                             if used_teachers:
#                                 used_teachers = used_teachers | teacherone
#                             else:
#                                 used_teachers = teacherone
#                             teacherone.update(teachtime=1)
#                             break
#                         else:
#                             continue
#         else:
#             if long_time-now_long_time>=40:
#                 class_sheet['stage']=[now_stage.name]
#                 class_sheet['long_time'] = [40]
#                 classes[i].long_time += 40
#                 ts=teachstage.filter(stage=now_stage)
#                 sortteacher=teacherorder(ts)
#                 for i in sortteacher:
#                     i=int(i)
#                     teacherone=teacher.filter(name=ts[i].teacher.name)
#                     if teacherone[0].teachtime==0:
#                         class_sheet['teacher']=[teacherone[0].name]
#                         if used_teachers:
#                             used_teachers = used_teachers | teacherone
#                         else:
#                             used_teachers = teacherone
#                         teacherone.update(teachtime=1)
#                         break
#                     else:
#                         continue
#             # elif 0<long_time-now_long_time<48:
#             #     class_sheet['stage'] = [now_stage.name]
#             #     class_sheet['long_time'] = [long_time-now_long_time]
#             #     classes[i].long_time += long_time-now_long_time
#             #     stages, sortarr = bToA(now_stage)
#             else:
#                 stages, sortarr = bToA(now_stage)
#                 for i in sortarr:
#                     i=int(i)
#                     class_sheet['stage']=stages[i].afterstage.name
#                     class_sheet['long_time'] = [40]
#                     classes[i].long_time = 40
#                     classes[i].now_stage = stages[i].afterstage
#                     ts = teachstage.filter(stage=stages[i].afterstage)
#                     sortteacher = teacherorder(ts)
#                     for i in sortteacher:
#                         i = int(i)
#                         teacherone = teacher.filter(name=ts[i].teacher.name)
#                         if teacherone[0].teachtime == 0:
#                             class_sheet['teacher'] = [teacherone[0].name]
#                             if used_teachers:
#                                 used_teachers = used_teachers | teacherone
#                             else:
#                                 used_teachers = teacherone
#                             teacherone.update(teachtime=1)
#                             break
#                         else:
#                             continue
#         # 所有老师和已选中老师的差集,并选择助教
#         # if classes[i].is_teacher2:
#         # # print('teacher:',teacher)
#         # # print('used_teachers:',used_teachers)
#         #     teacher2=teacher.difference(used_teachers)
#         # # print(teacher2)
#         #     sortteacher2=[]
#         #     for i in teacher2:
#         #         sortteacher2.append(i.classesed)
#         #     sortteacher2=np.argsort(np.array(sortteacher2))
#         #     for i in sortteacher2:
#         #         print(teacher2)
#         #         class_sheet['teacher2']=[teacher2[i].name]
#         #         teacher2[i].update(teachtime=1)
#
#         classes[i].save()
#         class_sheet_list.append(class_sheet)
#     Teacher.objects.all().update(teachtime=0)
#     # print(class_sheet_list)
#
#
#
#     return class_sheet_list

# 返回班级下标sortclass
def sort_class():
    classes = Classes.objects.all()
    order = []
    for i in classes:
        order.append(model.predict([[i.isprofessional, i.education, i.stu_num, i.is_outside]])[0][0])
    sortclass = list(reversed(np.argsort(np.array(order))))
    return sortclass

# 返回对于某阶段的老师以及排序下标teacherarr,sortteacher
def sort_teacher(stage):
    teacherstage=Teachstage.objects.all()
    tss=teacherstage.filter(stage=stage)
    teacherarr=[i.teacher for i in tss]
    sortteacher=list(reversed(np.argsort(np.array([i.level for i in tss]))))
    return teacherarr,sortteacher


def ordercla():
    classes=Classes.objects.all() #班级
    teachstage=Teachstage.objects.all()  #老师和阶段
    teacher=Teacher.objects.all()  #老师
    for i in teacher:
        i.state='00000000000000'
        i.save()
    stage=Stage.objects.all() # 阶段
    class_sheet_list=[]
    sortclass=sort_class()
    for i in sortclass:
        i=int(i)
        class_sheet={}
        class_i=classes[i]
        classesname=class_sheet['classname']=classes[i].name
        class_sheet['area']=classes[i].area
        class_sheet['course']=[]    #班级每天上下午的课程，包含14个列表
        nowstage=classes[i].now_stage
        longtime=int(stage.filter(name=nowstage.name).first().hours)
        now_long_time=int(classes[i].long_time)
        around=int(classes[i].around)
        week_time=around * 4 #本周上课总课时
        work_day=around #本周上课天数
        # 如果剩余课时大于一周课时进行周排
        if longtime - now_long_time >= week_time:
            print(1)
            halfday={}
            halfday['stage'] = nowstage.name
            classes.filter(name=classesname).update(long_time=now_long_time + week_time)
            teacherarr, sortteacher = sort_teacher(nowstage)
            for b in sortteacher:
                b=int(b)
                if teacherarr[b].state=='00000000000000':
                    halfday['teacher']=teacherarr[b].name
                    teacherstate=teacherarr[b]
                    teacherstate.state='11111111111111'
                    teacherstate.save()
                    break
                else:
                    continue
            else:
                halfday['teacher']='没有空闲老师'
            class_sheet['course'].append(halfday)  #直接排出一周的课
            class_sheet['course']=class_sheet['course']*around  #每半天都相同*周期
        # 如果剩余课时为零，下一个阶段进行周排
        elif longtime == now_long_time:
            print(2)
            halfday = {}
            stages, sortarr=bToA(nowstage)
            if not len(stages):
                halfday['stage'] = '结训'
                continue
            print('stages',stages)
            print(int(sortarr[0]))
            afterstage = stages[int(sortarr[0])].afterstage
            halfday['stage'] = afterstage.name
            class_i.now_stage=afterstage
            class_i.long_time=week_time
            class_i.save()
            teacherarr, sortteacher = sort_teacher(afterstage)
            for b in sortteacher:
                b = int(b)
                if teacherarr[b].state == '00000000000000':
                    halfday['teacher'] = teacherarr[b].name
                    teacherstate = teacherarr[b]
                    teacherstate.state = '11111111111111'
                    teacherstate.save()
                    break
                else:
                    continue
            else:
                halfday['teacher'] = '没有空闲老师'
            class_sheet['course'].append(halfday)  # 直接排出一周的课
            class_sheet['course'] = class_sheet['course'] * around  # 每半天都相同*周期
        # 以上都不符合，进行单排
        else:
            print(3)
            # 排每个半天 j代表一周上几个上下午
            for j in range(around):
                halfday={}
                # 如果还没有进入下一个阶段
                if longtime-now_long_time>4:
                    halfday['stage']=nowstage.name
                    now_long_time=int(classes[i].long_time)
                    classes.filter(name=classesname).update(long_time=now_long_time+4)
                    teacherarr,sortteacher=sort_teacher(nowstage)
                    # 遍历老师下标
                    for z in sortteacher:
                        z=int(z)
                        teacher=teacherarr[z]
                        state=list(teacher.state)
                        # 判断老师状态
                        print('state',state)
                        print(j)
                        if state[j]=='0':
                            halfday['teacher']=teacher.name
                            state[j]='1'
                            teacher.state=''.join(state)
                            teacher.save()
                            break
                        else:
                            continue
                    else:
                        halfday['teacher'] = '没有空闲老师'
                    class_sheet['course'].append(halfday)
                else:
                    stages, sortarr = bToA(nowstage)
                    if not len(stage):
                        halfday['stage'] = '结训'
                        continue
                    print(int(sortarr[0]))
                    print('stages',stages)
                    afterstage = stages[int(sortarr[0])].afterstage
                    halfday['stage'] = afterstage.name
                    class_i.now_stage = afterstage
                    class_i.long_time = week_time
                    class_i.save()
                    teacherarr, sortteacher = sort_teacher(afterstage)
                    for b in sortteacher:
                        b = int(b)
                        if teacherarr[b].state[j] == '0':
                            halfday['teacher'] = teacherarr[b].name
                            teacherstate = teacherarr[b]
                            state = list(teacherstate.state)
                            state[j] = '1'
                            teacherstate.state = ''.join(state)
                            teacherstate.save()
                            break
                        else:
                            continue
                    else:
                        halfday['teacher'] = '没有空闲老师'
                    class_sheet['course'].append(halfday)
        class_sheet_list.append(class_sheet)
    print(class_sheet_list)
    return class_sheet_list






class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y/%m/%d')

# 获取课程表
def getcourse(request,id):
    courseweek=Course_week.objects.all()
    if request.method=='GET':
        id=int(id)
        if id==1:
            if courseweek:
                course1=courseweek[0].first_week
            else:
                course1 = {"time":getNextday(),"data":ordercla()}
                course1 = json.dumps(course1)
                courseweek.create(first_week=course1)

            course1=json.loads(course1)
            return JsonResponse(course1)
        elif id==2:
            if courseweek[0].second_week:
                course2 = courseweek[0].second_week
            else:
                course2 = {"time": getN_N_day(), "data": ordercla()}
                # courseweek[0].second_week=course2
                course2=json.dumps(course2)
                courseweek.update(second_week=course2)
            course2 = json.loads(course2)
            return JsonResponse(course2)
        elif id==3:
            if courseweek[0].third_week:
                course3 = courseweek[0].third_week
            else:
                course3 = {"time": getN_N_N_day(), "data": ordercla()}
                course3 = json.dumps(course3)
                courseweek.update(third_week=course3)
            course3 = json.loads(course3)
            return JsonResponse(course3)

# 修改保存课程表
def changecourse(request,id):
    courseweek=Course_week.objects.all()
    data=request.POST.get('data',None)
    if not data:
        return HttpResponse('数据错误')
    id=int(id)
    if id==1:
        courseweek.update(first_week=data)
    elif id==2:
        courseweek.update(second_week=data)
    elif id==3:
        courseweek.update(third_week=data)
    else:
        return HttpResponse('信息错误')
    return HttpResponse('ok')

# 通过老师获取阶段
def teachertostage(request):
    tname=request.POST.get('tname')
    teacher=Teacher.objects.filter(name=tname).first()
    print(teacher)
    teachstages=Teachstage.objects.filter(teacher=teacher)
    stagearr=[i.stage.name for i in teachstages]
    data={'stage':stagearr}
    return JsonResponse(data)

# 通过阶段获取老师
def stagetoteacher(request):
    sname=request.POST.get('sname')
    stage=Stage.objects.filter(name=sname).first()
    stages=Teachstage.objects.filter(stage=stage)
    teacherarr=[i.teacher.name for i in stages]
    data={'teacher':teacherarr}
    return JsonResponse(data)


def data(request):
    ordercla()
    return HttpResponse('123')