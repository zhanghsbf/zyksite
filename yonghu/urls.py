from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name="profile"),
	url(r'^follow/(?P<user_id>[0-9]+)/$', views.follow, name="follow"),
	url(r'^unfollow/(?P<user_id>[0-9]+)/$', views.unfollow, name="unfollow"),
	url(r'^follows/(?P<user_id>[0-9]+)/$', views.follows_page, name="follows_page"),
	url(r'^fans/(?P<user_id>[0-9]+)/$', views.fans_page, name="fans_page"),
]