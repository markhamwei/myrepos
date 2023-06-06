from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
from datetime import datetime

# Create your views here.

def area_page(request):
	context = {
		'year' : '2023'
	}
	if(request.method == 'GET' or (request.method == 'POST' and request.POST['submit'] == 'Next Question!')):
		context['state'] = 'question'
		polygon_type = myutil.get_random(0, 3)
		if(polygon_type < 1):
			base, height, offset = myutil.get_randoms(3, 1, 10)
			offset = 6-offset
			context['question'] = f'PolyDrawer.drawTriangle_bh({base}, {height}, {offset}, true, 35, "polygonCanvas")'
			context['answer'] = myutil.scramble(str(base*height/2))
		elif(polygon_type < 2):
			base, height = myutil.get_randoms(2, 1, 10)
			context['question'] = f'PolyDrawer.drawRectangle({base}, {height}, true, 35, "polygonCanvas")'
			context['answer'] = myutil.scramble(str(base*height))
		elif(polygon_type < 3):
			base, height, offset = myutil.get_randoms(3, 1, 10)
			offset = 6-offset
			context['question'] = f'PolyDrawer.drawTrapezoid({base}, {height}, {base}, {offset}, true, 35, "polygonCanvas")'
			context['answer'] = myutil.scramble(str(base*height))
		elif(polygon_type < 4):
			base, height, top, offset = myutil.get_randoms(4, 1, 10)
			offset = 6-offset
			context['question'] = f'PolyDrawer.drawTrapezoid({base}, {height}, {top}, {offset}, true, 35, "polygonCanvas")'
			context['answer'] = myutil.scramble(str(height*(base+top)/2))
	
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

	return render(request, 'new/grade5Area.html', context)
