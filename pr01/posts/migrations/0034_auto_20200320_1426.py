# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-20 11:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_auto_20200320_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 14, 26, 54, 663881), verbose_name='Время Добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 14, 26, 54, 663881), verbose_name='Время Обновления'),
        ),
    ]
