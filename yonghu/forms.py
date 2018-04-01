from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['nickname', 'age', 'is_boy', 'note', 'head_cut']

	def __init__(self, *args, **kw):
		super(ProfileForm, self).__init__(*args, **kw)

		self.fields['nickname'].label = '昵称'
		self.fields['age'].label = '年龄'
		self.fields['is_boy'].label = '是男生吗'
		self.fields['note'].label = '个人宣言'
		self.fields['head_cut'].label = '请上传头像(尺寸50*50为佳)'