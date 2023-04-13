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
        estra_hour2 = randoms[3] % 3
        estra_minute2 = randoms[4]
        estra_second2 = randoms[5]
        extra_time = datetime.timedelta(
            hours=estra_hour2, minutes=estra_minute2, seconds=estra_second2)
        endTime = startTime + extra_time
        context['hour2'] = endTime.hour
        context['minute2'] = endTime.minute
        context['second2'] = endTime.second
        context['answer1'] = ''
        context['answer2'] = ''
        context['answer3'] = ''
        context['flag'] = ''
        context['cmd'] = 'Submit'
        context['button2'] = ''
        return render(request, 'grade5Clock.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        submittedValue = request.GET['Submit']
        hour1 = request.GET['hour1']
        minute1 = request.GET['minute1']
        second1 = request.GET['second1']
        hour2 = request.GET['hour2']
        minute2 = request.GET['minute2']
        second2 = request.GET['second2']
        answer1 = request.GET['answer1']
        answer2 = request.GET['answer2']
        answer3 = request.GET['answer3']
        context['hour1'] = hour1
        context['minute1'] = minute1
        context['second1'] = second1
        context['hour2'] = hour2
        context['minute2'] = minute2
        context['second2'] = second2
        try:
            startTime = datetime.datetime(
                2023, 4, 11, int(hour1), int(minute1), int(second1))
            if (submittedValue != 'GetAnswer'):
                extra_time = datetime.timedelta(
                    hours=int(answer1), minutes=int(answer2), seconds=int(answer3))
                endTime = startTime + extra_time
            if ((submittedValue == 'GetAnswer') or
                    (endTime.hour == int(hour2) and endTime.minute == int(minute2) and endTime.second == int(second2))):
                endTime = datetime.datetime(
                    2023, 4, 11, int(hour2), int(minute2), int(second2))
                extra_time = endTime - startTime
                hours, remainder = divmod(extra_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                context['answer1'] = hours
                context['answer2'] = minutes
                context['answer3'] = seconds
                context['flag'] = 'v'
                context['cmd'] = 'Next'
                context['state'] = '0'
            else:
                context['answer1'] = answer1
                context['answer2'] = answer2
                context['answer3'] = answer3
                context['flag'] = 'x'
                context['state'] = '1'
                context['cmd'] = 'Retry'
        except Exception:
            context['answer1'] = answer1
            context['answer2'] = answer2
            context['answer3'] = answer3
            context['flag'] = 'x'
            context['state'] = '1'
            context['cmd'] = 'Retry'

        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'grade5Clock.html', context)
