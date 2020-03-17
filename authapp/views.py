from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login
from .forms import LoginForm
from django.views.generic.edit import FormView
from .authentication import UsernameOrEmailBackend

def registration(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Вы успешно создали аккаунт {username}. Теперь войдите.')
			return redirect('authapp:login')
	else:
		form = UserRegistrationForm()

	return render(request, 'authapp/registration_form.html', {'form': form})


class LoginView(FormView):
	form_class = LoginForm
	template_name = 'authapp/login_form.html'
	success_url = '/'

	def form_valid(self, form):
		if form.is_valid():
			user = UsernameOrEmailBackend().authenticate(
				self.request,
				username=self.request.POST['username'],
				password=self.request.POST['password'],
			)

			login(self.request, user)
			return redirect('bookapp:profile')
