from django.shortcuts import render
from django.http import HttpResponse
# import wolframalpha

# Create your views here.


def grade5_geometry_home(request):
    return render(request, 'new/grade5geometryhome.html')
