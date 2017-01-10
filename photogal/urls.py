from django.conf.urls import url
from photogal import views

urlpatterns = [
               url(r'^album/(\d+)/(\d+)/$', views.show_album),
               url(r'^album/(\d+)/$', views.show_album),
               url(r'^album/$', views.hello),
               url(r'^copy/(\d+)/$', views.copy_photo),
               url(r'^settings/(\d+)/$', views.settings_photo),
               url(r'^info/(\d+)/$', views.info_photo),
               url(r'^insta/(\d+)/$', views.insta_photo),
               url(r'^insta_upload/(\d+)/$', views.insta_upload),
               url(r'^collect/(\d+)/$', views.show_collection),
               url(r'^collect/dl/(\d+)/$', views.download_collection),
               url(r'^collect/copy/(\d+)/$', views.copy_collection),
               url(r'^collect/del/(\d+)/(\d+)/$', views.del_collection_photo),
               url(r'^collect/settings/(\d+)/$', views.settings_collection),
               url(r'^collect/clear/(\d+)/$', views.clear_collection),
               url(r'^collect/guest/(\w+)/$', views.guest_collection),
               url(r'^collect/guest/dl/(\w+)/$', views.guest_download_collection),
               url(r'^updateselect/(\d+)/(\d+)/$', views.updateselect),
               url(r'^', views.hello),
               ]