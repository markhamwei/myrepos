from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil

# Create your views here.

def grade5_factors_list_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        number = myutil.get_random(2, 100)
        
        context['number'] = number
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'grade5/grade5_factors_list.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        number = int(request.GET['number'])
        try:
            useranswer = request.GET['answer']
        except:
            useranswer = ""
        
        factors = myutil.getFactors(number)
        matchCount = 0
        tmpint = 0
        for i in range(0, len(useranswer)):
            tmpChar = ord(useranswer[i])
            char0 = ord('0')
            char9 = ord('9')
            if((tmpChar >= char0) and (tmpChar <= char9)):
                tmpint = tmpint * 10 + (tmpChar - char0)
            else:
                if tmpint in factors:
                    matchCount += 1
                    tmpint = 0
        if tmpint in factors:
            matchCount += 1
        
        if(matchCount == len(factors)):
            success = 1
        else:
            success = 0
        if(submittedValue == 'GetAnswer'):
            success = 1
        
        context['number'] = number
        if(success == 0):
            context['state'] = '1'
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'
            context['answer'] = useranswer
        else:
            context['state'] = '0'
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['button2'] = ''
            context['answer'] = myutil.myList2Str(factors, False)

        return render(request, 'grade5/grade5_factors_list.html', context)
