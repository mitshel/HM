from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('hm_auth.urls')),
    url(r'^photo/',include('photogal.urls')),
    url(r'^',include('photogal.urls')),
]
