from django.db import models
# from teacher.models import Teacher
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
    # teachers=models.ManyToManyField(
    #     Teacher,
    #     through='teachstage',
    #     # through_fields=('teacher','stage'),
    # )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='阶段'

# class Teachstage(models.Model):
#     teacher=models.ForeignKey(
#         Teacher,
#         on_delete=models.CASCADE,
#     )
#     stage=models.ForeignKey(
#         Stage,
#         on_delete=models.CASCADE
#     )
#     level=models.IntegerField(
#         verbose_name='阶段代课频数',
#         default=0,
#     )

# 阶段优先表
class StageOrder(models.Model):
    beforstage=models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        related_name='beforstage'
    )
    afterstage=models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        related_name='afterstage'
    )
    level=models.IntegerField(
        verbose_name='配合优先级'
    )
    def __str__(self):
        return self.beforstage.name
    class Meta():
        verbose_name_plural='阶段优先级'

















































