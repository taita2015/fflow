# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 01:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'verbose_name': '好友', 'verbose_name_plural': '好友'},
        ),
    ]