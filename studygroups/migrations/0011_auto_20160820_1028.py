# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 17:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0010_auto_20160820_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
