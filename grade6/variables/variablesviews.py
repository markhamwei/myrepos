from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil

def variables_home(request):
    return render(request, 'new/grade6VariablesHome.html')