from django.db import models

# Create your models here.

# 专业方向表
class Professional(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='方向名称'
    )

# 阶段表
class Stage(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='阶段名称'
    )
    week=models.IntegerField(
        verbose_name='阶段周数'
    )
    hours=models.IntegerField(
        verbose_name='课时数'
    )
    order=models.IntegerField(
        verbose_name='阶段排列顺序'
    )