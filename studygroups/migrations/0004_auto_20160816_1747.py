# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 00:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0003_auto_20160814_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.RenameField(
            model_name='studygroup',
            old_name='stat_time',
            new_name='start_time',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
