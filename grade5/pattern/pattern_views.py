from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math
from pipes import stepkinds

# Create your views here.

def pattern_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        order = myutil.get_msec()
        order = order%2 #2 for ascending
        times = myutil.get_random(1, 3)
        if(times < 3):
            start = myutil.get_random(2, 9)
            step = myutil.get_random(2, 20)
        else:
            start = myutil.get_random(2, 5)
            step = myutil.get_random(2, 5)
        if(start == step):
            step += 1
        result0 = []
        result1 = []
        value0 = start
        value1 = start
        resultSelected = 1
        for _ in range(8):
            result0.append(value0)
            result1.append(value1)
            value0 = value0 * times + step
            value1 = value1 * times - step
            if((value1 < 1) or (value1 == start)):
                resultSelected = 0
            
        context['times'] = times
        if(resultSelected == 0):
            result = result0
            context['step'] = step
        else:
            result = result1
            context['step'] = -step
        
        if(order == 0): #in ascending order
            context['num1'] = result[0]
            context['num2'] = result[1]
            context['num3'] = result[2]
            context['num4'] = result[3]
            context['num5'] = result[4]
            context['num6'] = result[5]
            context['values'] = myutil.myList2Str(result, False)
        else:
            context['num1'] = result[7]
            context['num2'] = result[6]
            context['num3'] = result[5]
            context['num4'] = result[4]
            context['num5'] = result[3]
            context['num6'] = result[2]
            context['values'] = myutil.myList2Str(result, True)
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'grade5/grade5pattern.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        useranswer1 = -1
        useranswer2 = -2
        try:
            useranswer1 = int(request.GET['usernum1'])
            useranswer2 = int(request.GET['usernum2'])
        except Exception:
            pass
        
        values = request.GET['values']
        mylist = myutil.myStr2List(values)
        times = int(request.GET['times'])
        step = int(request.GET['step'])
        rightAnswer1 = int(mylist[6])
        rightAnswer2 = int(mylist[7])
        
        success = 0
        if(((useranswer1 == rightAnswer1) and (useranswer2 == rightAnswer2)) or (submittedValue == 'GetAnswer')):
            success = 1
            useranswer1 = rightAnswer1
            useranswer2 = rightAnswer2
            pattern = "rule = "
            if(rightAnswer1 < rightAnswer2):
                if(times > 1):
                    pattern += "*"+str(times)
                if(step > 0):
                    pattern += "+"+str(step)
                else:
                    if(step < 0):
                        pattern += str(step)
            else:
                if(step > 0):
                    pattern += "(-"+str(step)+")"
                else:
                    if(step < 0):
                        pattern += "(+"+str(abs(step))+")"
                if(times > 1):
                    pattern += "/"+str(times)
            context['pattern_rule'] = pattern
        
        context['values'] = values
        context['times'] = times
        context['step'] = step
        context['num1'] = mylist[0]
        context['num2'] = mylist[1]
        context['num3'] = mylist[2]
        context['num4'] = mylist[3]
        context['num5'] = mylist[4]
        context['num6'] = mylist[5]
        if(useranswer1 >= 0):
            context['usernum1'] = useranswer1
        if(useranswer2 >= 0):
            context['usernum2'] = useranswer2
        
        if(success == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
        else:
            context['state'] = '1'
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'

        return render(request, 'grade5/grade5pattern.html', context)
