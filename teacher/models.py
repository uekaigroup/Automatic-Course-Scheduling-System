from django.db import models
from professional.models import Stage
# Create your models here.


# 老师代课数据表
class TeacherData(models.Model):
    weekday=models.CharField(
        max_length=20,
        verbose_name='代课星期'
    )
    hours=models.CharField(
        max_length=20,
        verbose_name='每天课时'
    )

# 教师表
class Teacher(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='教师名字'
    )
    teacher_data=models.ForeignKey(
        to=TeacherData,
        on_delete=models.CASCADE,
        verbose_name='教师数据表'
    )
class Teacher_stage(models.Model):
    t_id=models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        verbose_name='布道师'
    )
    s_id=models.ForeignKey(
        to=Stage,
        on_delete=models.CASCADE,
        verbose_name='阶段'
    )
    priority=models.IntegerField(
        verbose_name='优先级'
    )