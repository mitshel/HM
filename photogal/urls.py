from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^album/(\d+)/(\d+)/$', 'photogal.views.show_album'),
                       url(r'^album/(\d+)/$', 'photogal.views.show_album'),
                       url(r'^album/$', 'photogal.views.hello'),
                       url(r'^copy/(\d+)/$', 'photogal.views.copy_photo'),
                       url(r'^collect/(\d+)/$', 'photogal.views.show_collection'),
                       url(r'^collect/dl/(\d+)/$', 'photogal.views.download_collection'),
                       url(r'^collect/copy/(\d+)/$', 'photogal.views.copy_collection'),
                       url(r'^collect/del/(\d+)/(\d+)/$', 'photogal.views.del_collection_photo'),
                       url(r'^collect/settings/(\d+)/$', 'photogal.views.settings_collection'),
                       url(r'^collect/clear/(\d+)/$', 'photogal.views.clear_collection'),
                       url(r'^updateselect/(\d+)/(\d+)/$', 'photogal.views.updateselect'),
                       url(r'^', 'photogal.views.hello'),
                       )