from django.db import models

# Create your models here.

# 专业方向表
class Professional(models.Model):
    name=models.CharField(
        max_length=20,
        verbose_name='方向名称'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='方向分类'


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
    p_id=models.ForeignKey(
        to=Professional,
        on_delete=models.CASCADE,
        verbose_name='对应方向',
        default=None
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='阶段'


# 公共阶段表
# class Pub_stage(models.Model):
#     name=models.CharField(
#         max_length=20,
#         verbose_name='共有阶段表'
#     )
#     long_time=models.IntegerField(
#         verbose_name='阶段时长',
#         default=0
#     )
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural='公共阶段'


