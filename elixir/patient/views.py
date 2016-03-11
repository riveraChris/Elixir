from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic.list import ListView

from .models import Patient

class PatientListView(ListView):

    model = Patient

def new_patient(request):
	if not request.user.is_authenticated():
		return redirect("/login")
#if request.user.type == 'professor':
#	return redirect('/dashboard')
	return render_to_response('../templates/patient/new_patient.html', context_instance=RequestContext(request))
