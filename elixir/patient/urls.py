
from django.conf.urls import url

from .views import PatientListView, PatientCreateView
from record import views
from record.views import RecordUpdateView

urlpatterns = [
	url(r'^new_patient/$', PatientCreateView.as_view(), name='new_patient'),
	url(r'^/(?P<pk>[0-9]+)$', RecordUpdateView.as_view(), name='update_record'),
	url(r'^list/$', PatientListView.as_view(), name='patient_list'),
]