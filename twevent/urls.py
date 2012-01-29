from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','event.views.default'),                   
    url(r'^login/?$', 'users.views.twitter_login'),
    url(r'^logout/?$', 'users.views.twitter_logout'),
    url(r'^login/authenticated/?$', 'users.views.twitter_authenticated'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    # Examples:
    # url(r'^$', 'twevent.views.home', name='home'),
    # url(r'^twevent/', include('twevent.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
