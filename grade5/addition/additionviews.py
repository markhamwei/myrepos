from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
# import wolframalpha

# Create your views here.


def addition_page(request):
    context = {'number1': '', 'number2': '', 'year': '2023'}
    randoms = myutil.get_randoms(2, 1000, 9999)
    context['number1'] = randoms[0]
    context['number2'] = randoms[1]
    return render(request, 'grade5Addition.html', context)
