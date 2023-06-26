from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.

def grade5_factors_gcf_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        numbers = myutil.get_randoms(4, 2, 12)
        
        number1 = numbers[0]*numbers[3]
        number2 = numbers[1]*numbers[3]
        if(number1 == number2):
            number2 += 10
            
        context['number1'] = number1
        context['number2'] = number2
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'grade5/grade5_factors_gcf.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        number1 = int(request.GET['number1'])
        number2 = int(request.GET['number2'])
        try:
            useranswer = int(request.GET['answer'])
        except:
            useranswer = -1
        
        gcf = math.gcd(number1, number2)
        if(gcf == useranswer):
            success = 1
        else:
            success = 0
        if(submittedValue == 'GetAnswer'):
            success = 1
        
        context['number1'] = number1
        context['number2'] = number2
        if(success == 0):
            context['state'] = '1'
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'
            if(useranswer >= 0):
                context['answer'] = useranswer
        else:
            context['state'] = '0'
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['button2'] = ''
            context['answer'] = gcf

        return render(request, 'grade5/grade5_factors_gcf.html', context)
