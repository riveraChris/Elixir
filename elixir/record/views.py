from django.http import *
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from django.shortcuts import get_object_or_404

from patient.models import Record, Patient

class RecordSearchView(ListView):
    template_name = 'record/record_view.html'
    model = Patient
    
   # def get_queryset(self, *args, **kwargs):
    #    qs = super(RecordSearchView, self).get_queryset(*args, **kwargs)
     #   query = self.request.GET.get("q")
      #  if query:
       #     qs = self.model.objects.filter(Q(name__icontains = query))

        #return qs

    #def get_context_data(self, *args, **kwargs):
     #   context = super(RecordSearchView, self).get_queryset(*args, **kwargs)
        # context["query"] = self.request.GET.get("q")
         #return context
class RecordDetailView(DetailView):
    model = Record
    template_name = 'record/record_detail.html'
    context_object_name = 'record'


class RecordCreateView(SuccessMessageMixin, CreateView):
    model = Record
    fields = ['medical_plan_name', 'medical_plan_number', 'height', 'weight', 'condition_1','condition_2','condition_3','more_info','created_By','created_DT']
    success_message = 'Record successfully created.'
    success_url = reverse_lazy('dash')


class RecordUpdateView(SuccessMessageMixin, UpdateView):
    model = Record
    context_object_name = 'record'
    template_name = 'record/record_update.html'
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
