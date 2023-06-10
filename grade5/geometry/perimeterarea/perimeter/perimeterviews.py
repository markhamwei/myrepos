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
	context = {
		'year' : '2023'
	}
	if(request.method == 'GET' or (request.method == 'POST' and request.POST['submit'] == 'Next Question!')):
		context['state'] = 'question'
		lst = myutil.get_randoms(2, 1, 10)
		lst.append(myutil.get_random(1, min(sum(lst)-1, 10)))
		context['question'] = f'PolyDrawer.drawPolygon_l({lst}, true, 35, "polygonCanvas")'
		context['answer'] = myutil.scramble(str(sum(lst)))
	
	if(request.method == 'POST'):
		if(request.POST['submit'] == 'Submit!'):
			val = myutil.unscramble(request.POST['answer'])
			resp = request.POST['response']
			if(resp.isnumeric() and abs(float(val)-float(resp))<1e-7):
				context['state'] = 'correct'
				context['response'] = request.POST['response']
				context['question'] = request.POST['question']
				context['answer'] = request.POST['answer']
			else:
				context['state'] = 'incorrect'
				context['response'] = request.POST['response']
				context['question'] = request.POST['question']
				context['answer'] = request.POST['answer']
		if(request.POST['submit'] == 'Get Answer'):
			context['state'] = 'get answer'
			context['answer'] = myutil.unscramble(request.POST['answer'])
			context['question'] = request.POST['question']

	return render(request, 'new/grade5Perimeter.html', context)
