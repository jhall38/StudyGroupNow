from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Location(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=500)
	lat = models.FloatField()
	lon = models.FloatField()

class StudyGroup(models.Model):
	manager = models.ForeignKey('auth.User')
	location = models.ForeignKey(Location)
	course_code = models.CharField(max_length=15)
	description = models.CharField(max_length=500)
	location_desc = models.CharField(max_length=500)
	start_time = models.DateTimeField(auto_now_add=True)
	end_time = models.DateTimeField()

class UserInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=20, blank=True)
	facebook_link = models.CharField(max_length=200, blank=True)
	bio = models.CharField(max_length=200, blank=True)
	profile_pic = models.FileField()
	email_public = models.CharField(max_length=200, blank=True)
	def get_absolute_url(self):
		return reverse('index')

