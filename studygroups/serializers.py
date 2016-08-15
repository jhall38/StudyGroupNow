from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')

class StudyGroupSerializer(serializers.HyperlinkedModelSerializer):
	manager = UserSerializer(many=True)
	class Meta:
		model = StudyGroup
		fields = ('id', 'manager', 'location', 'course_code', 'location_desc', 'start_time', 'end_time')	
