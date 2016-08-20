from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.template import Template, RequestContext
#from django.core.context_processors import csrf
from .models import StudyGroup, UserInfo, Location
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django import forms
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from .forms import UserForm
#import geopy
#from geopy.geocoders import GoogleV3
from django.contrib.auth.forms import UserCreationForm


#class StudGroupListView(generic.ListView):
#	template_name = 'studygroups/index.html'
	
#	def get_queryset(self):
#		return StudyGroup.objects.all()

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
	studygroup.name = request.POST['name']
	studygroup.course_code = request.POST['course']
	studygroup.location = Location.objects.filter(name = request.POST['location'])[0]
	studygroup.description = request.POST['description']
	if not 'now' in request.POST:
		studygroup.start_time = request.POST['startdate'] + ' ' + request.POST['starttime']
	studygroup.end_time = request.POST['enddate'] + ' ' + request.POST['endtime']
	studygroup.manager = request.user
	studygroup.save()
	return HttpResponseRedirect('/active/manage/%s' % studygroup.pk)
def edit(request, pk):
	studygroup = get_object_or_404(StudyGroup, pk=pk)
	return render(request, 'studygroups/add_or_edit.html', {'studygroup' : studygroup})
def submit_edit(request, pk):
	studygroup = get_object_or_404(StudyGroup, pk=pk)
	studygroup.name = request.POST['name']	
	studygroup.course_code = request.POST['course']
	studygroup.location = Location.objects.filter(name = request.POST['location'])[0]
	studygroup.description = request.POST['description']
	studygroup.end_time = request.POST['enddate'] + ' ' + request.POST['endtime']
	studygroup.manager = request.user
	studygroup.save()
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
		location.address = request.POST['new_location_address']
	#	geolocator = GoogleV3(api_key="AIzaSyBO2lWgBphsJzNOfFxsJHgtuJ9zQoE7zTU")
	#	geocode = geolocator(request.POST['new_location_address'] + ' Seattle WA USA')
	#	location.lat = geocode.latitude
	#	location.lon = geocode.longitude
	#	location.save()
	#	print(location.address + ' ' location.lat + ' ' + location.lon + ' ' geocode.address
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
			profile.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
		return render(request, self.template_name, {'form': form})

@login_required(login_url='/login/')
def edit_profile(request):
	return render(request, 'studygroups/edit_profile.html', {'profile' : UserInfo.objects.filter(user=request.user)[0]})

def submit_edit_profile(request):
	profile = UserInfo.objects.filter(user=request.user)[0]
	profile.first_name = request.POST['first_name']
	profile.last_name = request.POST['last_name']
	profile.email_public = request.POST['email']
	profile.phone_number = request.POST['phone']
	profile.year = request.POST['year']
	profile.major = request.POST['major']
	profile.minor = request.POST['minor']
	profile.bio = request.POST['about']
	profile.facebook_link = request.POST['facebook']
	profile.ideal_study_group = request.POST['ideal']
	if 'image' in request.FILES:
		profile.profile_pic = request.FILES['image']
	profile.save()
	return HttpResponseRedirect('/my_profile/')
