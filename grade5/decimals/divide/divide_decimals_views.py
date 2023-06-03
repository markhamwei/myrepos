from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.
numbersForDivide = [0, 10, 100, 1000, 10000] #0 will goto randomly get a number

def decimals_divide_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        decimalRange1 = myutil.get_random(2, 3)
        decimal1 = myutil.get_decimal2(decimalRange1)
        numberToChoose = myutil.get_random(0, 4)
        if(numberToChoose == 0):
            tmpint = int(myutil.get_random(1, 19))
            if((myutil.get_msec() % 2) == 0):
                decimal2 = round((tmpint/10), 1)
                decimalRange2 = 1
            else:
                decimal2 = round((tmpint/100), 2)
                decimalRange2 = 2
            decimal1 = decimal1 * decimal2 #make sure the new decimal1 can divide decimal2 without rest.
            decimalRange = decimalRange1 #prepare for final answer
            decimalRange1 = decimalRange1 + decimalRange2
            decimal1 = round(decimal1, decimalRange1)
        else:
            decimalRange2 = 0
            decimal2 = numbersForDivide[numberToChoose]
            decimalRange = decimalRange1 + numberToChoose
        context['decimal1'] = decimal1
        context['decimal2'] = decimal2
        
        context['decimalRange'] = decimalRange
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'new/grade5decimals_divide.html', context)
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
        
        divide_result = round(decimal1 / decimal2, decimalRange)
        if(divide_result == int(divide_result)):
            divide_result = int(divide_result)
        successful = 0
        if(divide_result == userinput): 
            successful = 1
        
        if (submittedValue == 'GetAnswer'):
            userinput = divide_result
            successful = 1
        
        if(successful == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
            if(userinput == int(userinput)):
                userinput = int(userinput)
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

        return render(request, 'new/grade5decimals_divide.html', context)
