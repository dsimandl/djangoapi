from django.conf.urls import patterns, url

from view import task_list, task_detail

urlpatterns = patterns(
    'api.view',
    url(r'^tasks/$', task_list, name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', task_detail, name='task_detail'),
)