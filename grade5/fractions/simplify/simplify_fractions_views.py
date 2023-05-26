from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.
primeNumberList = [2, 3, 5, 7]

def fractions_simplily_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        randoms = myutil.get_randoms(2, 2, 16)
        num1 = randoms[0]
        num2 = randoms[1]
        if(num1 == num2):
            num2 = num1 + 1
        randoms = myutil.get_randoms(2, 0, 3)
        myfactor = primeNumberList[randoms[0]] * primeNumberList[randoms[1]]
        context['number1'] = 0 #not mixed fraction
        context['number2'] = num1 * myfactor
        context['number3'] = num2 * myfactor
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'new/grade5fractions_simplify.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        usernumerator = -1
        userdenominator = -2
        try:
            usernumerator = int(request.GET['numerator'])
            userdenominator = int(request.GET['denominator'])
        except Exception:
            pass
        num1 = int(request.GET['num2'])
        num2 = int(request.GET['num3'])
        commFactor = math.gcd(num1, num2)
        numerator = num1/commFactor
        denominator = num2/commFactor
        if ((submittedValue == 'GetAnswer') or ((usernumerator == numerator) and (userdenominator == denominator))):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
            context['usernumber1'] = int(numerator)
            context['usernumber2'] = int(denominator)
        else:
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['state'] = '1'
            if(usernumerator > 0):
                context['usernumber1'] = usernumerator
                context['usernumber2'] = userdenominator
            else:
                context['usernumber1'] = ''
                context['usernumber2'] = ''

        context['number1'] = 0 #not mixed fraction
        context['number2'] = num1
        context['number3'] = num2
        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'new/grade5fractions_simplify.html', context)
