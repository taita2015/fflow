# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 15:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('credit', '0003_everydaycreditlog_threadviewlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditDefault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_point', models.IntegerField(default=10)),
                ('last_modify', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户积分',
                'verbose_name_plural': '用户积分',
            },
        ),
        migrations.RemoveField(
            model_name='usercreditdefault',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserCreditDefault',
        ),
    ]
