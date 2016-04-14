from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^dash/$', 'users.views.dash', name='dash'),
   	
]