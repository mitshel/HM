from django.conf.urls import include, url
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^login/$',login,{"template_name":"registration/login.html"}),
    url(r'^logout/$',logout,{"template_name":"registration/logout.html"}),
]
