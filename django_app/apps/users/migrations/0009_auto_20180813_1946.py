# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-13 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_group_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='password',
            field=models.CharField(blank=True, default=users.models.generate_token, max_length=100, verbose_name='进组密码'),
        ),
    ]
