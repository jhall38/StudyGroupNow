# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0012_auto_20160820_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='name',
            field=models.CharField(error_messages={'blank': 'You must give your Study Group a name'}, max_length=20),
        ),
    ]
