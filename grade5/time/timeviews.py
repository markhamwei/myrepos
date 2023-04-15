from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import datetime

# Create your views here.


def time_page(request):
    context = {'state': '0', 'year': '2023'}
    state = 0
    displaytype = ''
    submittedValue = ''
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    try:
        displaytype = request.GET['type']
    except Exception:
        pass
    try:
        submittedValue = request.GET['Submit']
    except Exception:
        pass

    if ((state == 0) or (submittedValue == 'text') or (submittedValue == 'picture')):  # the initial state
        if ((submittedValue == 'text') or (submittedValue == 'picture')):
            # maybe user clicked the switch button between picture/text time.
            displaytype = submittedValue
        if ((displaytype != 'text') and (displaytype != 'picture')):
            tmpMsec = myutil.get_msec()
            if (tmpMsec % 2 == 1):
                context['type'] = 'text'
            else:
                context['type'] = 'picture'
        else:
            context['type'] = displaytype
        if (context['type'] == 'picture'):
            context['OtherType'] = 'text'
        else:
            context['OtherType'] = 'picture'
        context['state'] = '1'

        if ((submittedValue == 'text') or (submittedValue == 'picture')):
            hour1 = int(request.GET['hour1'])
            minute1 = int(request.GET['minute1'])
            second1 = int(request.GET['second1'])
            hour2 = int(request.GET['hour2'])
            minute2 = int(request.GET['minute2'])
            second2 = int(request.GET['second2'])
            startTime = datetime.datetime(2023, 4, 11, hour1, minute1, second1)
            endTime = datetime.datetime(2023, 4, 11, hour2, minute2, second2)
        else:
            randoms = myutil.get_randoms(6, 0, 59)
            hour1 = randoms[0] % 7 + 9  # limit the start hour between 9 and 15
            minute1 = randoms[1]
            second1 = randoms[2]
            estra_hour2 = randoms[3] % 6
            estra_minute2 = randoms[4]
            estra_second2 = randoms[5]
            extra_time = datetime.timedelta(
                hours=estra_hour2, minutes=estra_minute2, seconds=estra_second2)
            startTime = datetime.datetime(2023, 4, 11, hour1, minute1, second1)
            endTime = startTime + extra_time
        context['hour1'] = hour1
        context['minute1'] = f'{minute1:02d}'
        context['second1'] = f'{second1:02d}'
        context['hour2'] = endTime.hour
        context['hour1_12'] = startTime.strftime("%I")
        context['hour2_12'] = endTime.strftime("%I")
        context['minute2'] = f'{endTime.minute:02d}'
        context['second2'] = f'{endTime.second:02d}'
        context['am_pm1'] = startTime.strftime("%p")
        context['am_pm2'] = endTime.strftime("%p")
        context['answer1'] = ''
        context['answer2'] = ''
        context['answer3'] = ''
        context['flag'] = ''
        context['cmd'] = 'Submit'
        context['button2'] = ''
        return render(request, 'grade5Clock.html', context)
    if (state == 1):  # which means user cliked submit in the initial page
        context['type'] = request.GET['type']
        if (context['type'] == 'picture'):
            context['OtherType'] = 'text'
        else:
            context['OtherType'] = 'picture'
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
        context['minute1'] = f'{int(minute1):02d}'
        context['second1'] = f'{int(second1):02d}'
        context['hour2'] = hour2
        context['minute2'] = f'{int(minute2):02d}'
        context['second2'] = f'{int(second2):02d}'
        try:
            startTime = datetime.datetime(
                2023, 4, 11, int(hour1), int(minute1), int(second1))
            context['hour1_12'] = startTime.strftime("%I")
            context['am_pm1'] = startTime.strftime("%p")
            if (submittedValue != 'GetAnswer'):
                extra_time = datetime.timedelta(
                    hours=int(answer1), minutes=int(answer2), seconds=int(answer3))
                endTime = startTime + extra_time
            if ((submittedValue == 'GetAnswer') or
                    (endTime.hour == int(hour2) and endTime.minute == int(minute2) and endTime.second == int(second2))):
                endTime = datetime.datetime(
                    2023, 4, 11, int(hour2), int(minute2), int(second2))
                context['hour2_12'] = endTime.strftime("%I")
                context['am_pm2'] = endTime.strftime("%p")
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
                endTime = datetime.datetime(
                    2023, 4, 11, int(hour2), int(minute2), int(second2))
                context['hour2_12'] = endTime.strftime("%I")
                context['am_pm2'] = endTime.strftime("%p")
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
            endTime = datetime.datetime(
                2023, 4, 11, int(hour2), int(minute2), int(second2))
            context['hour2_12'] = endTime.strftime("%I")
            context['am_pm2'] = endTime.strftime("%p")

        if (context['cmd'] == 'Retry'):
            context['button2'] = 'GetAnswer'
        else:
            context['button2'] = ''

        return render(request, 'grade5Clock.html', context)
