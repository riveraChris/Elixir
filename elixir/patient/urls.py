
from django.conf.urls import url

from .views import PatientListView, PatientCreateView

urlpatterns = [
	url(r'^list/$', PatientListView.as_view(), name='patient_list'),
	url(r'^new_patient/$', PatientCreateView.as_view(), name='new_patient'),
]