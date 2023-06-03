from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.
ROUNDNOTHING = -1
ROUNDTOINT = 0
ROUNDTOTENTH = 1
ROUNDTOHUNDREDTH = 2

def decimals_round_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        roundControl = ROUNDNOTHING
        nDigits = myutil.get_random(1, 3) #get how many digits after decimal point
        decimal1 = myutil.get_decimal2(nDigits)
        if(nDigits == 1):
            context['roundTarget'] = 'the nearest whole number'
            roundControl = ROUNDTOINT
        if(nDigits == 2):
            random1 = myutil.get_random(0, 4)
            if(random1 == 0):
                context['roundTarget'] = 'the nearest whole number'
                roundControl = ROUNDTOINT
            if(random1 >= 1):
                context['roundTarget'] = 'the nearest tenth'
                roundControl = ROUNDTOTENTH
        if(nDigits == 3):
            random1 = myutil.get_random(0, 6)
            if(random1 == 0):
                context['roundTarget'] = 'the nearest whole number'
                roundControl = ROUNDTOINT
            if(random1 == 1 or random1 == 2):
                context['roundTarget'] = 'the nearest tenth'
                roundControl = ROUNDTOTENTH
            if(random1 >= 3):
                context['roundTarget'] = 'the nearest hundredth'
                roundControl = ROUNDTOHUNDREDTH
        
        context['decimal1'] = decimal1
        context['roundControl'] = roundControl
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'new/grade5decimals_round.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        userinput = -2
        try:
            userinput = float(request.GET['userinput'])
        except Exception:
            pass
        decimal1 = float(request.GET['decimal1'])
        roundControl = int(request.GET['roundControl'])
        decimal2 = round(decimal1, roundControl)
        if(userinput >= 0):
            if(roundControl == ROUNDTOINT):
                context['userinput'] = int(userinput)
            else:
                context['userinput'] = userinput
        if(roundControl == ROUNDTOINT):
            context['roundTarget'] = 'the nearest whole number'
        else:
            if(roundControl == ROUNDTOTENTH):
                context['roundTarget'] = 'the nearest tenth'
            else:
                context['roundTarget'] = 'the nearest hundredth'
        
        successful = 0
        if(userinput == decimal2):
            successful = 1
        
        if (submittedValue == 'GetAnswer'):
            if(roundControl == ROUNDTOINT):
                userinput = int(decimal2)
            else:
                userinput = decimal2
            context['userinput'] = userinput
            successful = 1
        
        if(successful == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
        else:
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['state'] = '1'
        
        context['decimal1'] = decimal1
        context['roundControl'] = roundControl
        
        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'new/grade5decimals_round.html', context)
