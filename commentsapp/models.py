from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
	comment_author = models.ForeignKey(User, models.CASCADE)
	comment_content = models.TextField(max_length=1000)
	comment_date = models.DateField(auto_now=True)

	# The name of object(name of book/author) that related to specific book or author
	related_object_name = models.CharField(max_length=2**10, blank=True, null=True, default='', help_text='NEVER CHANGE!')

	def __str__(self):
		if len(self.comment_content) > 17:
			return f'{self.comment_content[:17]}...'
		else:
			return f'{self.comment_content}'
