from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import random

def basicsolving_page(request):
    context = {
        'year':'2023'
        }
    input = request.GET
    if('response' in input):
        if(input['submit'] == 'Get answer!'):
            context['state'] = 'correct'
            context['response'] = input['answer']
        else:
            context['state'] = 'correct' if input['response'] == input['answer'] else 'incorrect'
            context['response'] = input['response']
        context['answer'] = input['answer']
        context['varname'] = input['varname']
        context['problem'] = input['problem']
    else:
        context['state'] = 'question'
        answer = str(myutil.get_randoms(1, 1, 10)[0])
        context['answer'] = answer
        var = random.sample('abcdefghjkmnpqrstwyz',1)[0]
        context['varname'] = var
        op1 = random.sample('+-*',1)[0]
        const1 = str(random.randint(1, 10))
        op2 = random.sample('+-*',1)[0]
        const2 = str(random.randint(1, 10))
        const3 = eval(f'{answer} {op1} {const1} {op2} {const2}')
        context['problem'] = f'{var} {op1} {const1} {op2} {const2} = {const3}'.replace('*','×')
    
    return render(request, 'new/grade6BasicSolving.html', context)