from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^search/$', views.search_studygroups),
	url(r'^load_courses/$', views.load_courses),
	url(r'^add/$', views.add, name="add"),
	url(r'^manage/$', views.manage, name="manage"),
]
