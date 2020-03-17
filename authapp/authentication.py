from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class UsernameOrEmailBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None):
		if '@' in username:
			kwargs = {'email': username}
		else:
			kwargs = {'username': username}
		try:
			user = get_user_model().objects.get(**kwargs)
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None
	

	def get_user(self, username_pk):
		try:
			return get_user_model().objects.get(pk=username_pk)
		except get_user_model().DoesNotExist:
			return None