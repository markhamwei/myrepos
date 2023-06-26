from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.

def fractions_identify_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        randoms = myutil.get_randoms(1, 0, 2)
        fractiontype = randoms[0]
        if(fractiontype != myutil.MIXED):
            randoms = myutil.get_randoms(2, 2, 99)
            if(randoms[0] == randoms[1]):
                randoms[0] = randoms[1] + 1
            context['number1'] = 0
            commonFactor = math.gcd(randoms[0], randoms[1])
            if(fractiontype == myutil.IMPROPER):
                context['number2'] = max(randoms[0],randoms[1])/commonFactor
                context['number3'] = min(randoms[0],randoms[1])/commonFactor
                if(context['number3'] == 1):
                    context['number2'] += 1
                    context['number3'] += 1
            else:
                context['number2'] = min(randoms[0],randoms[1])/commonFactor
                context['number3'] = max(randoms[0],randoms[1])/commonFactor
        else:
            randoms = myutil.get_randoms(1, 1, 9)
            context['number1'] = randoms[0]
            randoms = myutil.get_randoms(2, 2, 99)
            if(randoms[0] == randoms[1]):
                randoms[0] = randoms[1] + 1
            commonFactor = math.gcd(randoms[0], randoms[1])
            context['number2'] = min(randoms[0],randoms[1])/commonFactor
            context['number3'] = max(randoms[0],randoms[1])/commonFactor
        context['flag'] = '='
        context['cmd'] = 'Submit'
        context['fractionType'] = fractiontype
        return render(request, 'grade5/grade5fractions_Identify.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        useranswer = "-1"
        try:
            useranswer = request.GET['fractionType']
        except Exception:
            pass
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        num3 = request.GET['num3']
        answer = request.GET['type']
        context['number1'] = num1
        context['number2'] = num2
        context['number3'] = num3
        context['fractionType'] = answer
        context['state'] = '1'
        if (submittedValue != 'GetAnswer'):
            if(int(useranswer) == myutil.IMPROPER):
                context['improper'] = 'checked'
            else:
                if(int(useranswer) == myutil.PROPER):
                    context['proper'] = 'checked'
                else:
                    if(int(useranswer) == myutil.MIXED):
                        context['mix'] = 'checked'
        context['flag'] = 'x'
        context['cmd'] = 'Retry'

        try:
            if ((submittedValue == 'GetAnswer') or (int(answer) == int(useranswer))):
                if(int(answer) == myutil.IMPROPER):
                    context['improper'] = 'checked'
                else:
                    if(int(answer) == myutil.PROPER):
                        context['proper'] = 'checked'
                    else:
                        if(int(answer) == myutil.MIXED):
                            context['mix'] = 'checked'
                context['flag'] = 'v'
                context['cmd'] = 'Next'
                context['state'] = '0'
        except Exception:
            pass
        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'grade5/grade5fractions_Identify.html', context)
