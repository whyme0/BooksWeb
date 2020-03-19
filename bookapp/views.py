from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Autor, Book

import datetime

class HomePage(TemplateView):
	template_name = 'bookapp/index.html'


class BooksView(ListView):
	model = Book
	paginate_by = 1
	context_object_name = 'books_list'
	template_name = 'bookapp/books.html'

	def get_queryset(self):
		search_context = self.request.GET.get('search', None)

		books = Book.objects.order_by('book_year')
		if search_context:
			# сейчас фильтр не учитывает кириллицу, поскольку используется sqlite
			books = Book.objects.filter(
				Q(book_name__icontains=search_context) |
				Q(book_description__icontains=search_context)
			)

		return books

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		if search_context := self.request.GET.get('search', None) :
			context['search_context'] = search_context

		return context



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


class AuthorsView(ListView):
	model = Autor
	paginate_by = 1
	context_object_name = 'authors'
	template_name = 'bookapp/authors.html'

	def get_queryset(self):
		search_context = self.request.GET.get('search', None)

		authors = Autor.objects.order_by('author_full_name')
		if search_context:
			authors = Autor.objects.filter(author_full_name=search_context)

		return authors

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		if search_context := self.request.GET.get('search', None):
			context['search_context'] = search_context

		return context


def particular_author(request, pk):
	author = get_object_or_404(Autor, pk=pk)
	if author is not None:
		author_books = Book.objects.filter(book_autor_info=author.author_full_name)
		context = {
			'author': author,
			'author_books': author_books
		}
	return render(request, 'bookapp/author_info.html', context)
	

def profile(request):
	return render(request, 'bookapp/profile.html')
