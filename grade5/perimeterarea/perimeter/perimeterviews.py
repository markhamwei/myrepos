from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
from datetime import datetime
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from accounts.models import QuestionResponse
import datetime

# Create your views here.

@ensure_csrf_cookie
def perimeter_page(request):
	if(request.method == 'GET'):
		context = { 'year' : '2023' }
		return render(request, 'new/grade5Perimeter.html', context)
	else:
		content = json.loads(request.body)
		field = QuestionResponse.objects.create(
			user=request.user,
			question_ID="grade5/perimeterarea/perimeter",
			question_content=content['question-content'],
			response=content['response'],
			correctness=content['correctness'],
			response_peeked=content['response-peeked'],
			response_datetime=datetime.datetime.now()
		)
		field.save()
		return render(request, 'new/grade5Perimeter.html')