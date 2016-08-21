from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.template import Template, RequestContext
from .models import StudyGroup, UserInfo, Location
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django import forms
from ratelimit.decorators import ratelimit
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from .forms import UserForm
import geopy
from django.core.exceptions import ValidationError
from geopy.geocoders import GoogleV3
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import UserSerializer, UserInfoSerializer, UserInfoUpdateSerializer, LocationSerializer, LocationCreateSerializer, StudyGroupSerializer, StudyGroupCreateSerializer
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)
from .permissions import IsOwnerOrReadOnlyStudyGroup, IsOwnerOrReadOnlyUserInfo

@login_required(login_url='login/')
def index(request):
	if not StudyGroup.objects.filter(manager=request.user).exists():
		return render(request, 'studygroups/index.html', {'active_studygroup' : False})
	else:
		return render(request, 'studygroups/index.html', {'active_studygroup' : True})

def search_studygroups(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
	studygroups = StudyGroup.objects.filter(course_code=search_text).filter(end_time__gte=datetime.now())	
	return render(request, 'studygroups/studygroups_search.html', {'studygroups' : studygroups})

def load_courses(request):
	course_codes = StudyGroup.objects.values_list('course_code', flat=True).distinct()
	return render(request, 'studygroups/course_codes.html', {'course_codes' : course_codes})
def manage(request, pk):
	studygroup = get_object_or_404(StudyGroup, pk=pk)
	return render(request, 'studygroups/manage.html', {'studygroup' : studygroup})
def active(request):
	active_groups = StudyGroup.objects.filter(manager=request.user)
	return render(request, 'studygroups/active.html', {'active_groups' : active_groups})
def add(request):
	return render(request, 'studygroups/add_or_edit.html')
def submit_add(request):
	studygroup = StudyGroup()
	submit_studygroup(request, studygroup)
	return HttpResponseRedirect('/active/manage/%s' % studygroup.pk)
def edit(request, pk):
	studygroup = get_object_or_404(StudyGroup, pk=pk)
	return render(request, 'studygroups/add_or_edit.html', {'studygroup' : studygroup})
def submit_edit(request, pk):
	studygroup = get_object_or_404(StudyGroup, pk=pk)
	submit_studygroup(request, studygroup)
	return HttpResponseRedirect('/active/manage/%s' % pk)
def load_locations(request):
	locations = Location.objects.values_list('name', flat=True)
	if StudyGroup.objects.filter(manager=request.user).exists():
		current_location = StudyGroup.objects.filter(manager=request.user)[0].location.name 
		return render(request, 'studygroups/locations.html', {'locations' : locations, 'current_location' : current_location})
	return render(request, 'studygroups/locations.html', {'locations' : locations})
def new_location(request):
	if request.method == "POST":
		location = Location()
		location.name = request.POST['new_location_name']
		geolocator = GoogleV3(api_key="AIzaSyBO2lWgBphsJzNOfFxsJHgtuJ9zQoE7zTU")
		geocoded = geolocator.geocode(request.POST['new_location_address'] + ' Seattle WA USA 98105')
		if geocoded.address == 'Seattle, WA 98105, USA':
			raise ValidationError(_('Address is invalid or does not exist. Remember this address should not inlcude city, state, country or zip code.'))
		location.lat = geocoded.latitude
		location.lon = geocoded.longitude
		location.address = geocoded.address
		location.full_clean()
		location.save()
	locations = Location.objects.values_list('name', flat=True)
	return render(request, 'studygroups/locations.html', {'locations' : locations})
def delete(request, pk):
	studygroup = get_object_or_404(StudyGroup, pk=pk)
	if studygroup.manager.pk is not request.user.pk:
		return HttpResponseForbidden()
	studygroup.delete()
	return HttpResponseRedirect('/active/')
def signup(request):
	return render(request, 'studygroups/signup.html')
def signup_submit(request):
	new_user = User()
	new_user.username = request.POST['username']
	new_user.password = request.POST['password']
	new_user.email = request.POST['email']
	new_user.save()
	return render(request, 'studygroups/edi_profile.html')
@login_required(login_url="login/")
def my_profile(request):
	return render(request, 'studygroups/profile.html', {'this_profile' : UserInfo.objects.filter(user=request.user)[0], 'is_this_user' : True})
def edit_profile(request):
	return render(request, 'studygroups/edit_profile.html')

@login_required(login_url='login/')
def profile(request, username):
	this_user = get_object_or_404(User, username=username)
	print(this_user.username)
	print(UserInfo.objects.filter(user__username=this_user.username))
	this_profile = get_object_or_404(UserInfo, user=this_user.id)
	return render(request, 'studygroups/profile.html', {'this_profile' : this_profile})

class UserFormView(View):
	form_class = UserForm
	template_name = 'studygroups/signup.html'
	
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		print(form)
		if form.is_valid():
			print("test")
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			profile = UserInfo()
			profile.user = user
			profile.email_public = user.email
			profile.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
		return render(request, self.template_name, {'form': form})

@login_required(login_url='login/')
def edit_profile(request):
	return render(request, 'studygroups/edit_profile.html', {'profile' : UserInfo.objects.filter(user=request.user)[0]})

def submit_edit_profile(request):
	profile = UserInfo.objects.filter(user=request.user)[0]
	profile.first_name = request.POST['first_name']
	profile.last_name = request.POST['last_name']
	profile.email_public = request.POST['email']
	profile.phone_number = request.POST['phone']
	if request.POST['year'] != "":
		profile.year = request.POST['year']
		if profile.year != "Freshman" and profile.year != "Sophmore" and profile.year != "Junior" and profile.year != "Senior" and profile.year != "Beyond Senior":
			raise ValidationError(_('Invalid year: Only "Freshman", "Sophmore", "Junior", "Senior", and "Beyond Senior" are valid options'))
	profile.major = request.POST['major']
	profile.minor = request.POST['minor']
	profile.bio = request.POST['about']
	profile.facebook_link = request.POST['facebook']
	profile.ideal_study_group = request.POST['ideal']
	if 'image' in request.FILES:
		profile.profile_pic = request.FILES['image']
	profile.full_clean()
	profile.save()
	return HttpResponseRedirect('/my_profile/')

def submit_studygroup(request, studygroup):
	print(request.POST['startdate'])
	print(datetime.strptime(request.POST['startdate'] + ' ' + request.POST['starttime'], '%Y-%m-%d %H:%M'))
	studygroup.name = request.POST['name']
	studygroup.course_code = request.POST['course']
	studygroup.location = Location.objects.filter(name = request.POST['location'])[0]
	studygroup.description = request.POST['description']
	print(request.POST['startdate'] + ' ' + request.POST['starttime'])
	if not 'now' in request.POST:
		studygroup.start_time = request.POST['startdate'] + ' ' + request.POST['starttime']
	studygroup.end_time = request.POST['enddate'] + ' ' + request.POST['endtime']
	if studygroup.end_time < studygroup.start_time: 
		raise ValidationError(_('Your end date is sooner than your start date!'))
	elif studygroup.start_time < str(datetime.now()):
		raise ValidationError(_('Your starting date is in the past. You are not a time traveler!'))
	elif (datetime.strptime(studygroup.end_time, '%Y-%m-%d %H:%M')-datetime.strptime(studygroup.start_time, '%Y-%m-%d %H:%M')).total_seconds() > 86400: 
		raise ValidationError(_('Your studygroup can not last for more than 24 hours'))
	studygroup.manager = request.user
	studygroup.full_clean()
	studygroup.save()

class StudyGroupListAPIView(ListAPIView):
	queryset = StudyGroup.objects.filter(end_time__gte=datetime.now())
	serializer_class = StudyGroupSerializer
	permission_classes = [IsAuthenticated]
	throttle_classes = (UserRateThrottle,)	

class StudyGroupDetailAPIView(RetrieveAPIView):
	queryset = StudyGroup.objects.filter(end_time__gte=datetime.now())
	serializer_class = StudyGroupSerializer	
	permission_classes = [AllowAny]
	throttle_classes = (UserRateThrottle,)	

class StudyGroupUpdateAPIView(RetrieveUpdateAPIView):
	queryset = StudyGroup.objects.filter(end_time__gte=datetime.now())
	serializer_class = StudyGroupCreateSerializer
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyStudyGroup]
	throttle_classes = (UserRateThrottle,)	
	def perform_update(self, serializer):
		serializer.save(manager=self.request.user)

