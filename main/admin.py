from django.contrib import admin
from .models import Post, Comment



class CommentInline(admin.TabularInline):
	model = Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','user','pub_date')
	inlines = [
			CommentInline,
		]

class CommentAdmin(admin.ModelAdmin):
	list_display = ('post','user')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)