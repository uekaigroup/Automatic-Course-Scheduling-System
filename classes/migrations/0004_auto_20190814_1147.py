# Generated by Django 2.2.4 on 2019-08-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20190813_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='is_teacher2',
            field=models.IntegerField(choices=[(0, '不需要助教'), (1, '必须要助教')], default=0, verbose_name='是否需要助教'),
        ),
    ]
