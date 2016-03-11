
from django.conf.urls import url

from .views import PatientListView, new_patient

urlpatterns = [
	url(r'^list/$', PatientListView.as_view(), name='patient_list'),
	url(r'^new_patient/$', new_patient, name='new_patient'),
]