from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^write/', views.write, name='write'),
	url(r'^post/(?P<post_id>[0-9]+)/$', views.posts, name='post'),
	url(r'^userpost/(?P<user_id>[0-9]+)/$', views.user_post, name='user_post'),
	url(r'^usercomment/(?P<user_id>[0-9]+)/$', views.user_comment, name='user_comment'),
]