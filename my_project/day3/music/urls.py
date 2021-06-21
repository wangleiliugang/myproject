from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views),
    url(r'^show/$', show_views),
    url(r'^music_info/$', music_info_views),
]
