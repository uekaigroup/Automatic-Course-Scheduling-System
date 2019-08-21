from django.db import models

# Create your models here.

class Course_week(models.Model):
    first_week=models.CharField(
        max_length=200,
        verbose_name='下周课程数据',
    )
    second_week=models.CharField(
        max_length=200,
        verbose_name='下下周课程数据'
    )
    third_week=models.CharField(
        max_length=200,
        verbose_name='下下下周课程数据'
    )