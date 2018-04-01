import random
from .generate_post_comment import post_generator, comment_generator
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	body = models.TextField()
	photo1 = models.ImageField(null=True, blank=True, upload_to='photo/%Y/%m/%d')
	photo2 = models.ImageField(null=True, blank=True, upload_to='photo/%Y/%m/%d')
	photo3 = models.ImageField(null=True, blank=True, upload_to='photo/%Y/%m/%d')
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	body = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "用户:{0}对文章{1}的评论".format(self.user.username, self.post.title)

def add_post(x):
	user_len = User.objects.all().count()
	for i in range(x):
		id1 = random.randint(0,user_len-1)
		user = User.objects.all()[id1]
		title = '测试文章from: %s' %user
		body = post_generator()
		post = Post(user=user, title=title, body=body)
		post.save()
		print(post)

def add_comment(x):
	user_len = User.objects.all().count()
	post_len = Post.objects.all().count()
	for i in range(x):
		id1 = random.randint(0,user_len-1)
		id2 = random.randint(0,post_len-1)
		user = User.objects.all()[id1]
		post = Post.objects.all()[id2]
		body = comment_generator()
		comment = Comment(user=user, post=post, body=body)
		comment.save()
		print(comment)