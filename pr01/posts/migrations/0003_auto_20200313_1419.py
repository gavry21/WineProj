# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 11:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200313_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='', verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 14, 19, 25, 521102), verbose_name='Время Добавления'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 14, 19, 25, 521102), verbose_name='Время Обновления'),
        ),
    ]
