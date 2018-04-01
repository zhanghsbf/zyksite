from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def login(request):
	if request.method == "POST":
		user = authenticate(username=request.POST['username'],\
							password=request.POST['password'])
		if user is not None:
			if user.is_active:
				username = user.username
				auth.login(request, user)
				messages.info(request, '登录成功！')
				# 登录时判断用户是否有资料模型，没有则创建一个
				has_p = models.Profile.objects.filter(user=user).first()
				if has_p is None:
					cre_p = models.Profile(user=user,nickname=user.username)
					cre_p.save()
				return redirect('/')
			else:
				messages.info(request, '账号未激活，请去邮箱激活...')
		else:
			messages.warning(request, '账号不存在，或用户名/密码错误...')

	return render(request, 'yonghu/login.html')

@login_required(login_url='/transfer/')
def logout(request):
	auth.logout(request)
	messages.info(request, "成功注销...")
	return redirect('/')


# @login_required(login_url="/transfer/")
def profile(request, user_id):
	'''
		展示用户资料，关注取关用户，以及修改用户资料
	'''
	profile_user = get_object_or_404(User, pk=user_id)			# 拿到当前页面的用户对象
	follows = models.Follow.objects.filter(fan=profile_user)	# 当前页面用户关注数
	fans = models.Follow.objects.filter(follow=profile_user)	# 粉丝数

	try:
		profile = models.Profile.objects.get(user=profile_user)
	except:
		profile = models.Profile(user=profile_user)
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)	# 拿到数据库中的当前用户对象
		is_mine_profile = user == profile_user
		i_followed_him = profile.is_follow_him(user)
		he_is_my_fan = profile.is_him_my_fan(user)
		if request.method == 'POST':
			# 只有当前用户等于登录用户时模板才显示修改表单
			profile_form = forms.ProfileForm(request.POST, instance=profile)
			if profile_form.is_valid():
				profile_form.save()
				profile.head_cut = request.FILES.get('head_cut')						# 不知为何用ModelForm保存文件没用
				if profile.head_cut != None:
					profile.save()
			messages.info(request, '个人资料已储存')
			return redirect('yonghu:profile', user_id=user.id)
			# else:
			# 	messages.info(request, '资料全都要填')
		else:
			profile_form = forms.ProfileForm()
	messages.get_messages(request)
	print('当前的用户是：%s'%user)

	return render(request, 'yonghu/profile.html', locals())

@login_required(login_url='/transfer/')
def follow(request, user_id):
	if request.user.is_authenticated():
		username = request.user.username
		user_now = User.objects.get(username=username)
		user = User.objects.get(pk=user_id)
		user_profile = models.Profile.objects.get(user=user)
		user_profile.follow(user_now)
		messages.info(request, '关注成功')
		return redirect('yonghu:profile', user_id=user_id)

@login_required(login_url='/transfer/')
def unfollow(request, user_id):
	if request.user.is_authenticated():
		username = request.user.username
		user_now = User.objects.get(username=username)
		user = User.objects.get(pk=user_id)
		user_profile = models.Profile.objects.get(user=user)
		user_profile.unfollow(user_now)
		messages.info(request, '取消关注')
		return redirect('yonghu:profile', user_id=user_id)

# login_required提示页面
def login_required_transfer(request):
	return render(request, 'yonghu/login_required_transfer.html')


def follows_page(request, user_id):
	'''展示关注者的页面'''
	user = get_object_or_404(User, pk=user_id)
	follows_list = models.Follow.objects.filter(fan=user)
	paginator = Paginator(follows_list, 10)

	page = int(request.GET.get('page',1))
	try:
		follows = paginator.page(page)
	except PageNotAnInteger:
		follows = paginator.page(1)
	except EmptyPage:
		follows = paginator.page(paginator.num_pages)
		
	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages

	return render(request, 'yonghu/follows.html', locals())

def fans_page(request, user_id):
	'''展示粉丝的页面'''
	user = get_object_or_404(User, pk=user_id)
	fans_list = models.Follow.objects.filter(follow=user)
	paginator = Paginator(fans_list, 10)

	page = int(request.GET.get('page',1))
	try:
		fans = paginator.page(page)
	except PageNotAnInteger:
		fans = paginator.page(1)
	except EmptyPage:
		fans = paginator.page(paginator.num_pages)
	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages
	number = 5 * (page - 1)
	return render(request, 'yonghu/fans.html', locals())

