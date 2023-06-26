from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math

# Create your views here.

def grids_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        randoms = myutil.get_randoms(2, 11, 99)
        location1 = randoms[0]
        location2 = randoms[1]
        if(location1 == location2):
            location2 = 99 - location1
            
        rloc1 = int(location1%10)
        cloc1 = int(location1/10)
        if(rloc1 == 0):
            location1 += 1
            rloc1 = 1
        rloc2 = int(location2%10)
        cloc2 = int(location2/10)
        if(rloc2 == 0):
            location2 += 1
            rloc2 = 1
        
        if(rloc1 < rloc2):
            context['upordown'] = 'up '+str(rloc2 - rloc1)
        else:
            context['upordown'] = 'down '+str(rloc1 - rloc2)
            
        if(cloc1 < cloc2):
            context['leftorright'] = 'right '+str(cloc2 - cloc1)
        else:
            context['leftorright'] = 'left '+str(cloc1 - cloc2)
        
        context['location'] = str(chr(64+cloc1))+str(rloc1)
        context['gridx1'] = str(cloc1)+','
        context['gridy1'] = str(rloc1)
        context['loc1'] = location1
        context['loc2'] = location2
        context['flag'] = '='
        context['cmd'] = 'Submit'
        return render(request, 'new/grade5grids.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        useranswer = ''
        try:
            useranswer = request.GET['newlocation'].upper()
        except Exception:
            pass
        location1 = int(request.GET['loc1'])
        rloc1 = int(location1%10)
        cloc1 = int(location1/10)
        location2 = int(request.GET['loc2'])
        rloc2 = int(location2%10)
        cloc2 = int(location2/10)
        if(rloc1 < rloc2):
            context['upordown'] = 'up '+str(rloc2 - rloc1)
        else:
            context['upordown'] = 'down '+str(rloc1 - rloc2)
            
        if(cloc1 < cloc2):
            context['leftorright'] = 'right '+str(cloc2 - cloc1)
        else:
            context['leftorright'] = 'left '+str(cloc1 - cloc2)
        
        context['location'] = str(chr(64+cloc1))+str(rloc1)
        newLocation = str(chr(64+cloc2))+str(rloc2)
        success = 0
        if((newLocation == useranswer) or (submittedValue == 'GetAnswer')):
            success = 1
            useranswer = newLocation
            context['gridx1'] = str(cloc1)+','
            context['gridy1'] = str(rloc1)+','
            context['gridx2'] = str(cloc2)+','
            context['gridy2'] = str(rloc2)
        else:
            context['gridx1'] = str(cloc1)+','
            context['gridy1'] = str(rloc1)
        
        context['loc1'] = location1
        context['loc2'] = location2
        context['newlocation'] = useranswer
            
        if(success == 1):
            context['flag'] = 'v'
            context['cmd'] = 'Next'
            context['state'] = '0'
        else:
            context['state'] = '1'
            context['flag'] = 'x'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'

        return render(request, 'new/grade5grids.html', context)
