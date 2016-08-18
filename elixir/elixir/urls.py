from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', include('users.urls')),
    url(r'^', include('appointment.urls')),
    url(r'^', include('patient.urls')),
    url(r'^', include('record.urls')),
    

    # Include the Django admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/menu'}, name='logout')
]