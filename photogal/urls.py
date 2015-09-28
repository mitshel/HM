from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^album/(\d+)/(\d+)/$', 'photogal.views.show_page'),
                       url(r'^album/(\d+)/$', 'photogal.views.show_page'),
                       url(r'^album/$', 'photogal.views.show_page'),
                       url(r'^', 'photogal.views.hello'),
                       )