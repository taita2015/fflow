# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0030_threadlike'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AlterModelOptions(
            name='threadlike',
            options={'verbose_name': '点赞', 'verbose_name_plural': '点赞'},
        ),
    ]