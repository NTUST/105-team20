from django.conf.urls import url
from django.contrib import admin
from tubebook_main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', firstindex),
    url(r'^(\d{1,3})/$', index),
    url(r'^post/(\d{1,3})/$', post),
    url(r'^about/$', about),
    url(r'^author/$', authorList),
    url(r'^author/(\d{1,3})/$', authorProfile),
    url(r'^tag/(\d{1,3})/(\d{1,3})/$', postListByTag),
    url(r'^author/(\d{1,3})/(\d{1,3})/$', postListByAuthor)
]
