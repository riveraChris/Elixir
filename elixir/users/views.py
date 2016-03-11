from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

#def login_user(request):
#	logout(request)
#	username = password = ''
#	if request.POST:
#		username = request.POST['username']
#		password = request.POST['password']
#
#		user = authenticate(username = username, password = password)
#
#		if user is not None:
#			if user.is_active:
#				login(request, user)
#				context = {"user":user}
#				return HttpResponseRedirect('../dash', context)
#			else:
#				print("The password is valid, but the account has been disabled!")
#		else:
#			print("The password is invalid")
#
#	return render_to_response('../templates/users/login.html', context_instance=RequestContext(request))

def dash(request):
 	if not request.user.is_authenticated():
		return redirect("/login")
	#if request.user.type == 'professor':
	#	return redirect('/dashboard')
	return render_to_response('../templates/users/dash.html', context_instance=RequestContext(request))
 
def menu(request):
	if not request.user.is_authenticated():
		return redirect("/login")
	#if request.user.type == 'professor':
	#	return redirect('/dashboard')
	return render_to_response('../templates/users/menu.html', context_instance=RequestContext(request))