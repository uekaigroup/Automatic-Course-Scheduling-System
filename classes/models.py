from django.db import models
from django.utils import timezone
from professional.models import Professional,Stage
from area.models import Area

from django import forms
# Create your models here.

# 班级课时数据表
class class_hours(models.Model):
    week_hours=models.BinaryField(
        max_length=30,
        verbose_name='每天上下午代课时长',
        default=None,
    )
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
    is_teacher2=models.IntegerField(choices=(
        (0,'不需要助教'),
        (1,'必须要助教')),
        default=0,verbose_name='是否需要助教'
    )
    area=models.ForeignKey(
        to=Area,
        on_delete=models.CASCADE,
        verbose_name='班级上课地点'
    )
    start_time=models.DateTimeField('开班时间',default=timezone.now)
    add_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='班级'

