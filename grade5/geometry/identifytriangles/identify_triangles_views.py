from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.
Acute_Equilateral = 0
Acute_Isosceles = 1
Acute_Scalene = 2
Obtuse_Isosceles = 3
Obtuse_Scalene = 4
Right_Isosceles = 5
Right_Scalene = 6

def triangles_identify_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    lastTringleType = -1
    specifyTringleType = -1 #to specify the triangle type instead of randomly generate
    try:
        specifyTringleType = int(request.GET['specifyTriangleType'])
    except Exception:
        pass
    
    try:
        submittedValue = request.GET['Submit'] #make sure the next random question is different angle type.
        if(submittedValue == 'Next'):
            lastTringleType = int(request.GET['saveType'])
    except Exception:
        pass
    
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        if(specifyTringleType < 0):
            triangleType = myutil.get_random(0, 6)
            while(triangleType == lastTringleType):
                triangleType = myutil.get_random(0, 6)
        else:
            triangleType = specifyTringleType
        if(triangleType == Acute_Equilateral):
            angle1 = 60
            angle2 = 60
        if(triangleType == Acute_Isosceles):
            angle1 = myutil.get_random(50, 85)
            if(angle1 == 60):
                angle1 += 5
            angle2 = angle1
        if(triangleType == Acute_Scalene):
            angle1 = myutil.get_random(50, 85)
            angle2 = myutil.get_random(50, 85)
            angle3 = 180 - angle1 - angle2
            angle1 = min(angle1, angle2, angle3)
            angle2 = max(angle1, angle2, angle3)
            angle1 -= 1
            angle2 += 1
        if(triangleType == Obtuse_Isosceles):
            angle1 = myutil.get_random(100, 160)
            if(angle1%2 == 1):
                angle1 -= 1
            angle2 = int((180-angle1) / 2)
        if(triangleType == Obtuse_Scalene):
            angle1 = myutil.get_random(100, 160)
            if(angle1%2 == 1):
                angle1 -= 1
            angle2 = int((180-angle1) / 2)
            delta = myutil.get_random(1, angle2-10)
            angle2 -= delta
        if(triangleType == Right_Isosceles):
            angle1 = 90
            angle2 = 45
        if(triangleType == Right_Scalene):
            angle1 = 90
            angle2 = 45
            delta = myutil.get_random(1, 35)
            angle2 -= delta
            
        context['angle1'] = angle1
        context['angle2'] = angle2
        context['flag'] = '='
        context['cmd'] = 'Submit'
        context['saveType'] = triangleType
        return render(request, 'grade5/grade5triangles_Identify.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        useranswer1 = "none"
        useranswer2 = "none"
        useranswer = -1
        try:
            useranswer1 = request.GET['group1']
            useranswer2 = request.GET['group2']
        except Exception:
            pass

        saveType = int(request.GET['saveType'])
        angle1 = request.GET['angle1']
        angle2 = request.GET['angle2']
        if((useranswer1 == 'acute') and (useranswer2 == 'equilateral')):
            useranswer = Acute_Equilateral
        if((useranswer1 == 'acute') and (useranswer2 == 'isosceles')):
            useranswer = Acute_Isosceles
        if((useranswer1 == 'acute') and (useranswer2 == 'scalene')):
            useranswer = Acute_Scalene
        if((useranswer1 == 'obtuse') and (useranswer2 == 'isosceles')):
            useranswer = Obtuse_Isosceles
        if((useranswer1 == 'obtuse') and (useranswer2 == 'scalene')):
            useranswer = Obtuse_Scalene
        if((useranswer1 == 'right') and (useranswer2 == 'isosceles')):
            useranswer = Right_Isosceles
        if((useranswer1 == 'right') and (useranswer2 == 'scalene')):
            useranswer = Right_Scalene
        success = 0
        if((saveType == useranswer) or (submittedValue == 'GetAnswer')):
            success = 1
            useranswer = saveType
            if(useranswer == Acute_Equilateral):
                useranswer1 = 'acute'
                useranswer2= 'equilateral'
            if(useranswer == Acute_Isosceles):
                useranswer1 = 'acute'
                useranswer2= 'isosceles'
            if(useranswer == Acute_Scalene):
                useranswer1 = 'acute'
                useranswer2= 'scalene'
            if(useranswer == Obtuse_Isosceles):
                useranswer1 = 'obtuse'
                useranswer2= 'isosceles'
            if(useranswer == Obtuse_Scalene):
                useranswer1 = 'obtuse'
                useranswer2= 'scalene'
            if(useranswer == Right_Isosceles):
                useranswer1 = 'right'
                useranswer2= 'isosceles'
            if(useranswer == Right_Scalene):
                useranswer1 = 'right'
                useranswer2= 'scalene'
        
        context['angle1'] = angle1
        context['angle2'] = angle2
        context['saveType'] = saveType
        if(useranswer1 == 'acute'):
            context['acute'] = 'checked'
        if(useranswer1 == 'obtuse'):
            context['obtuse'] = 'checked'
        if(useranswer1 == 'right'):
            context['right'] = 'checked'
        if(useranswer2 == 'equilateral'):
            context['equilateral'] = 'checked'
        if(useranswer2 == 'isosceles'):
            context['isosceles'] = 'checked'
        if(useranswer2 == 'scalene'):
            context['scalene'] = 'checked'
            
        if(success == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
        else:
            context['state'] = '1'
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'

        return render(request, 'grade5/grade5triangles_Identify.html', context)
