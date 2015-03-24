from django.conf.urls import patterns, include, url 
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views


post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_creation = views.PostViewSet.as_view({
    'post': 'set_comment'
})


urlpatterns = patterns('api.views', 
   url(r'^v1/posts/$', post_list, name='post_list'), 
   url(r'^v1/post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'), 
   url(r'^v1/post/(?P<pk>[0-9]+)/comment/$', comment_creation, name='comment_creation'),
)


urlpatterns = format_suffix_patterns(urlpatterns)