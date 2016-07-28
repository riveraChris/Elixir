from django.conf.urls import patterns, include, url

from users import views
from users.views import MenuAppView

urlpatterns = [
	url(r'^menu/$', MenuAppView.as_view(), name='menu'),
	url(r'^app_search/$', 'users.views.app_search', name='app_search'),
	url(r'^app_menu/$', 'users.views.app_menu', name='app_menu'),
	url(r'^record_search/$', 'users.views.record_search', name='record_search'),
	url(r'^record_menu/$', 'users.views.record_menu', name='record_menu'),
	url(r'^hipaa/$', 'users.views.hipaa', name='hipaa'),
	url(r'^accounts/', include('registration.backends.default.urls')),

   	
]