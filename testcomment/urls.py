"""testcomment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appcoment.views import newcabs, ComentListView, newcabspk, listing, lpost, show_genres, postcoments, post_update

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', newcabs),
    url(r'^newcabspk/(?P<pk>[0-9]+)/$', newcabspk),
    url(r'^postcoments/(?P<pk>[0-9]+)/$', postcoments),
    url(r'^lpost/(?P<pk>[0-9]+)/$', lpost),
    url(r'^coments/$', ComentListView.as_view()),
    url(r'^listing/$', listing),
    url(r'^genres/$', show_genres),
    url(r'^(?P<pk>[0-9]+)/update/$', post_update),

]
