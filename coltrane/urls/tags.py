from django.conf.urls import patterns, url
from coltrane.views import TagListView
from coltrane.models import Entry, Link


urlpatterns = patterns('',
                       url(r'^$', TagListView.as_view(), name='coltrane_tag_list'),
                       url(r'^entries/(?P<tag>[-\w]+)/$', 'taggit.views.tagged_object_list',
                           {'queryset_or_model': Entry,
                            'template_name': 'coltrane/entries_by_tag.html'}),
                       url(r'^links/(?P<tag>[-\w]+)/$', 'taggit.views.tagged_object_list',
                           {'queryset_or_model': Link,
                            'template_name': 'coltrane/links_by_tag.html'}),
                       )