from django.conf.urls import url
from django.contrib import admin
from tubebook_main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', firstindex),
    url(r'^(\d)/$', index),
    url(r'^post/(\d)/$', post),
    url(r'^about/$', about),
    url(r'^author/$', authorList),
    url(r'^author/(\d)/$', authorProfile),
    url(r'^tag/(\d)/(\d)/$', postListByTag),
    url(r'^author/(\d)/(\d)/$', postListByAuthor)
]
