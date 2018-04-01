from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
# 写的真丑，有空改改

def index(request):
	"""主页面的视图"""
	bg = random.randint(1,3)
	page = int(request.GET.get('page',1))
	if request.user.is_authenticated():
		username = request.user.username
		user = request.user
		# 关注人的文章
		follow_post_list = Post.objects.raw('''select * from main_post where user_id in (
												select follow_id from yonghu_follow where fan_id = %s)
												union
												select * from main_post where user_id = %s
												order by (-pub_date)
											'''%(user.id, user.id))
		follow_post_list = list(follow_post_list)
		paginator2 = Paginator(follow_post_list, 5)
		try:
			follow_posts = paginator2.page(page)
		except PageNotAnInteger:
			follow_posts = paginator2.page(1)
		except EmptyPage:
			follow_posts = paginator2.page(paginator2.num_pages)
	# 所有人的文章
	post_list = Post.objects.all().order_by('-pub_date')
	paginator = Paginator(post_list, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages
	return render(request, 'index.html', locals())

@login_required(login_url='/transfer/')
def write(request):
	"""撰写文章的视图"""
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
		if request.method == 'POST':
			post = Post(user=user)
			post_form = PostForm(request.POST, instance=post)
			if post_form.is_valid():
				post_form.save()
				post.photo1 = request.FILES.get('photo1')
				post.photo2 = request.FILES.get('photo2')
				post.photo3 = request.FILES.get('photo3')
				post.save()
				messages.info(request, '发布成功')
				return redirect('/')
			else:
				messages.info(request, '输入内容有误')
		else:
			post_form = PostForm()
			messages.get_messages(request)
			return render(request, 'main/write.html', locals())

def posts(request, post_id):
	"""博客文章的详情页面,包括评论功能"""
	post = Post.objects.get(pk=post_id)
	if request.user.is_authenticated():   #登录了才有评论功能
		username = request.user.username
		user = User.objects.get(username=username)
		if request.method == 'POST':
			comment_form = CommentForm(request.POST)
			if comment_form.is_valid():
				comment = Comment(user=user, post=post, body=request.POST['body'])
				comment.save()
				messages.info(request, '评论已提交')
				return redirect('main:post', post_id=post.id)
			else:
				messages.info(request, '内容有问题')
		else:
			comment_form = CommentForm()

	comments_list = Comment.objects.filter(post=post).order_by('pub_date')
	paginator = Paginator(comments_list, 5)
	page = int(request.GET.get('page',1))
	try:
		comments = paginator.page(page)
	except PageNotAnInteger:
		comments = paginator.page(1)
	except EmptyPage:
		comments = paginator.page(paginator.num_pages)

	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages

	messages.get_messages(request)
	return render(request, 'main/post.html', locals())

def page_not_found(request):
	return render(request, '404.html')

def user_post(request,user_id):
	post_user = get_object_or_404(User, id=user_id)
	post_list = Post.objects.filter(user=post_user).order_by('-pub_date')
	paginator = Paginator(post_list, 5)
	page = int(request.GET.get('page',1))
	if request.user.is_authenticated():					# 目的是弄出右上角的个人选项，如果不用username的话，未登录的人在模板里的user是anonymous
		username = request.user.username
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages

	return render(request, 'main/all_posts.html', locals())

def user_comment(request,user_id):
	comment_user = get_object_or_404(User, id=user_id)
	comment_list = Comment.objects.filter(user=comment_user).order_by('-pub_date')
	paginator = Paginator(comment_list, 5)
	page = int(request.GET.get('page',1))
	if request.user.is_authenticated():
		username = request.user.username
	try:
		comments = paginator.page(page)
	except PageNotAnInteger: 
		comments = paginator.page(1)
	except EmptyPage:
		comments = paginator.page(paginator.num_pages)
	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages

	return render(request, 'main/all_comments.html', locals())