class StudyGroupCreateAPIView(CreateAPIView):
	queryset = StudyGroup.objects.filter(end_time__gte=datetime.now())
	serializer_class = StudyGroupCreateSerializer	
	permission_classes = [IsAuthenticated]
	throttle_classes = (UserRateThrottle,)	
	def perform_create(self, serializer):
		if serializer.validated_data.get('end_time') < serializer.validated_data.get('start_time'): 
			raise ValidationError(_('Your end date is sooner than your start date!'))
		elif serializer.validated_data.get('start_time') < timezone.now():
			raise ValidationError(_('Your starting date is in the past. You are not a time traveler!'))
		elif (serializer.validated_data.get('end_time')-serializer.validated_data.get('start_time')).total_seconds() > 86400: 
			raise ValidationError(_('Your studygroup can not last for more than 24 hours'))
		if Location.objects.get(pk=serializer.validated_data.get('location_id')):			
			serializer.save(manager=self.request.user, location=Location.objects.get(pk=serializer.validated_data.get('location_id')))
		else:
			raise ValidationError(_('No Location of that id exists. Remember you must use the id of an existing location.'))	

class StudyGroupDeleteAPIView(DestroyAPIView):
	queryset = StudyGroup.objects.filter(end_time__gte=datetime.now())
	serializer_class = StudyGroupSerializer
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyStudyGroup]
	throttle_classes = (UserRateThrottle,)	

class LocationListAPIView(ListAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	permission_classes = [AllowAny]
	throttle_classes = (UserRateThrottle,)	

class LocationDetailAPIView(RetrieveAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	permission_classes = [IsAuthenticated]
	throttle_classes = (UserRateThrottle,)	

class LocationCreateAPIView(CreateAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationCreateSerializer
	permission_classes = [IsAuthenticated]
	throttle_classes = (UserRateThrottle,)	
	def perform_create(self, serializer):
		geolocator = GoogleV3(api_key="AIzaSyBO2lWgBphsJzNOfFxsJHgtuJ9zQoE7zTU")
		geocoded = geolocator.geocode(serializer.validated_data.get('address') + ' Seattle WA USA 98105')
		if geocoded.address == 'Seattle, WA 98105, USA':
			raise ValidationError(_('Address is invalid or does not exist. Remember this address should not inlcude city, state, country or zip code.'))
		serializer.save(address=geocoded.address, lat=geocoded.latitude, lon=geocoded.longitude)
class UserInfoDetailAPIView(RetrieveAPIView):
	queryset = UserInfo.objects.all()
	serializer_class = UserInfoSerializer
	permission_classes = [IsAuthenticated]
	throttle_classes = (UserRateThrottle,)
	lookup_field = 'user__username'
class UserInfoUpdateAPIView(RetrieveUpdateAPIView):
	queryset = UserInfo.objects.all()
	serializer_class = UserInfoUpdateSerializer
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyUserInfo]
	throttle_classes = (UserRateThrottle,)
	lookup_field = 'user__username'
