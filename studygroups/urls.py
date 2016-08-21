from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^search/$', views.search_studygroups),
	url(r'^load_courses/$', views.load_courses),
	url(r'^active/add/$', views.add, name="add"),
	url(r'^active/add/submit/$', views.submit_add, name="submit_add"),
	url(r'^active/edit/(?P<pk>[0-9]+)/$', views.edit, name="edit"),
	url(r'^active/edit/(?P<pk>[0-9]+)/submit$', views.submit_edit, name="submit_edit"),
	url(r'^active/$', views.active, name="active_groups"),
	url(r'^active/manage/(?P<pk>[0-9]+)/$', views.manage, name="manage"),
	url(r'^active/manage/(?P<pk>[0-9]+)/delete/$', views.delete, name="delete"),
	url(r'^load_locations/$', views.load_locations),
	url(r'^new_location/$', views.new_location),
	url(r'^signup/$', views.UserFormView.as_view(), name="signup"),
	url(r'^signup/submit/$', views.signup_submit, name="signup_submit"),
	url(r'^profile/(?P<username>[-\w\d]+)/$', views.profile, name='profile'),
	url(r'^my_profile/$', views.my_profile, name='my_profile'),
	url(r'^edit_profile/$', views.edit_profile, name="edit_profile"),
	url(r'^edit_profile/submit/$', views.submit_edit_profile, name="submit_edit_profile"),
]
