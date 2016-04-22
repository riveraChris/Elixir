from django.http import *
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from django_filters import FilterSet, CharFilter

from django.shortcuts import get_object_or_404

from patient.models import Record, Patient

class RecordFilter(FilterSet):
  name = CharFilter(name='name', lookup_type= 'icontains')
  lastname = CharFilter(name='first_last_name', lookup_type= 'icontains')
  class Meta:
    model = Patient
    fields = [
      'name',
      'lastname',
    ]

def record_list(request):
  qs = Patient.objects.all()
  ordering = request.GET.get("ordering")
  if ordering:
    qs = Patient.objects.all().order_by(ordering)
  f =  RecordFilter(request.GET, queryset = qs)
  return render(request, 'record/record_view.html', { "object_list": f })

class FilterMixin(object):
  filter_class = None
  search_ordering_param = "ordering"

  def get_queryset (self, *args, **kwargs):
    try:
      qs = super(FilterMixin, self).get_queryset(*args, **kwargs)
      return qs
    except:
      raise ImproperlyConfigured("You must have a queryset in order to use FilterMixin")

  def get_context_data(self, *args, **kwargs):
    context = super(FilterMixin, self).get_context_data(*args, **kwargs)
    qs = self.get_queryset()
    ordering = self.request.GET.get(self.search_ordering_param)
    if ordering:
      qs = qs.order_by(ordering)
    filter_class= self.filter_class
    if filter_class:
      f = filter_class(self.request.GET, queryset=qs)
      context["object_list"] = f
    return context


class RecordSearchView(FilterMixin, ListView):
    template_name = 'record/record_view.html'
    model = Patient
    queryset = Patient.objects.all()
    filter_class = RecordFilter

    
    def get_context_data(self, *args, **kwargs):
      context = super(RecordSearchView, self).get_context_data(*args, **kwargs)
      context["query"] = self.request.GET.get("q")
      return context
    
    def get_queryset(self, *args, **kwargs):
      qs = super(RecordSearchView, self).get_queryset(*args, **kwargs)
      query = self.request.GET.get("q")
      if query:
        qs = self.model.objects.filter(
          Q(name__icontains = query)
          )

      return qs

class RecordDetailView(DetailView):
    model = Record
    template_name = 'record/record_detail.html'
    context_object_name = 'record'


class RecordCreateView(SuccessMessageMixin, CreateView):
    model = Record
    fields = ['medical_plan_name', 'medical_plan_number', 'height', 'weight', 'condition_1','condition_2','condition_3','more_info','created_By','created_DT']
    success_message = 'Record successfully created.'
    success_url = reverse_lazy('menu')


class RecordUpdateView(SuccessMessageMixin, UpdateView):
    model = Record
    context_object_name = 'record'
    template_name = 'record/record_update.html'
    fields = ['medical_plan_name', 'medical_plan_number', 'height', 'weight', 'condition_1','condition_2','condition_3','more_info','created_By','created_DT']
    success_message = 'The record is updated.'
    success_url = reverse_lazy('menu')


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('dash')



#def new_patient(request):
#	if not request.user.is_authenticated():
#		return redirect("/login")
#if request.user.type == 'professor':
#	return redirect('/dashboard')
#	return render_to_response('../templates/patient/new_patient.html', context_instance=RequestContext(request))
