# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 03:58
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0014_auto_20160820_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(error_messages={'blank': 'You must enter an address', 'max_length': 'The address may not exceed 500 characters. Remember you are not suppose to enter in the city, state, country, or zipcode.'}, max_length=500),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(error_messages={'blank': 'You must enter a name for this location', 'max_length': 'The name may not exceed 50 characters. Please enter a shorter name.'}, max_length=50),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='course_code',
            field=models.CharField(error_messages={'blank': 'You must enter a course number'}, max_length=15, validators=[django.core.validators.RegexValidator(message='Improper Course Code Format! (EX: INFO 344, PHYS 444H)', regex='^[a-zA-Z]* [0-9]{2,3}[a-zA-Z]{0,2}$')]),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='description',
            field=models.CharField(error_messages={'blank': 'You must enter a description!', 'max_length': 'Your description is too long! Pleaseenter a description that is 500 characters or less.'}, max_length=500),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='end_time',
            field=models.DateTimeField(error_messages={'blank': 'You must enter an ending date and time', 'invalid_choice': 'The date and time you entered is invalid. Please check your input and try again. If you are using the API, the proper format is YYY-MM-DD HH:MM:SS'}),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='name',
            field=models.CharField(error_messages={'blank': 'You must give your Study Group a name!', 'max_length': 'The name of your Study Group cannot be more than 20 characters'}, max_length=20),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime.now, error_messages={'blank': 'You must enter a starting date and time', 'invalid_choice': 'The date and time you entered is invalid. Please check your input and try again. If you are using the API, the proper format is YYY-MM-DD HH:MM:SS'}),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bio',
            field=models.CharField(blank=True, error_messages={'max_length': 'Your about section is too long! Please do not exceed 500 characters'}, max_length=500),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email_public',
            field=models.CharField(blank=True, error_messages={'max_length': 'Your email is too long! Please enter an email that has 200 characters or less.'}, max_length=200, validators=[django.core.validators.EmailValidator(message='Please enter a valid email!')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='facebook_link',
            field=models.CharField(blank=True, error_messages={'max_length': 'Please use a link that is less than 300 characters long.'}, max_length=300, validators=[django.core.validators.RegexValidator(message='Please enter a valid facebook profile link "https://www.facebook.com/..."', regex='^https:\\/\\/www\\.facebook\\.com\\/.+$')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(blank=True, error_messages={'max_length': 'The name you entered is too long! Please enter a name that is less than 100 characters.'}, max_length=100, validators=[django.core.validators.RegexValidator(message='Please enter a valid name (only letters)', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ideal_study_group',
            field=models.CharField(blank=True, error_messages={'max_length': 'The ideal study group section is too long! Please do not exceed 1000 characters.'}, max_length=1000),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(blank=True, error_messages={'max_length': 'The name you entered is too long! Please enter a name that is less than 100 characters.'}, max_length=100, validators=[django.core.validators.RegexValidator(message='Please enter a valid name (only letters)', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='major',
            field=models.CharField(blank=True, error_messages={'max_length': 'The major you entered is invalid! Please enter a major that does not exceed 50 characters'}, max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='minor',
            field=models.CharField(blank=True, error_messages={'max_length': 'The minor you entered is invalid! Please enter a major that does not exceed 50 characters'}, max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.CharField(blank=True, error_messages={'max_length': 'Invalid phone number! Please enter in the format of (###) ###-####'}, max_length=14, validators=[django.core.validators.RegexValidator(message="Please enter a valid phone number in the format of '(###) ###-####'.", regex='^\\([0-9]{3}\\) [0-9]{3}-[0-9]{4}$')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, error_messages={'invalid': 'Invalid profile picture! You may only upload image files.'}, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='year',
            field=models.CharField(blank=True, error_messages={'max_length': 'Please enter a valid year (Freshmen, Sophmore, Junior, Senior, Beyond Senior'}, max_length=20),
        ),
    ]
