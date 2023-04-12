from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import datetime

# Create your views here.


def time_page(request):
    context = {'state': '0', 'year': '2023'}
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        randoms = myutil.get_randoms(6, 0, 59)
        hour1 = randoms[0] % 12 + 1
        minute1 = randoms[1]
        second1 = randoms[2]
        context['hour1'] = hour1
        context['minute1'] = minute1
        context['second1'] = second1
        startTime = datetime.datetime(2023, 4, 11, hour1, minute1, second1)
        hour2 = randoms[3] % 12
        minute2 = randoms[4]
        second2 = randoms[5]
        extra_time = datetime.timedelta(
            hours=hour2, minutes=minute2, seconds=second2)
        endTime = startTime + extra_time
        context['hour2'] = endTime.hour
        context['minute2'] = endTime.minute
        context['second2'] = endTime.second
        context['answer'] = ''
        return render(request, 'grade5Clock.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        useranswer = request.GET['answer']
        answer = myutil.math_query(f'{num1}-{num2}')
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

        return render(request, 'grade5Clock.html', context)
