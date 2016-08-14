from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import authenticate

def login(request):
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)

