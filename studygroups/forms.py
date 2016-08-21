from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	class Meta:
		model = User
		fields = {'email', 'username', 'password'}
		fields_order = ['username', 'email', 'password']
#class StudyGroupForm(forms.ModelForm):
#	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Studygroup'})
	
	
