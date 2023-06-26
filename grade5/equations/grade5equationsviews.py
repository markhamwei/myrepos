from django.shortcuts import render
from django.http import HttpResponse
# import wolframalpha

# Create your views here.


def grade5_equations_home(request):
    return render(request, 'grade5/grade5equationshome.html')
