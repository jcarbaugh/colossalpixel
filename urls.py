from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('colossalpixel.views',
    url(r'^(?P<rgb>[0-9a-fA-F]{3}|[0-9a-fA-F]{6}).png$', 'png', name='png'),
    url(r'^(?P<rgb>[0-9a-fA-F]{3}|[0-9a-fA-F]{6})/?$', 'rgb', name='rgb'),
    url(r'^$', 'index', name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.generic.simple',
        url(r'test/', 'direct_to_template', {'template': 'colossalpixel/test.html'})
    )

urlpatterns += patterns('colossalpixel.views',
    url(r'^(?P<rgb>.*)', 'notacolor', name='notacolor'),
)