from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': r'e:\django_work\javascripts\tinymce\jscripts\tiny_mce'}),
    url(r'^search/$', 'cms.search.views.search'),
    url(r'^weblog/categories/', include('coltrane.urls.categories')),
    url(r'^weblog/links/', include('coltrane.urls.links')),
    url(r'^weblog/tags/', include('coltrane.urls.tags')),
    url(r'^weblog/', include('coltrane.urls.entries')),
    #url(r'', include('django.contrib.flatpages.urls')),
)
