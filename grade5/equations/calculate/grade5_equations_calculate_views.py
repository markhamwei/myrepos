from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil

# Create your views here.
OPERATE_ADD = 0
OPERATE_SUBTRACT = 1
OPERATE_MULTIPLY = 2
OPERATE_DIVIDE= 3

def grade5_equations_calculate_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    lastOperate = -1
    specifyOperate = -1
    try:
        lastOperate = int(request.GET['operate'])
    except Exception:
        pass
    try:
        specifyOperate = int(request.GET['specifyOperate'])
    except Exception:
        pass
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        if(specifyOperate >= 0):
            operate = specifyOperate
        else:
            operate = myutil.get_random(0, 3)
            if(operate == lastOperate):
                operate += 1
                if(operate == 4):
                    operate = 0
        #always use num1 to represent the value of X
        if(operate == OPERATE_ADD):
            numbers = myutil.get_randoms(2, 1, 30)
            num1 = numbers[0]
            num2 = numbers[1]
            num3 = num1 + num2
            equation = "X + "+str(num2)+" = "+str(num3)
        if(operate == OPERATE_SUBTRACT):
            numbers = myutil.get_randoms(2, 1, 50)
            num1 = max(numbers)
            num2 = min(numbers)
            if(num1 == num2):
                num1 += 3
            num3 = num1 - num2
            equation = "X - "+str(num2)+" = "+str(num3)
        if(operate == OPERATE_MULTIPLY):
            numbers = myutil.get_randoms(2, 1, 15)
            num1 = numbers[0]
            num2 = numbers[1]
            num3 = num1 * num2
            equation = str(num2)+"X = "+str(num3)
        if(operate == OPERATE_DIVIDE):
            numbers = myutil.get_randoms(2, 2, 15)
            num1 = numbers[0] * numbers[1]
            num2 = numbers[0]
            num3 = numbers[1]
            equation = "X &divide; "+str(num2)+" = "+str(num3)
        
        context['equation'] = equation
        context['operate'] = operate
        context['number1'] = num1
        context['number2'] = num2
        context['number3'] = num3
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'grade5/grade5_equations_calculate.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        num1 = int(request.GET['num1'])
        num2 = int(request.GET['num2'])
        num3 = int(request.GET['num3'])
        try:
            useranswer = int(request.GET['answer'])
        except:
            useranswer = -1
        operate = int(request.GET['operate'])
        if(operate == OPERATE_ADD):
            equation = "X + "+str(num2)+" = "+str(num3)
        if(operate == OPERATE_SUBTRACT):
            equation = "X - "+str(num2)+" = "+str(num3)
        if(operate == OPERATE_MULTIPLY):
            equation = str(num2)+"X = "+str(num3)
        if(operate == OPERATE_DIVIDE):
            equation = "X &divide; "+str(num2)+" = "+str(num3)
        
        success = 0
        if((num1 == useranswer) or ((submittedValue == 'GetAnswer'))):
            success = 1
            useranswer = num1
        
        context['equation'] = equation
        context['number1'] = num1
        context['number2'] = num2
        context['number3'] = num3
        context['operate'] = operate
        if(success == 0):
            context['state'] = '1'
            if(useranswer >= 0):
                context['answer'] = useranswer
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'
        else:
            context['state'] = '0'
            context['answer'] = useranswer
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['button2'] = ''

        return render(request, 'grade5/grade5_equations_calculate.html', context)
