from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.template import Template, RequestContext
#from django.core.context_processors import csrf
from .models import StudyGroup, UserInfo, Location, User
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm


#class StudGroupListView(generic.ListView):
#	template_name = 'studygroups/index.html'
	
#	def get_queryset(self):
#		return StudyGroup.objects.all()

@login_required(login_url='/login/')
def index(request):
	if not StudyGroup.objects.filter(manager=request.user).exists():
		return render(request, 'studygroups/index.html', {'active_studygroup' : False})
	else:
		print(request.user)
		print(StudyGroup.objects.filter(manager=request.user))
		return render(request, 'studygroups/index.html', {'active_studygroup' : True})

def search_studygroups(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
	studygroups = StudyGroup.objects.filter(course_code=search_text)
	
	return render(request, 'studygroups/studygroups_search.html', {'studygroups' : studygroups})

def load_courses(request):
	course_codes = StudyGroup.objects.values_list('course_code', flat=True).distinct()
	print(course_codes)
	return render(request, 'studygroups/course_codes.html', {'course_codes' : course_codes})
def manage(request):
	if StudyGroup.objects.filter(manager=request.user).exists():
		return render(request, 'studygroups/manage.html', {'studygroup' : StudyGroup.objects.filter(manager=request.user)[0], 'active_studygroup' : True})
	else:
		return render(request, 'studygroups/manage.html')

def add_or_edit(request):
	if StudyGroup.objects.filter(manager=request.user).exists():
		print("printyprint: " + StudyGroup.objects.filter(manager=request.user)[0].course_code)
		return render(request, 'studygroups/add_or_edit.html', {'studygroup': StudyGroup.objects.filter(manager=request.user)[0], 'active_studygroup': True})
	else:
		return render(request, 'studygroups/add_or_edit.html')

def submit_add_edit(request):
	if not StudyGroup.objects.filter(manager=request.user).exists():
		studygroup = StudyGroup()
	else:
		studygroup = StudyGroup.objects.filter(manager=request.user)[0]

	studygroup.course_code = request.POST['course']
	studygroup.location = Location.objects.filter(name = request.POST['location'])[0]
	studygroup.location_desc = request.POST['description']
	print(request.POST['enddate'])
	studygroup.end_time = request.POST['enddate'] + ' ' + request.POST['endtime']
	studygroup.manager = request.user
	studygroup.save()
	return render(request, 'studygroups/manage.html', {'studygroup': StudyGroup.objects.filter(manager=request.user)[0], 'active_studygroup': True})
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
		location.save()
	locations = Location.objects.values_list('name', flat=True)
	return render(request, 'studygroups/locations.html', {'locations' : locations})
def delete(request):
	if StudyGroup.objects.filter(manager=request.user).exists():
		StudyGroup.objects.filter(manager=request.user)[0].delete()
	return render(request, 'studygroups/index.html')
def signup(request):
	return render(request, 'studygroups/signup.html')
def signup_submit(request):
	new_user = User()
	new_user.username = request.POST['username']
	new_user.password = request.POST['password']
	new_user.email = request.POST['email']
	new_user.save()
	return render(request, 'studygroups/index.html')
#def register(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            new_user = form.save()
#            return HttpResponseRedirect("/books/")
#    else:
#        form = UserCreationForm()
#    return render(request, "registration/register.html", {
#        'form': form,
#    })

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
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
		return render(request, self.template_name, {'form': form})
