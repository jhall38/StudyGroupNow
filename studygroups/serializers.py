from django.contrib.auth.models import User, Group
from .models import StudyGroup, UserInfo, Location
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')
class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ('id', 'name', 'address', 'lat', 'lon')
class LocationCreateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ('name', 'address')

class StudyGroupSerializer(serializers.HyperlinkedModelSerializer):
	manager = UserSerializer()
	location = LocationSerializer()
	class Meta:
		model = StudyGroup
		fields = ('id', 'name', 'manager', 'location', 'course_code', 'description', 'start_time', 'end_time')	
class StudyGroupCreateSerializer(serializers.HyperlinkedModelSerializer):
	location_id = serializers.IntegerField()
	class Meta:
		model = StudyGroup
		fields = ('name', 'course_code', 'description', 'start_time', 'end_time', 'location_id')
class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
		model = UserInfo
		fields = ('id', 'user', 'first_name', 'last_name', 'email_public', 'phone_number', 'facebook_link', 'bio', 'profile_pic', 'year', 'major', 'minor', 'ideal_study_group')   
class UserInfoUpdateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserInfo
		fields = ('first_name', 'last_name', 'email_public', 'phone_number', 'facebook_link', 'bio', 'year', 'major', 'minor', 'ideal_study_group')
