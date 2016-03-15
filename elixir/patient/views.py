from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Patient


class PatientListView(ListView):

    model = Patient

class PatientDetailView(DetailView):
    model = Patient


class PatientCreateView(SuccessMessageMixin, CreateView):
    model = Patient
    fields = ['name', 'mid_name', 'first_last_name', 'second_last_name', 'birthdate','age','sex','address1','address2','city','state','zipcode','phone']
    success_message = 'Appointment successfully created.'
    success_url = reverse_lazy('new_patient')


class PatientUpdateView(SuccessMessageMixin, UpdateView):
    model = Patient
    fields = ['name', 'mid_name', 'first_last_name', 'second_last_name', 'birthdate','age','sex','address1','address2','city','state','zipcode','phone']
    success_message = 'The new Patient is created.'


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('list_appointments')



#def new_patient(request):
#	if not request.user.is_authenticated():
#		return redirect("/login")
#if request.user.type == 'professor':
#	return redirect('/dashboard')
#	return render_to_response('../templates/patient/new_patient.html', context_instance=RequestContext(request))
