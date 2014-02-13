from django.conf.urls import patterns, include, url

from api.view import task_router

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include(task_router._urls)),
    url(r'^admin/', include(admin.site.urls)),
)
