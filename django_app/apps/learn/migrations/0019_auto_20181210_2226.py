# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-10 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import utils.time_util


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0018_wordbook_maintainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorword',
            name='latest_error_time',
            field=models.DateTimeField(default=utils.time_util.get_now, verbose_name='最近一次答错时间'),
        ),
        migrations.AlterField(
            model_name='learningrecord',
            name='learn_time',
            field=models.DateTimeField(default=utils.time_util.get_now, verbose_name='学习时间'),
        ),
    ]
