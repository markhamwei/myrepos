from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil

# Create your views here.


def multiply_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        randoms = myutil.get_randoms(2, 10, 999)
        context['number1'] = randoms[0]
        context['number2'] = randoms[1]
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'grade5Multiply.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        useranswer = request.GET['answer']
        answer = myutil.math_query(f'{num1}*{num2}')
        context['number1'] = num1
        context['number2'] = num2
        context['state'] = '1'
        context['answer'] = useranswer
        context['flag'] = 'x'
        context['cmd'] = 'Retry'

        try:
            if ((submittedValue == 'GetAnswer') or (int(answer) == int(useranswer))):
                context['answer'] = answer
                context['flag'] = 'v'
                context['cmd'] = 'Next'
                context['state'] = '0'
        except Exception:
            pass
        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'grade5Multiply.html', context)
