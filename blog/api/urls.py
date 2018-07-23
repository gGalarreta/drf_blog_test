from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api import views

urlpatterns = [
    url(r'^posts/create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^posts/list/$', views.PostListView.as_view(), name='post_list'),
    url(r'^posts/(?P<pk>\d+)/detail/$', views.PostDetailView.as_view(), name="post_detail"),
    url(r'^posts/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(), name="post_update"),
    url(r'^posts/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name="post_delete"),
]

urlpatterns = format_suffix_patterns(urlpatterns)