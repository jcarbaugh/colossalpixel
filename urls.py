from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<rgb>[0-9a-fA-F]{3}|[0-9a-fA-F]{6}).png$', 'colossalpixel.views.png', name='png'),
    url(r'^(?P<rgb>[0-9a-fA-F]{3}|[0-9a-fA-F]{6})/$', 'colossalpixel.views.rgb', name='rgb'),
    url(r'^test/$', 'colossalpixel.views.test', name='test'),
    url(r'^$', 'colossalpixel.views.index', name='index'),
    url(r'^(?P<rgb>.*)', 'colossalpixel.views.notacolor', name='notacolor'),
)
