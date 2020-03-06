from django.urls import path, include

from . import views

app_name = 'authapp'
urlpatterns = [
	path('registration/', views.registration, name='registration'),
	path('', include('django.contrib.auth.urls')),
]
