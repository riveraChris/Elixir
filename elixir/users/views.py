from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from appointment.models import Appointment
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django_filters import FilterSet, CharFilter
from django.shortcuts import get_object_or_404

import datetime
from django.utils.timezone import utc

def app_search(request):
 	if not request.user.is_authenticated():
		return redirect("/login")

	return render_to_response('../templates/appointment/appointment_search.html', context_instance=RequestContext(request))

def app_menu(request):
 	if not request.user.is_authenticated():
		return redirect("/login")

	return render_to_response('../templates/appointment/appointment_menu.html', context_instance=RequestContext(request))

def record_search(request):
 	if not request.user.is_authenticated():
		return redirect("/login")

	return render_to_response('../templates/record/record_search.html', context_instance=RequestContext(request))

def record_menu(request):
 	if not request.user.is_authenticated():
		return redirect("/login")

	return render_to_response('../templates/record/record_menu.html', context_instance=RequestContext(request))


def hipaa(request):
 	if not request.user.is_authenticated():
		return redirect("/login")

	return render_to_response('../templates/users/hipaa.html', context_instance=RequestContext(request))

class MenuAppView(ListView):
	now = datetime.date.today()
	model = Appointment
	template_name = '../templates/users/menu.html'
	queryset = Appointment.objects.filter(
		time__year = now.year,
		time__month = now.month,
		time__day = now.day
		)

