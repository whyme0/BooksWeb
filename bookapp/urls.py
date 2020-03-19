from django.urls import path

from . import views

app_name = 'bookapp'
urlpatterns = [
	path('', views.HomePage.as_view(), name='index'),
	path('books/', views.BooksView.as_view(), name='books'),
	path('books/<int:pk>', views.particular_book, name='particular_book'),
	path('authors/', views.AuthorsView.as_view(), name='authors'),	
	path('authors/<int:pk>', views.particular_author, name='particular_author'),
	path('profile/', views.profile, name='profile'),
]
