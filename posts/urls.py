__author__ = 'narendra'


from django.conf.urls import url
from posts.views import *

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<abc>\d+)/$', post_detail, name="detail"),
    url(r'^(?P<abc>\d+)/edit/$', post_update, name="update"),
    url(r'^(?P<abc>\d+)/delete/$', post_delete),
]