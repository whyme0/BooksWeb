from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime


class Autor(models.Model):
	author_full_name = models.CharField(max_length=303, default=None)
	date_birth = models.DateField('birth date')
	death_date = models.DateField('death date')
	birth_place = models.CharField(max_length=90, default=None)
	author_picture = models.ImageField(upload_to='bookapp/static/bookapp/pictures', default=None)

	def __str__(self):
		return self.author_full_name

	
	def get_static_url(self) -> str:
		return self.author_picture.url[7:]


class Book(models.Model):
	book_autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
	book_autor_info = models.CharField(max_length=303)
	book_name = models.CharField(max_length=2**10)
	book_genre = models.CharField(max_length=32)
	book_picture = models.ImageField(upload_to='bookapp/static/bookapp/pictures', default=None)
	
	# just year of publication
	book_year = models.PositiveSmallIntegerField(
			validators=[
				MaxValueValidator(
					datetime.now().year,
					'Год должен быть не больше чем тукущий'
				)
			]
		)
	
	book_description = models.TextField()


	def __str__(self):
		return self.book_name

	def get_static_url(self):
		return self.book_picture.url[7:]


	def is_new():
		return self._book_year >= 2000
