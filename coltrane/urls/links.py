from django.conf.urls import patterns, url
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView
from coltrane.models import Link

urlpatterns = patterns('',
                       url(r'^$', ArchiveIndexView.as_view(model=Link, date_field='pub_date'), name='coltrane_link_archive_index'),
                       url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(model=Link, make_object_list=True,
                                                                                date_field='pub_date')),
                       url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', MonthArchiveView.as_view(model=Link,
                                                                                                  date_field='pub_date')),
                       url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                           DayArchiveView.as_view(model=Link, date_field='pub_date')),
                       url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
                           DateDetailView.as_view(model=Link, date_field='pub_date'), name='coltrane_link_details'),
                       )