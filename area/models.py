from django.db import models

# Create your models here.

# 地点表
class Area(models.Model):
    con=models.CharField(
        max_length=20,
        verbose_name='上课地点'
    )