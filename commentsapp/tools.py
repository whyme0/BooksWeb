from time import mktime
from bookapp.models import Book
from .models import Comment

def is_comment_empty(request):
	'''Check if text in textarea not empty, therefore comment is correct'''
	return len(request.POST['comment_text'].strip()) == 0

def create_comment(request, current_model):
	'''Create comment and save it in database'''
	if not is_comment_empty(request):
			comment = Comment()
			comment.comment_author = request.user
			comment.comment_content = request.POST['comment_text'].strip()

			if type(current_model) is type(Book()):
				comment.related_object_name = current_model.book_name
			# else current model is Author
			else:
				comment.related_object_name = current_model.author_full_name
			
			comment.save()
	else:
		return 'Ваш комментарий выглядит пустым, не так ли?'
