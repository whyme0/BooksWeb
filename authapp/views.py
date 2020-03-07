from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages

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
