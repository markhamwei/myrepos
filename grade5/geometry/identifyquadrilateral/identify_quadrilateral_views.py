from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.
POLY_SQUARE = 0
POLY_RECTANGLE = 1
POLY_PARALLELOGRAM = 2
POLY_RHOMBUS = 3
POLY_TRAPEZOID = 4

def quadrilateral_identify_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    lastPolyType = -1
    specifyPolyType = -1 #to specify the poly type instead of randomly generate
    try:
        specifyPolyType = int(request.GET['specifyPolyType'])
    except Exception:
        pass
    
    try:
        submittedValue = request.GET['Submit'] #make sure the next random question is different angle type.
        if(submittedValue == 'Next'):
            lastPolyType = int(request.GET['saveType'])
    except Exception:
        pass
    
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        if(specifyPolyType < 0):
            polyType = myutil.get_random(0, 4)
            while(polyType == lastPolyType):
                polyType = myutil.get_random(0, 4)
        else:
            polyType = specifyPolyType
        if(polyType == POLY_SQUARE):
            angleDegree = 90
            side1 = myutil.get_random(70, 100)
            side2 = side1
            trapezoidOffset = 0
        if(polyType == POLY_RECTANGLE):
            angleDegree = 90
            side1 = myutil.get_random(100, 120)
            side2 = side1 - myutil.get_random(40, 50)
            trapezoidOffset = 0
        if(polyType == POLY_PARALLELOGRAM):
            angleDegree = myutil.get_random(50, 80)
            side1 = myutil.get_random(100, 120)
            side2 = side1 - myutil.get_random(40, 50)
            trapezoidOffset = 0
        if(polyType == POLY_RHOMBUS):
            angleDegree = myutil.get_random(50, 80)
            side1 = myutil.get_random(70, 100)
            side2 = side1
            trapezoidOffset = 0
        if(polyType == POLY_TRAPEZOID):
            angleDegree = myutil.get_random(50, 90)
            side1 = myutil.get_random(100, 120)
            side2 = side1 - myutil.get_random(40, 60)
            trapezoidOffset = myutil.get_random(20, 50)
            
        context['side1'] = side1
        context['side2'] = side2
        context['trapezoidOffset'] = trapezoidOffset
        context['angleDegree'] = angleDegree
        context['flag'] = '='
        context['cmd'] = 'Submit'
        context['saveType'] = polyType
        return render(request, 'grade5/grade5quadrilateral_Identify.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        useranswer = -1
        try:
            useranswer = int(request.GET['polyType'])
        except Exception:
            pass
        saveType = int(request.GET['saveType'])
        angleDegree = request.GET['angleDegree']
        trapezoidOffset = request.GET['trapezoidOffset']
        side1 = request.GET['side1']
        side2 = request.GET['side2']
        success = 0
        if((saveType == useranswer) or (submittedValue == 'GetAnswer')):
            success = 1
            useranswer = saveType
        
        context['angleDegree'] = angleDegree
        context['saveType'] = saveType
        context['side1'] = side1
        context['side2'] = side2
        context['trapezoidOffset'] = trapezoidOffset
        if(useranswer == POLY_SQUARE):
            context['square'] = 'checked'
        if(useranswer == POLY_RECTANGLE):
            context['rectangle'] = 'checked'
        if(useranswer == POLY_PARALLELOGRAM):
            context['parallelogram'] = 'checked'
        if(useranswer == POLY_RHOMBUS):
            context['rhombus'] = 'checked'
        if(useranswer == POLY_TRAPEZOID):
            context['trapezoid'] = 'checked'
            
        if(success == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
        else:
            context['state'] = '1'
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'

        return render(request, 'grade5/grade5quadrilateral_Identify.html', context)
