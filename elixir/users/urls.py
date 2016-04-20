from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^dash/$', 'users.views.dash', name='dash'),
	url(r'^menu/$', 'users.views.menu', name='menu'),

   	
]