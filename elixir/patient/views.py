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
    context_object_name = 'patient'
    template_name = 'patient/patient_form.html'
    fields = ['name', 'mid_name', 'first_last_name', 'second_last_name', 'birthdate','age','sex','address1','address2','city','state','zipcode','phone', 'doctor']
    success_message = 'Patient successfully created.'

class PatientUpdateView(SuccessMessageMixin, UpdateView):
    model = Patient
    fields = ['name', 'mid_name', 'first_last_name', 'second_last_name', 'birthdate','age','sex','address1','address2','city','state','zipcode','phone']
    success_message = 'The new Patient is updated.'


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('dash')

