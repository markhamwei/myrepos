from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import random

def rh(str):
    return '('+str+')' if '+' in str else str

#makes a random equation using a fixed number of operations and variables->value maps
def random_equation(ops, vars, pool):
    if(ops == 0):
        if(random.randint(0,2)==1):
            k = random.choice(pool)
            return (str(k), vars[k])
        else:
            k = random.randint(1, 10)
            return (str(k), k)
    else:
        split = random.randint(0, ops-1)
        x,y = random_equation(split, vars, pool),random_equation(ops-split-1, vars, pool)
        if(random.randint(0,2)==0):
            return (x[0]+' + '+y[0], x[1]+y[1])
        else:
            return ('{a} × {b}'.format(a=rh(x[0]),b=rh(y[0])), x[1]*y[1])

def evaluating_page(request):
    input = request.GET
    context={
        'year': '2023',
        'state':'question',
        'definitions':''
        }
    if('response' in input):
        if(input['submit'] == 'Submit!'):
            context['state'] = 'correct' if input['response'] == input['answer'] else 'incorrect'
            context['problem'] = input['problem']
            context['definitions'] = input['definitions']
            context['response'] = input['response']
            context['answer'] = input['answer']
        elif(input['submit'] == 'Get answer!'):
            context['state'] = 'correct'
            context['problem'] = input['problem']
            context['definitions'] = input['definitions']
            context['response'] = input['response']
            context['answer'] = input['answer']

    else:
        pool = random.sample('abcdefghjkmnpqrsuvwyz', random.randint(1, 3))
        vars = {}
        for i in pool:
            vars[i] = random.randint(1, 10)
        
        context['problem'], context['answer'] = random_equation(random.randint(1, 3), vars, pool)
        for i in pool:
            if(i in context['problem']):
                context['definitions'] += '{} = {}\n\n'.format(i, vars[i])
        
    return render(request, 'new/grade6Evaluating.html', context)