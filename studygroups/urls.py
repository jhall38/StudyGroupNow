from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^search/$', views.search_studygroups),
	url(r'^load_courses/$', views.load_courses),
	url(r'^add_or_edit/$', views.add_or_edit, name="add_or_edit"),
	url(r'^add_or_edit/submit/$', views.submit_add_edit, name="submit_add_edit"),
	url(r'^manage/$', views.manage, name="manage"),
	url(r'^manage/delete/$', views.delete, name="delete"),
	url(r'^load_locations/$', views.load_locations),
	url(r'^add_or_edit/new_location/$', views.new_location),
]
