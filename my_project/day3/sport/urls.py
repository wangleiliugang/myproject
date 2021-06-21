from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views),
    url(r'^person/$', person_views),
]
