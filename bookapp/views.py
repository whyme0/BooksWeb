from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Autor, Book

def index(request):
	return render(request, 'bookapp/index.html', {'session': request.session})


def books(request):
	books_list = Book.objects.all()[:5]
	context = {
		'books_list': books_list
	}
	return render(request, 'bookapp/books.html', context)


def particular_book(request, pk):
	book = get_object_or_404(Book, pk=pk)

	# we need to get author of book for further transfer primary key to <a> href
	# attribute in book_info.html page at 14 line 
	book_author = Autor.objects.filter(author_full_name=book.book_autor_info).get()
	context = {
		'book': book,
		'book_author': book_author
	}
	return render(request, 'bookapp/book_info.html', context)


def authors(request):
	authors_list = Autor.objects.all()[:5]
	context = {
		'authors_list': authors_list
	}
	return render(request, 'bookapp/authors.html', context)


def particular_author(request, pk):
	author = get_object_or_404(Autor, pk=pk)
	if author is not None:
		author_books = Book.objects.filter(book_autor_info=author.author_full_name)
		context = {
			'author': author,
			'author_books': author_books
		}
	return render(request, 'bookapp/author_info.html', context)
	
