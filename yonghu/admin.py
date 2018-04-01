from django.contrib import admin
from .models import Profile, Follow
# Register your models here.

class FollowAdmin(admin.ModelAdmin):
	fields = ['follow', 'fan']
	list_display = ('follow', 'fan')
	list_filter = ['follow', 'fan']

admin.site.register(Follow, FollowAdmin)
admin.site.register(Profile)
