from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil

# Create your views here.


def addition_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        randoms = myutil.get_randoms(2, 100, 9999)
        context['number1'] = randoms[0]
        context['number2'] = randoms[1]
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'grade5Addition.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        useranswer = request.GET['answer']
        answer = myutil.math_query(f'{num1}+{num2}')
        context['number1'] = num1
        context['number2'] = num2
        context['state'] = '1'
        context['answer'] = useranswer
        context['flag'] = 'x'
        context['cmd'] = 'Retry'
        try:
            if (int(answer) == int(useranswer)):
                context['flag'] = 'v'
                context['cmd'] = 'Refresh'
                context['state'] = '0'
        except Exception:
            pass
        return render(request, 'grade5Addition.html', context)
