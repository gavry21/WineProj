# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 13:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_auto_20200313_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('r', 'Роман'), ('p', 'Поэма'), ('rr', 'Рассказ')], default='r', max_length=120, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 16, 14, 34, 934025), verbose_name='Время Добавления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 16, 14, 34, 934025), verbose_name='Время Обновления'),
        ),
    ]