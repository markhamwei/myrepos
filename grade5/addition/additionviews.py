from django.shortcuts import render
from django.http import HttpResponse
#import wolframalpha

# Create your views here.
def addition_page(request):
	return render(request, 'grade5Addition.html')
