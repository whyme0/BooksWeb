from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'authapp'
urlpatterns = [
	path('registration/', views.registration, name='registration'),
]

urlpatterns += [
	path('login/',
		 views.LoginView.as_view(),
		 name='login')
]
urlpatterns += [
	path('logout/',
		 auth_views.LogoutView.as_view(template_name='authapp/logout.html'),
		 name='logout')
]