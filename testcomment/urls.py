from django.conf.urls import url
from django.contrib import admin
from appcoment.views import index, newcabspk, postcoments, post_update, postaddrows

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^postaddrows/', postaddrows),
    url(r'^newcabspk/(?P<pk>[0-9]+)/$', newcabspk),
    url(r'^postcoments/(?P<pk>[0-9]+)/$', postcoments),
    url(r'^(?P<pk>[0-9]+)/update/$', post_update),

]
