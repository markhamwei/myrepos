from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import random

def page(request):
    return render(request, 'new/grade6multiplechoicesolving.html')