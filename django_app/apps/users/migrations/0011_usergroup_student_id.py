# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-08 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180814_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='student_id',
            field=models.IntegerField(default=0, verbose_name='学号'),
        ),
    ]