from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User


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

admin.site.register(QuestionResponse)


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	registration_date = models.DateTimeField(default=None)
	expiration_date = models.DateTimeField(default=None)
	is_premium = models.BooleanField(default=False)

admin.site.register(Profile)