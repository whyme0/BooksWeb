from django.urls import path

from . import views

app_name = 'bookapp'
urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.books, name='books'),
	path('autors/', views.autors, name='autor'),
]
