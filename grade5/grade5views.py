from django.shortcuts import render
from django.http import HttpResponse
# import wolframalpha

# Create your views here.


def grade5_home(request):
    return render(request, 'grade5/grade5home.html')
