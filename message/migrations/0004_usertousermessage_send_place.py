# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20170419_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertousermessage',
            name='send_place',
            field=models.BooleanField(default=False),
        ),
    ]