# Generated by Django 2.2.4 on 2019-08-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_auto_20190823_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='around',
            field=models.IntegerField(default=5, verbose_name='上课周期'),
        ),
    ]
