from django.shortcuts import render
from django.http import HttpResponse
# import wolframalpha

# Create your views here.


def grade5_wholenumbers_home(request):
    return render(request, 'grade5/grade5wholenumbershome.html')
