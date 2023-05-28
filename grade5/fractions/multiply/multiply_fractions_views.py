from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.

def fractions_multiply_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        randoms = myutil.get_randoms(2, 0, 2)
        fraction1 = [0, 0, 0]
        fraction2 = [0, 0, 0]
        if(randoms[0] == 0): #improper
            franction = myutil.get_improper_fraction(2, 19)
            fraction1[0] = 0
            fraction1[1] = franction[0]
            fraction1[2] = franction[1]
        if(randoms[0] == 1): #proper
            franction = myutil.get_proper_fraction(2, 19)
            fraction1[0] = 0
            fraction1[1] = franction[0]
            fraction1[2] = franction[1]
        if(randoms[0] == 2): #mixed
            franction = myutil.get_mixed_fraction(9, 2, 19)
            fraction1[0] = franction[0]
            fraction1[1] = franction[1]
            fraction1[2] = franction[2]
        if(randoms[1] == 0): #improper
            franction = myutil.get_improper_fraction(2, 19)
            fraction2[0] = 0
            fraction2[1] = franction[0]
            fraction2[2] = franction[1]
        if(randoms[1] == 1): #proper
            franction = myutil.get_proper_fraction(2, 19)
            fraction2[0] = 0
            fraction2[1] = franction[0]
            fraction2[2] = franction[1]
        if(randoms[1] == 2): #mixed
            franction = myutil.get_mixed_fraction(9, 2, 19)
            fraction2[0] = franction[0]
            fraction2[1] = franction[1]
            fraction2[2] = franction[2]
            
        context['number11'] = fraction1[0]
        context['number12'] = fraction1[1]
        context['number13'] = fraction1[2]
        context['number21'] = fraction2[0]
        context['number22'] = fraction2[1]
        context['number23'] = fraction2[2]
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'new/grade5fractions_multiply.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        userinteger = -1
        usernumerator = -2
        userdenominator = -3
        try:
            userinteger = int(request.GET['integer'])
            usernumerator = int(request.GET['numerator'])
            userdenominator = int(request.GET['denominator'])
        except Exception:
            pass
        num11 = int(request.GET['num11'])
        num12 = int(request.GET['num12'])
        num13 = int(request.GET['num13'])
        num21 = int(request.GET['num21'])
        num22 = int(request.GET['num22'])
        num23 = int(request.GET['num23'])
        
        addition_result = myutil.multiply_fractions(num11, num12, num13, num21, num22, num23)
        successful = 0
        if(addition_result[2] == 0): #denominator of the addition result
            if((addition_result[0] == userinteger) and (usernumerator <= 0)):
                successful = 1
        else:
            if((addition_result[0] == userinteger) and (addition_result[1] == usernumerator) and (addition_result[2] == userdenominator)):
                successful = 1
        
        if (submittedValue == 'GetAnswer'):
            successful = 1
        
        if(successful == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
            context['usernumber1'] = int(addition_result[0])
            context['usernumber2'] = int(addition_result[1])
            context['usernumber3'] = int(addition_result[2])
        else:
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['state'] = '1'
            if(userinteger > 0):
                context['usernumber1'] = int(userinteger)
            if(usernumerator > 0):
                context['usernumber2'] = int(usernumerator)
            if(userdenominator > 0):
                context['usernumber3'] = int(userdenominator)
        
        context['number11'] = num11
        context['number12'] = num12
        context['number13'] = num13
        context['number21'] = num21
        context['number22'] = num22
        context['number23'] = num23
        
        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'new/grade5fractions_multiply.html', context)
