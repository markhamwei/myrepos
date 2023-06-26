import sys
from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil

# Create your views here.
unitNum = 5
lengthUnit = ['km', 'm', 'dm', 'cm', 'mm']


def length_page(request):
    context = {'number1': '', 'unit1': '', 'state': '0', 'year': '2023', 'answer': '', 'unit2': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        randoms = myutil.get_randoms(2, 0, unitNum-1)
        unitIndex0 = randoms[0]
        unitIndex1 = randoms[1]

        if (unitIndex0 == unitIndex1):
            unitIndex1 = (unitIndex1+1) % unitNum
        if (unitIndex0 == 0):
            unitIndex1 = 1  # km always with m
        if (unitIndex1 == 0):
            unitIndex0 = 1  # km always with m

        context['unit1'] = lengthUnit[unitIndex0]
        context['unit2'] = lengthUnit[unitIndex1]
        number = myutil.get_msec()
        number %= 10
        if (number == 0):
            number += 1
        if (unitIndex0 < unitIndex1):
            context['number1'] = number
        else:
            answer = myutil.math_query(
                f'{number}{lengthUnit[unitIndex1]} = ? {lengthUnit[unitIndex0]}')
            words = answer.split(' ')
            context['number1'] = words[0]
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'grade5/grade5Length.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        num1 = request.GET['num1']
        useranswer = request.GET['answer']
        unit1 = request.GET['unit1']
        unit2 = request.GET['unit2']
        context['unit1'] = unit1
        context['unit2'] = unit2
        queryanswer = myutil.math_query(
            f'{num1}{unit1} = ? {unit2}')
        words = queryanswer.split(' ')
        answer = words[0]
        # print >>sys.stderr, queryanswer
        context['number1'] = num1
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

        return render(request, 'grade5/grade5Length.html', context)
