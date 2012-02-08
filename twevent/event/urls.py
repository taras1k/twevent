from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^create$', 'event.views.create', name='create_event'),
    url(r'^attend/(?P<event_id>\w+)$', 'event.views.attend_event', name='attend_event'),
    url(r'^(?P<event_id>\w+)$', 'event.views.view_event', name='view_event'),    
    
    )
