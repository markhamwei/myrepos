from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
from datetime import datetime

# Create your views here.

def perimeter_page(request):
	context = { 'year' : '2023' }
	return render(request, 'new/grade5Perimeter.html', context)
