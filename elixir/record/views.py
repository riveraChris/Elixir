from django.http import *
from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from patient.models import Record

class RecordDetailView(DetailView):
    model = Record


class RecordCreateView(SuccessMessageMixin, CreateView):
    model = Record
    fields = ['medical_plan_name', 'medical_plan_number', 'height', 'weight', 'condition_1','condition_2','condition_3','more_info','created_By','created_DT']
    success_message = 'Record successfully created.'
    success_url = reverse_lazy('dash')


class RecordUpdateView(SuccessMessageMixin, UpdateView):
    model = Record
    fields = ['medical_plan_name', 'medical_plan_number', 'height', 'weight', 'condition_1','condition_2','condition_3','more_info','created_By','created_DT']
    success_message = 'The record is updated.'
    success_url = reverse_lazy('dash')


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('dash')



#def new_patient(request):
#	if not request.user.is_authenticated():
#		return redirect("/login")
#if request.user.type == 'professor':
#	return redirect('/dashboard')
#	return render_to_response('../templates/patient/new_patient.html', context_instance=RequestContext(request))
