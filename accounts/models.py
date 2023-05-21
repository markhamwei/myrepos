from django.db import models
from django.conf import settings

# Create your models here.

class QuestionResponse(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
	)
	question_ID = models.CharField(max_length=100) # Identify which question this entry refers to
	question_content = models.CharField(max_length=150) # content of question
	response = models.CharField(max_length=100) # Response content
	correctness = models.BooleanField()	# Whether or not response was correct
	response_peeked = models.BooleanField() # whether or not Get Answer was used
	response_datetime = models.DateTimeField() # datetime at which response was made
	