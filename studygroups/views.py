from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.template import Template, RequestContext
#from django.core.context_processors import csrf
from .models import StudyGroup, UserInfo, Location
from django.contrib.auth.decorators import login_required
import datetime

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
def add(request):
	return render(request, 'studygroups/addedit.html')
def edit(request):
	return render(request, 'studygroups/addedit.html')
def manage(request):
	return render(request, 'studygroups/manage.html')

def add_or_edit(request):
	return render(request, 'studygroups/add_or_edit.html')

def submit_add_edit(request):
	if not StudyGroup.objects.filter(manager=request.user).exists():
		studygroup = StudyGroup()
	else:
		studygroup = StudyGroup.objects.filter(manager=request.user)[0]

	studygroup.course = request.POST['course']
	studygroup.location = Location.objects.filter(name = request.POST['location'])[0]
	studygroup.location_desc = request.POST['description']
	studygroup.location_desc = request.POST['description']
	print(request.POST['enddate'])
	studygroup.end_time = request.POST['enddate'] + ' ' + request.POST['endtime']
	studygroup.manager = request.user
	studygroup.save()
	return render(request, 'studygroups/manage.html')
def load_locations(request):
	locations = Location.objects.values_list('name', flat=True)
	return render(request, 'studygroups/locations.html', {'locations' : locations})
def new_location(request):
	if request.method == "POST":
		location = Location()
		location.name = request.POST['new_location_name']
		location.address = request.POST['new_location_address']
		location.save()
	locations = Location.objects.values_list('name', flat=True)
	return render(request, 'studygroups/locations.html', {'locations' : locations})
	
