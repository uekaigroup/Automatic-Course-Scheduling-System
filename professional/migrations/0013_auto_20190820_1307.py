# Generated by Django 2.2.4 on 2019-08-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0012_auto_20190820_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='teachers',
            field=models.ManyToManyField(through='professional.Teachstage', to='teacher.Teacher'),
        ),
    ]
