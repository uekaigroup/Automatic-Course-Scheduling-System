# Generated by Django 2.2.4 on 2019-08-21 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_week',
            name='first_week',
            field=models.CharField(default=None, max_length=200, verbose_name='下周课程数据'),
        ),
        migrations.AlterField(
            model_name='course_week',
            name='second_week',
            field=models.CharField(default=None, max_length=200, verbose_name='下下周课程数据'),
        ),
        migrations.AlterField(
            model_name='course_week',
            name='third_week',
            field=models.CharField(default=None, max_length=200, verbose_name='下下下周课程数据'),
        ),
    ]
