from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.
primeNumberList = [2, 3, 5, 7]

def decimals_subtract_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        decimalRange1 = myutil.get_random(1, 3)
        decimal1 = myutil.get_decimal2(decimalRange1)
        decimalRange2 = myutil.get_random(1, 3)
        decimal2 = myutil.get_decimal2(decimalRange2)
        if(decimal1 > decimal2):
            context['decimal1'] = decimal1
            context['decimal2'] = decimal2
        else:
            context['decimal1'] = decimal2
            context['decimal2'] = decimal1
        if(decimalRange1 > decimalRange2):
            context['decimalRange'] = decimalRange1
        else:
            context['decimalRange'] = decimalRange2
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'new/grade5decimals_subtract.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        userinput = -1
        try:
            userinput = float(request.GET['userinput'])
        except Exception:
            pass
        decimal1 = float(request.GET['decimal1'])
        decimal2 = float(request.GET['decimal2'])
        decimalRange = int(request.GET['decimalRange'])
        
        addition_result = round(decimal1 - decimal2, decimalRange)
        successful = 0
        if(addition_result == userinput): 
            successful = 1
        
        if (submittedValue == 'GetAnswer'):
            userinput = addition_result
            successful = 1
        
        if(successful == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
            context['userinput'] = userinput
        else:
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['state'] = '1'
            if(userinput >= 0):
                context['userinput'] = userinput
        
        context['decimal1'] = decimal1
        context['decimal2'] = decimal2
        context['decimalRange'] = decimalRange
        
        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'new/grade5decimals_subtract.html', context)
