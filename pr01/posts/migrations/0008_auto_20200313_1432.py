# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 11:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200313_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 14, 32, 45, 845024), verbose_name='Время Добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 14, 32, 45, 845024), verbose_name='Время Обновления'),
        ),
    ]
