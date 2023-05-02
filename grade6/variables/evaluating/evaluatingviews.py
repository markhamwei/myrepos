from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil

def evaluating_page(request):
    context={'definitions':'hi :)'}
    return render(request, 'new/grade6Evaluating.html', context)