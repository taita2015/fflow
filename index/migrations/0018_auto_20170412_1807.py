# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_auto_20170409_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='使用语言'),
            preserve_default=False,
        ),
    ]
