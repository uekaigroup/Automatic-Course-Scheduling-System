from django.db import models
from django.utils import timezone
from professional.models import Professional,Stage
from area.models import Area

from django import forms
# Create your models here.

# 班级课时数据表
class class_hours(models.Model):
    # week_hours=models.BinaryField(
    #     max_length=30,
    #     verbose_name='每天上下午带课时长',
    #     default=None,
    # )
    # hours=models.CharField(
    #     max_length=30,
    #     verbose_name='每天上课'
    #
    # )
    tercher=models.CharField(
        max_length=30,
        verbose_name='老师上课天数'
    )
    tercher2 = models.CharField(
        max_length=30,
        verbose_name='助教上课天数'
    )

# def start():
#     return Stage.objects.filter(name='开训')[0].id


# 班级表
class Classes(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='班级名称'
    )
    p_id=models.ForeignKey(
        to=Professional,
        on_delete=models.CASCADE
    )
    stu_num=models.IntegerField(
        verbose_name='班级人数',
        default=0
    )
    now_stage=models.ForeignKey(
        to=Stage,
        on_delete=models.CASCADE,
        verbose_name='当前阶段',
        default=None
    )
    long_time = models.IntegerField(
        verbose_name='当前阶段进行时长',
        default=0
    )
    isprofessional=models.IntegerField(choices=(
        (0,'非专业'),
        (1,'专业')),
        default=0,verbose_name='是否相关专业'
    )
    education=models.IntegerField(choices=(
        (0,'非本科'),
        (1,'本科')),
        default=0,verbose_name='学历'
    )
    now_teacher=models.CharField(
        max_length=20,
        verbose_name='当前代课老师名字',
        default=' '
    )
    is_six=models.IntegerField(choices=(
        (0,'不是六天制'),
        (1,'是六天制')),
        default=0,verbose_name='是否为六天制'
    )
    around=models.IntegerField(
        verbose_name='上课周期',
        default=5
    )
    someday=models.CharField(
        max_length=20,
        verbose_name='哪几天上课',
        default='0'
    )
    is_teacher2 = models.IntegerField(choices=(
        (0, '不需要助教'),
        (1, '必须要助教')),
        default=0, verbose_name='是否需要助教'
    )
    is_outside = models.IntegerField(choices=(
        (0, '不是校外课程'),
        (1, '是校外课程')),
        default=0, verbose_name='是否校外课程'
    )
    area=models.CharField(
        max_length=20,
        verbose_name='班级上课地点',
        default=None
    )
    start_time=models.DateTimeField('开班时间',default=timezone.now)
    add_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='班级'


