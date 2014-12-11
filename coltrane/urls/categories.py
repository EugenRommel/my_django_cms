from django.conf.urls import patterns, url
from coltrane.views import CategoryListView, CategoryDetailView

urlpatterns = patterns('',
                       url(r'^$', CategoryListView.as_view(), name='coltrane_category_list'),
                       url(r'^(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='coltrane_category_details'),
                       )