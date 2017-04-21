# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 04:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0009_auto_20170419_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToUserMessageSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('a_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_a_user', to=settings.AUTH_USER_MODEL)),
                ('b_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_b_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
