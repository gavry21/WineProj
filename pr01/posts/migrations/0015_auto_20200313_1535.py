# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 12:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20200313_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='email', max_length=254, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='Имя', max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='author',
            name='second_name',
            field=models.CharField(default='Фамилия', max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 15, 35, 59, 884368), verbose_name='Время Добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 15, 35, 59, 884368), verbose_name='Время Обновления'),
        ),
    ]
