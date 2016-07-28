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

from patient.models import Record, Patient, Note

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


class NoteFilter(FilterSet):
  record = CharFilter(name='record', lookup_type= 'icontains')
  class Meta:
    model = Patient
    fields = [
      'record',
    ]

def note_list(request):
  qs = Note.objects.all()
  ordering = request.GET.get("ordering")
  if ordering:
    qs = Note.objects.all().order_by(ordering)
  f =  NoteFilter(request.GET, queryset = qs)
  return render(request, 'record/note_view.html', { "object_list": f })



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
    success_url = reverse_lazy('menu')


class CreateNoteView(CreateView):
    model = Note
    template_name = 'record/add_note.html'
    fields = ['received_Place','received_State','service_Food','returned_Type','diaper','evacuations','milk','snack', 'hygiene', 'comments']
    success_message = 'Note successfully created.'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
      form.instance.record = Record.objects.get(id = self.kwargs["pk"])
      form.save()
      return super(CreateNoteView, self).form_valid(form)


class NoteSearchView(FilterMixin, ListView):
    template_name = 'record/note_view.html'
    model = Note
    filter_class = NoteFilter

    
    def get_context_data(self, *args, **kwargs):
      context = super(NoteSearchView, self).get_context_data(*args, **kwargs)
      context["query"] = self.request.GET.get("q")
      context["record"] = self.kwargs["pk"]
      return context
    
    def get_queryset(self, *args, **kwargs):
      qs = super(NoteSearchView, self).get_queryset(*args, **kwargs)
      # query = self.request.GET.get("q")
      # if query:
      #   qs = self.model.objects.filter(
      #     Q(name__icontains = query)
      #     )
      record = Record.objects.get(id = self.kwargs["pk"])
      qs = Note.objects.filter(record = record)

      return qs

class NoteDetailView(DetailView):
    model = Note
    template_name = 'record/note_detail.html'
    context_object_name = 'note'
    
