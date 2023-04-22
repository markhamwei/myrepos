from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import datetime

# Create your views here.

def perimeter_page(request):
	context = {}
	return render(request, 'grade5Perimeter.html', context)
