# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0002_auto_20160814_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
