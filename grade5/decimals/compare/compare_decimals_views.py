from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.
GREATER = 1
EQUALTO = 0
LESSTHAN = -1

def decimals_compare_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        random1 = myutil.get_random(0, 1) #0 for same int piece, 1 for random int piece.
        numDigits1 = myutil.get_random(1, 3) #the possible value is among {1, 2, 3}, to control how many digits in decimal piece.
        decimal1 = myutil.get_decimal(1, numDigits1)
        
        numDigits2 = myutil.get_random(1, 3) #the possible value is among {1, 2, 3}, to control how many digits in decimal piece.
        decimal2 = myutil.get_decimal(1, numDigits2)
        
        context['decimal1'] = round(decimal1[0]+decimal1[1], numDigits1)
        if(random1 == 0):
            context['decimal2'] = round(decimal1[0]+decimal2[1], numDigits2)
        else:
            context['decimal2'] = round(decimal2[0]+decimal2[1], numDigits2)
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'grade5/grade5decimals_compare.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        useranswer = -2
        try:
            useranswer = int(request.GET['comparison'])
        except Exception:
            pass
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        
        successful = 0
        if((num1 > num2) and (useranswer == GREATER)):
            successful = 1
        if((num1 == num2) and (useranswer == EQUALTO)):
            successful = 1
        if((num1 < num2) and (useranswer == LESSTHAN)):
            successful = 1
        
        if (submittedValue == 'GetAnswer'):
            if(num1 > num2):
                useranswer = GREATER
            else:
                if(num1 < num2):
                    useranswer = LESSTHAN
                else:
                    useranswer = EQUALTO
            successful = 1
        
        if(useranswer == GREATER):
            context['greater'] = 'checked'
        if(useranswer == LESSTHAN):
            context['less'] = 'checked'
        if(useranswer == EQUALTO):
            context['equal'] = 'checked'
        if(successful == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
        else:
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['state'] = '1'
        
        context['decimal1'] = num1
        context['decimal2'] = num2
        
        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'grade5/grade5decimals_compare.html', context)
