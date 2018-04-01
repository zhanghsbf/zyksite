from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'photo1', 'photo2', 'photo3']

	def __init__(self, *args, **kw):
		super(PostForm, self).__init__(*args, **kw)
		self.fields['title'].label = '标题'
		self.fields['body'].label = '正文'

class CommentForm(forms.Form):
	body = forms.CharField(label='评论内容', max_length=100)
	