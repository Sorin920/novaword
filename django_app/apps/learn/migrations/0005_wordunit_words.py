# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-21 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_auto_20170821_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordunit',
            name='words',
            field=models.ManyToManyField(to='learn.Word'),
        ),
    ]
