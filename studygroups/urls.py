from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import (
	StudyGroupListAPIView,
	StudyGroupDetailAPIView,
	StudyGroupUpdateAPIView,
	StudyGroupDeleteAPIView,
	StudyGroupCreateAPIView,
	LocationListAPIView,
	LocationCreateAPIView,
	LocationDetailAPIView,
	UserInfoDetailAPIView,
	UserInfoUpdateAPIView
	)
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
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),	
	url(r'^api/studygroups/$', StudyGroupListAPIView.as_view(), name='api_list_studygroups'),
	url(r'^api/studygroups/add/$', StudyGroupCreateAPIView.as_view(), name='api_add_studygroup'),
	url(r'^api/studygroups/(?P<pk>[0-9]+)/$', StudyGroupDetailAPIView.as_view(), name='api_detail_studygroup'),
	url(r'^api/studygroups/(?P<pk>[0-9]+)/edit$', StudyGroupUpdateAPIView.as_view(), name='api_edit_studygroup'),
	url(r'^api/locations/$', LocationListAPIView.as_view(), name='api_list_locations'),
	url(r'^api/locations/add/$', LocationCreateAPIView.as_view(), name='api_add_location'),
	url(r'^api/locations/(?P<pk>[0-9]+)/$', LocationDetailAPIView.as_view(), name='api_detail_location'),	
	url(r'^api/profiles/(?P<user__username>[-\w\d]+)/$', UserInfoDetailAPIView.as_view(), name='api_detail_profile'),
	url(r'^api/profiles/(?P<user__username>[-\w\d]+)/edit$', UserInfoUpdateAPIView.as_view(), name='api_edit_profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
