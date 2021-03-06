# Generated by Django 2.2.4 on 2019-08-19 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20190816_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_hours',
            name='week_hours',
        ),
        migrations.AddField(
            model_name='classes',
            name='education',
            field=models.IntegerField(choices=[(0, '非本科'), (1, '本科')], default=0, verbose_name='学历'),
        ),
        migrations.AddField(
            model_name='classes',
            name='is_six',
            field=models.IntegerField(choices=[(0, '不是六天制'), (1, '是六天制')], default=0, verbose_name='是否为六天制'),
        ),
        migrations.AddField(
            model_name='classes',
            name='isprofessional',
            field=models.IntegerField(choices=[(0, '非专业'), (1, '专业')], default=0, verbose_name='是否相关专业'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='area',
            field=models.CharField(default=None, max_length=20, verbose_name='班级上课地点'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='now_stage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='professional.Stage', verbose_name='当前阶段'),
        ),
    ]
