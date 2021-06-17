# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 12:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200313_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 15, 6, 53, 553996), verbose_name='Время Добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 15, 6, 53, 553996), verbose_name='Время Обновления'),
        ),
    ]