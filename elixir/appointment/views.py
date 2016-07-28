from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django_filters import FilterSet, NumberFilter
from .models import Appointment


class AppFilter(FilterSet):
    dd = NumberFilter(name='time', lookup_expr='day')
    mm = NumberFilter(name='time', lookup_expr='month')
    yy = NumberFilter(name='time', lookup_expr='year')
    class Meta:
        model = Appointment
        fields = [
            'dd',
            'mm',
            'yy',
         ]

def app_list(request):
  qs = Appointment.objects.all()
  ordering = request.GET.get("ordering")
  if ordering:
    qs = Appointment.objects.all().order_by(ordering)
  f =  AppFilter(request.GET, queryset = qs)
  return render(request, 'appointment/appointment_list.html', { "object_list": f })


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


class AppointmentListView(FilterMixin, ListView):
    model = Appointment
    template_name = 'appointment/appointment_list.html'
    queryset = Appointment.objects.all()
    filter_class = AppFilter

    
    def get_context_data(self, *args, **kwargs):
      context = super(AppointmentListView, self).get_context_data(*args, **kwargs)
      context["query"] = self.request.GET.get("q")
      return context
    
    def get_queryset(self, *args, **kwargs):
      qs = super(AppointmentListView, self).get_queryset(*args, **kwargs)
      query = self.request.GET.get("q")
      if query:
        qs = self.model.objects.filter(
          Q(time__icontains = query)
          )

      return qs
    


class AppointmentDetailView(DetailView):
    model = Appointment
    context_object_name = 'app'

class AppointmentCreateView(SuccessMessageMixin, CreateView):
    model = Appointment
    fields = ['record', 'phone_number', 'time', 'time_zone', 'treatment']
    success_message = 'Appointment successfully created.'


class AppointmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Appointment
    fields = ['record', 'phone_number', 'time', 'time_zone', 'treatment']
    success_message = 'Appointment successfully updated.'


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy('list_appointments')