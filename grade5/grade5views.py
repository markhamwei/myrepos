from django.shortcuts import render
from django.http import HttpResponse
# import wolframalpha

# Create your views here.


def grade5_home(request):
    return render(request, 'new/grade5home.html')
