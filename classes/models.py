from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

# 方向表
class Direction(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='课程方向'
    )

# 阶段表
class Stage(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='课程阶段'
    )
    time=models.IntegerField(
        verbose_name='阶段天数'
    )
    d=models.ForeignKey(
        to=Direction,
        on_delete=models.CASCADE,
        verbose_name='方向外键',
        related_name='Stage_d'
    )
    order=models.IntegerField(
        verbose_name='阶段排序'
    )

# 教师表
class Teacher(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='布道师名字'
    )
    s=models.ManyToManyField(
        to=Stage,
        verbose_name='教师可带课程'
    )
    lock_day=models.CharField(
        max_length=50,
        verbose_name='教师锁定日期'
    )


# 班级表
class Classes(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='班级名称'
    )
    d=models.ForeignKey(
        to=Direction,
        on_delete=models.CASCADE,
        related_name='Classes_d'
    )
    school=models.CharField(
        max_length=20,
        verbose_name='合作院校'
    )
    stime=models.DateTimeField('开班时间',default=timezone.now)
    now_stage=models.CharField(
        verbose_name='本周阶段',
    )
    now_teacher=models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        verbose_name='目前布道师',
        related_name='now_teacher'
    )
    now_sistant=models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        verbose_name='目前助教',
        related_name='now_sistant'
    )
    next_stage = models.ForeignKey(
        to=Stage,
        on_delete=models.CASCADE,
        verbose_name='下个阶段',
        related_name='next_stage'
    )
    next_teacher = models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        verbose_name='下阶段布道师',
        related_name='next_teacher'
    )
    next_sistant = models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        verbose_name='下阶段助教',
        related_name='next_sistant'
    )
    issistant=models.IntegerField(choices=(
        ('0','不需要助教'),
        (1,'必须要助教')),
        default=0,verbose_name='是否需要助教'
    )
    add_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

# 老师阶段表
# class TeacherStage(models.Model):
#     tid=models.ForeignKey(
#         to=Teacher,
#         on_delete=models.CASCADE,
#         verbose_name='布道师',
#         related_name='tid'
#     )
#     sid=models.ForeignKey(
#         to=Stage,
#         on_delete=models.CASCADE,
#         verbose_name='阶段',
#         related_name='sid'
#     )
#     level=models.IntegerField(
#         verbose_name='匹配优先级'
#     )
# #
# # 阶段组合优先级
# class StageToStage(models.Model):
#     d=models.ForeignKey(
#         to=Direction,
#         on_delete=models.CASCADE,
#         verbose_name='所属方向'
#     )
#     bstage=models.ForeignKey(
#         to=Stage,
#         on_delete=models.CASCADE,
#         verbose_name='前导课程'
#     )
#     nstage=models.ForeignKey(
#         to=Stage,
#         on_delete=models.CASCADE,
#         verbose_name='后置课程',
#         related_name='StageToStage_nstage'
#     )
#     level=models.IntegerField(
#         verbose_name='阶段组合优先级'
#     )
#
# # 阶段组合变更记录表
# class StageChangeRecord(models.Model):
#     d = models.ForeignKey(
#         to=Direction,
#         on_delete=models.CASCADE,
#         verbose_name='所属方向'
#     )
#     bstage = models.ForeignKey(
#         to=Stage,
#         on_delete=models.CASCADE,
#         verbose_name='前导课程'
#     )
#     nstage = models.ForeignKey(
#         to=Stage,
#         on_delete=models.CASCADE,
#         verbose_name='后置课程',
#         related_name='StageChangeRecord_nstage'
#     )
#     reason=models.TextField(
#         max_length=600,
#         verbose_name='更换原因'
#     )
#     update_time=models.DateTimeField(
#         auto_now=True,
#         verbose_name='更改时间'
#     )

# # 校外课程阶段表
# class OutsidStage(models.Model):
#     s=models.ForeignKey(
#         to=Stage,
#         on_delete=models.CASCADE,
#         verbose_name='校外课程阶段'
#     )
#     days=models.CharField(
#         max_length=50,
#         verbose_name='阶段天数'
#     )
#     teacher=models.IntegerField(
#         verbose_name='代课老师'
#     )
#
#
# # 校外课程表
# class OutsidCourse(models.Model):
#     school=models.CharField(
#         max_length=20,
#         verbose_name='学校名称'
#     )
#     project=models.CharField(
#         max_length=20,
#         verbose_name='项目名称'
#     )
#
# # 市场课记录表
# class Outside(models.Model):
#     days=models.IntegerField(
#         verbose_name='上课天数'
#     )
#     teachers=models.IntegerField(
#         verbose_name='老师数量'
#     )