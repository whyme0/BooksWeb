from django.shortcuts import render, get_object_or_404
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


def particular_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	context = {
		'book': book
	}
	return render(request, 'bookapp/book_info.html', context)
