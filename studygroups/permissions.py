from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnlyStudyGroup(BasePermission):
	message = 'You must be the owner of this studygroup to edit or delete it'
	def has_object_permission(self, request, view, obj):
		return obj.manager == request.user
class IsOwnerOrReadOnlyUserInfo(BasePermission):
	message = 'You cannot edit a profile that is not yours'
	def has_object_permission(self, request, view, obj):
		return obj.user == request.user

