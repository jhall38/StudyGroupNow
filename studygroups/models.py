from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files.storage import default_storage
from django.core.validators import RegexValidator, EmailValidator
import datetime

class Location(models.Model):
	name = models.CharField(max_length=50, error_messages={'blank': 'You must enter a name for this location', 'max_length': 'The name may not exceed 50 characters. Please enter a shorter name.'})
	address = models.CharField(max_length=500, error_messages={'blank': 'You must enter an address', 'max_length': 'The address may not exceed 500 characters. Remember you are not suppose to enter in the city, state, country, or zipcode.'})
	lat = models.FloatField()
	lon = models.FloatField()

class StudyGroup(models.Model):
	name = models.CharField(max_length=20, error_messages={'blank': 'You must give your Study Group a name!', 'max_length': 'The name of your Study Group cannot be more than 20 characters'})
	manager = models.ForeignKey('auth.User')
	location = models.ForeignKey(Location)
	course_code = models.CharField(max_length=15, validators = [RegexValidator(regex='^[a-zA-Z]* [0-9]{2,3}[a-zA-Z]{0,2}$', message='Improper Course Code Format! (EX: INFO 344, PHYS 444H)')], error_messages={'blank': 'You must enter a course number'})
	description = models.CharField(max_length=500, error_messages={'blank': 'You must enter a description!', 'max_length': 'Your description is too long! Pleaseenter a description that is 500 characters or less.'})
	start_time = models.DateTimeField(default=datetime.datetime.now, error_messages={'blank': 'You must enter a starting date and time', 'invalid_choice': 'The date and time you entered is invalid. Please check your input and try again. If you are using the API, the proper format is YYY-MM-DD HH:MM:SS'})
	end_time = models.DateTimeField(error_messages={'blank': 'You must enter an ending date and time', 'invalid_choice': 'The date and time you entered is invalid. Please check your input and try again. If you are using the API, the proper format is YYY-MM-DD HH:MM:SS'})

class UserInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100, blank=True, validators = [RegexValidator(regex='^[a-zA-Z]*$', message='Please enter a valid name (only letters)')], error_messages={'max_length': 'The name you entered is too long! Please enter a name that is less than 100 characters.'})
	last_name = models.CharField(max_length=100, blank=True, validators = [RegexValidator(regex='^[a-zA-Z]*$', message='Please enter a valid name (only letters)')], error_messages={'max_length': 'The name you entered is too long! Please enter a name that is less than 100 characters.'})
	phone_number = models.CharField(blank=True, max_length=14, validators = [RegexValidator(regex='^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$', message="Please enter a valid phone number in the format of '(###) ###-####'.")], error_messages={'max_length': 'Invalid phone number! Please enter in the format of (###) ###-####'})
	facebook_link = models.CharField(max_length=300, blank=True, validators = [RegexValidator(regex='^https:\/\/www\.facebook\.com\/.+$', message='Please enter a valid facebook profile link \"https://www.facebook.com/...\"')], error_messages={'max_length': 'Please use a link that is less than 300 characters long.'})
	bio = models.CharField(max_length=500, blank=True, error_messages={'max_length': 'Your about section is too long! Please do not exceed 500 characters'})
	profile_pic = models.ImageField(upload_to='images', blank=True, null=True, error_messages={'invalid': 'Invalid profile picture! You may only upload image files.'})
	email_public = models.CharField(max_length=200, blank=True, validators = [EmailValidator(message='Please enter a valid email!')], error_messages={'max_length' : 'Your email is too long! Please enter an email that has 200 characters or less.'})
	year = models.CharField(max_length=20, blank=True, error_messages = {'max_length': 'Please enter a valid year (Freshmen, Sophmore, Junior, Senior, Beyond Senior'})
	major = models.CharField(max_length=50, blank=True, error_messages = {'max_length': 'The major you entered is invalid! Please enter a major that does not exceed 50 characters'})	
	minor = models.CharField(max_length=50, blank=True, error_messages = {'max_length': 'The minor you entered is invalid! Please enter a major that does not exceed 50 characters'})	
	ideal_study_group = models.CharField(max_length=1000, blank=True, error_messages = {'max_length': 'The ideal study group section is too long! Please do not exceed 1000 characters.'})
	def get_absolute_url(self):
		return reverse('index')

