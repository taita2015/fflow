# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0011_auto_20170420_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditlog',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
