import random
from django.db import models
from django.contrib.auth.models import User

class Follow(models.Model):
	follow = models.ForeignKey(User, related_name="follow_user")
	fan = models.ForeignKey(User, related_name="fan_user")
	
	def __str__(self):
		return "follow:{},fan:{}".format(self.follow,self.fan)

	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nickname = models.CharField(max_length=10, blank=True)
	age = models.IntegerField(null=True, blank=True)
	is_boy = models.NullBooleanField(null=True, blank=True)
	note = models.TextField(null=True, blank=True)
	head_cut = models.ImageField(default='/media/head_cuts/default.jpg' ,upload_to='head_cuts')

	def follow(self, User):
		f = Follow(follow=self.user, fan=User)			# 这四个函数是面向登录用户User而不是self的，
		f.save()										# 如follow_him是让User关注self

	def unfollow(self, User):
		f = Follow.objects.get(follow=self.user, fan=User)
		f.delete()

	def is_follow_him(self, User):
		f = Follow.objects.filter(follow=self.user, fan=User)
		return len(f) is not 0

	def is_him_my_fan(self, User):
		f = Follow.objects.filter(follow=User, fan=self.user)
		return len(f) is not 0

	def __str__(self):
		return self.user.username

# 增加测试用户
def add_robot(x,y):
	for i in range(x,y):
		name = 'robot%s' %i
		robot = User(username=name, password='cat', is_active=1)
		robot.save()
		robot_profile = Profile(user=robot,nickname=robot.username)
		robot_profile.save()
		print(robot)

def make_relation(x):
	for i in range(x):
		all_user = User.objects.all()
		user1 = all_user[random.randint(0,len(all_user)-1)]
		user2 = all_user[random.randint(0,len(all_user)-1)]
		if user1 != user2:
			f = Follow.objects.filter(follow=user1, fan=user2).first()
			if f is not None:
				print('已存在')
			else:
				f = Follow(follow=user1, fan=user2)
				f.save()
				print(f)

