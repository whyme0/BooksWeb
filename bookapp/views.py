from django.shortcuts import render
from django.views import generic
from .models import Autor, Book

def index(request):
	return render(request, 'bookapp/index.html')


def books(request):
	books_list = Book.objects.all()[:5]
	context = {
		'books_list': books_list
	}
	return render(request, 'bookapp/books.html', context)


def autors(request):
	return render(request, 'bookapp/autors.html')
