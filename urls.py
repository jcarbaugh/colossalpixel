from django.conf.urls.defaults import *

# from django.contrib import admin
# admin.autodiscover()

application = webapp.WSGIApplication([('/', MainHandler),
                                      ('/([0-9a-fA-F]{3}|[0-9a-fA-F]{6})/?', RGBHandler),
                                      ('/png/([0-9a-fA-F]{3}|[0-9a-fA-F]{6})/?', PNGHandler),
                                      ('/(.*)', NotAColorHandler)], debug=True)

urlpatterns = patterns('',
    url(r'^png/(?P<rgb>[0-9a-fA-F]{3}|[0-9a-fA-F]{6})/$', 'colossalpixel.views.png', name='png'),
    url(r'^(?P<rgb>[0-9a-fA-F]{3}|[0-9a-fA-F]{6})/$', 'colossalpixel.views.rgb', name='rgb'),
    url(r'^$', 'colossalpixel.views.index', name='index'),
    url(r'^(?P<rgb>.*)', 'colossalpixel.views.notacolor', name='notacolor'),
    # url(r'^admin/', include(admin.site.urls)),
)
