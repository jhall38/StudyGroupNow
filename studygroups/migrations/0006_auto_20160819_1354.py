# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0005_auto_20160817_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='email_public',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='remail_public',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
