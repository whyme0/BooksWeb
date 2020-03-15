from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'email', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		unique_together = ['email']


class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs.update({'placeholder': 'Ваш логин'})
		self.fields['password'].widget.attrs.update({'placeholder': 'Ваш пароль'})