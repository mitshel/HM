from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$','django.contrib.auth.views.login',{"template_name":"registration/login.html"}),
    url(r'^logout/$','django.contrib.auth.views.logout',{"template_name":"registration/logout.html"}),
]
