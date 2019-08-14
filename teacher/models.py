from django.db import models
from professional.models import Stage
# Create your models here.


# 教师表
class Teacher(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='教师姓名'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='布道师'


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
    t_id=models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        verbose_name='对应教师',
        default=0,
    )



