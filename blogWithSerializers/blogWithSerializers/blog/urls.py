
from django import views

from django.urls import path
from blog.views import PostViewSet
from rest_framework.urlpatterns import format_suffix_patterns

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_creation= PostViewSet.as_view({
    'post': 'set_comment'
})



urlpatterns = [
    path(r'^v1/posts/$', post_list, name='post_list'),
    path(r'^v1/post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'), 
    path(r'^v1/post/(?P<pk>[0-9]+)/comment/$', comment_creation, name='comment_creation')

]