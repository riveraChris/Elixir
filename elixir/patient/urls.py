
from django.conf.urls import url

from .views import PatientListView, PatientCreateView
from record import views
from record.views import RecordUpdateView, RecordSearchView, RecordDetailView, CreateNoteView, NoteSearchView, NoteDetailView

urlpatterns = [
	url(r'^new_patient/$', PatientCreateView.as_view(), name='new_patient'),
	url(r'^update/(?P<pk>[0-9]+)/$', RecordUpdateView.as_view(), name='update_record'),
	url(r'^note/(?P<pk>[0-9]+)/$', CreateNoteView.as_view(), name='add_note'),
	url(r'^detail/(?P<pk>[0-9]+)/$', RecordDetailView.as_view(), name='detail_record'),
	#url(r'^view/$', 'record.views.record_list', name='view_record'),
	url(r'^view/$', RecordSearchView.as_view(), name='view_record'),
	url(r'^view_note/(?P<pk>[0-9]+)/$', NoteSearchView.as_view(), name='view_note'),
	url(r'^detail_note/(?P<pk>[0-9]+)/$', NoteDetailView.as_view(), name='detail_note'),
	#url(r'^list/$', PatientListView.as_view(), name='patient_list'),
]