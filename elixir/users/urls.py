from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^dash/$', 'users.views.dash', name='dash'),
   	#url(r'^$', 'users.views.login_user', name='login'),
   	#url(r'^login/$', 'users.views.login_user', name='login'),

]