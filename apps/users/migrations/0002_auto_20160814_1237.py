# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 04:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comment',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='\u624b\u673a\u53f7'),
        ),
        migrations.AlterField(
            model_name='user',
            name='private_key',
            field=models.CharField(max_length=5000, verbose_name='ssh\u79c1\u94a5'),
        ),
        migrations.AlterField(
            model_name='user',
            name='public_key',
            field=models.CharField(max_length=1000, verbose_name='\u516c\u94a5'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Role', verbose_name='\u89d2\u8272'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='comment',
            field=models.TextField(blank=True, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='\u7ec4\u540d\u79f0'),
        ),
    ]