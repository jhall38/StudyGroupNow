# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studygroup',
            name='name',
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='end_time',
            field=models.DateTimeField(),
        ),
    ]
