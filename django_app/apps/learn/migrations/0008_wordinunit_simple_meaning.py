# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-06 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0007_auto_20170823_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordinunit',
            name='simple_meaning',
            field=models.CharField(default='', max_length=100, verbose_name='\u7b80\u5355\u89e3\u91ca'),
        ),
    ]
