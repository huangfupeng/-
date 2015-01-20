# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('origingroup.download',
    # Examples:
    url(r'^$', 'api.home'),
    url(r'^(?P<file_type>\w+)/$', 'api.home'),
    # url(r'^(?P<jobs_type>\w+)/(?P<company_id>\d+)/$', 'api.home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)