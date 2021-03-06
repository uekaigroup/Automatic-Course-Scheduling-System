# Generated by Django 2.2.4 on 2019-08-16 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0008_delete_pub_stage'),
        ('classes', '0004_auto_20190814_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='is_outside',
            field=models.IntegerField(choices=[(0, '不是校外课程'), (1, '是校外课程')], default=0, verbose_name='是否需要助教'),
        ),
        migrations.AddField(
            model_name='classes',
            name='long_time',
            field=models.IntegerField(default=0, verbose_name='当前阶段进行时长'),
        ),
        migrations.AddField(
            model_name='classes',
            name='now_stage',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='professional.Stage', verbose_name='当前阶段'),
        ),
        migrations.AddField(
            model_name='classes',
            name='stu_num',
            field=models.IntegerField(default=0, verbose_name='班级人数'),
        ),
        migrations.AlterField(
            model_name='class_hours',
            name='week_hours',
            field=models.BinaryField(default=None, max_length=30, verbose_name='每天上下午带课时长'),
        ),
    ]
