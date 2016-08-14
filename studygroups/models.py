from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=500)

class StudyGroup(models.Model):
	name = models.CharField(max_length=100)
	manager = models.ForeignKey('auth.User')
	location = models.ForeignKey(Location)
	course_code = models.CharField(max_length=15)
	location_desc = models.CharField(max_length=500)
	stat_time = models.DateTimeField(auto_now_add=True)
	end_time = models.DateTimeField(blank=True)

class UserInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=20, blank=True)
	facebook_link = models.CharField(max_length=200, blank=True)
	nickname = models.CharField(max_length=50, blank=True)	


