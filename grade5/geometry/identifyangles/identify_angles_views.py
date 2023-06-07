from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.
ACUTE_ANGLE = 0
RIGHT_ANGLE = 1
OBTUSE_ANGLE = 2
STRAIGHT_ANGLE = 3
REFLEX_ANGLE = 4

def angles_identify_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    lastAngleType = -1
    specifyAngleType = -1 #to specify the angle type instead of randomly generate
    try:
        specifyAngleType = int(request.GET['specifyAngleType'])
    except Exception:
        pass
    
    try:
        submittedValue = request.GET['Submit'] #make sure the next random question is different angle type.
        if(submittedValue == 'Next'):
            lastAngleType = int(request.GET['saveType'])
    except Exception:
        pass
    
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        if(specifyAngleType < 0):
            angleType = myutil.get_random(0, 4)
            while(angleType == lastAngleType):
                angleType = myutil.get_random(0, 4)
        else:
            angleType = specifyAngleType
        if(angleType == ACUTE_ANGLE):
            angleDegree = myutil.get_random(1, 89)
        if(angleType == RIGHT_ANGLE):
            angleDegree = 90
        if(angleType == OBTUSE_ANGLE):
            angleDegree = myutil.get_random(91, 179)
        if(angleType == STRAIGHT_ANGLE):
            angleDegree = 180
        if(angleType == REFLEX_ANGLE):
            angleDegree = myutil.get_random(181, 359)
            
        context['angleDegree'] = angleDegree
        context['flag'] = '='
        context['cmd'] = 'Submit'
        context['saveType'] = angleType
        return render(request, 'new/grade5angles_Identify.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        useranswer = -1
        try:
            useranswer = int(request.GET['angleType'])
        except Exception:
            pass
        saveType = int(request.GET['saveType'])
        angleDegree = request.GET['angleDegree']
        success = 0
        if((saveType == useranswer) or (submittedValue == 'GetAnswer')):
            success = 1
            useranswer = saveType
        
        context['angleDegree'] = angleDegree
        context['saveType'] = saveType
        if(useranswer == ACUTE_ANGLE):
            context['acute'] = 'checked'
        if(useranswer == RIGHT_ANGLE):
            context['right'] = 'checked'
        if(useranswer == OBTUSE_ANGLE):
            context['obtuse'] = 'checked'
        if(useranswer == STRAIGHT_ANGLE):
            context['straight'] = 'checked'
        if(useranswer == REFLEX_ANGLE):
            context['reflex'] = 'checked'
            
        if(success == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
        else:
            context['state'] = '1'
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'

        return render(request, 'new/grade5angles_Identify.html', context)
