from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from commentsapp.models import Comment
from commentsapp.tools import create_comment
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


class ParticularBook(ListView, DetailView):
	template_name = 'bookapp/book_info.html'
	paginate_by = 1
	object_list = Comment.objects.all()
	object = Book

	def get_queryset(self):
		comments = Comment.objects.filter(related_object_name=self.get_object().book_name)
		comments = comments.order_by('comment_date')
		return comments

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['book_author'] = Autor.objects.get(author_full_name=self.get_object().book_autor)
		context['comments'] = self.get_queryset()
		context['book'] = self.get_object()
		# context['current_link'] = self.request.path

		return context

	def get_object(self):
		return get_object_or_404(Book, pk=self.kwargs.get('pk'))

	def post(self, request, pk, *args, **kwargs):
		create_comment(request, self.get_object())
		return redirect('bookapp:particular_book', pk=pk)


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


class ParticularAuthor(ListView, DetailView):
	template_name = 'bookapp/author_info.html'
	paginate_by = 1
	object_list = Comment.objects.all()
	object = Autor

	def get_queryset(self):
		comments = Comment.objects.filter(related_object_name=self.get_object().author_full_name)
		comments = comments.order_by('comment_date')

		return comments

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author_books'] = Book.objects.filter(book_autor_info=self.get_object().author_full_name)
		context['comments'] = self.get_queryset()
		context['author'] = self.get_object()

		return context

	def get_object(self):
		return get_object_or_404(Autor, pk=self.kwargs.get('pk'))

	def post(self, request, pk, *args, **kwargs):
		create_comment(request, self.get_object())
		return redirect('bookapp:particular_author', pk=pk)


class ProfilePage(TemplateView):
	template_name = 'bookapp/profile.html'
