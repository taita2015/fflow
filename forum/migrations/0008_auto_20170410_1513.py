# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20170410_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subclass',
            name='display_name',
            field=models.CharField(default='', max_length=20, verbose_name='显示名字'),
            preserve_default=False,
        ),
    ]