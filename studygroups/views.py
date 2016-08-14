from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.template import Template, RequestContext
#from django.core.context_processors import csrf
from .models import StudyGroup, UserInfo
from django.contrib.auth.decorators import login_required

#class StudGroupListView(generic.ListView):
#	template_name = 'studygroups/index.html'
	
#	def get_queryset(self):
#		return StudyGroup.objects.all()

@login_required(login_url='/login/')
def index(request):
	return render(request, 'studygroups/index.html')

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

