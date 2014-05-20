from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('services.views',
    url(r'^api/service/$', 'service_list'),
    url(r'^api/service/(?P<pk>[0-9]+)/$', 'service_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
