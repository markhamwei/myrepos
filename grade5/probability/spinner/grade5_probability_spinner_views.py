from django.shortcuts import render
from django.http import HttpResponse
from mylib import myutil
import math
from fractions import Fraction

# Create your views here.

def grade5_probability_spinner_page(request):
    context = {'number1': '', 'number2': '', 'state': '0', 'year': '2023', 'answer': '', 'button2': ''
               }
    state = 0
    try:
        state = int(request.GET['state'])
    except Exception:
        state = 0
    if (state == 0):  # the initial state
        context['state'] = '1'
        slices = myutil.get_random(4,15)
        maxnumber = myutil.get_random(2,min(slices-2, 8))
        myarray = myutil.get_randoms(slices, 1, maxnumber)
        mydict = myutil.getItemsCount(myarray)
        if(len(mydict) == 1):
            myarray[len(myarray) - 1] += 1 
            if(myarray[len(myarray) - 1] > 8): #only up to 8 different colors
                myarray[len(myarray) - 1] = 1
            mydict = myutil.getItemsCount(myarray)
        sorted_by_values = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
        mySortedDict = dict(sorted_by_values)
        keys = list(mySortedDict.keys())
        value1 = mySortedDict[keys[0]]
        value2 = mySortedDict[keys[1]]
        #print("dict: "+str(mySortedDict))
        #print("myarray: "+str(myarray))
        if(value1 == value2):
            for i in range(len(myarray)):
                if(myarray[i] == keys[0]):
                    myarray[i] = keys[1]
                    #print("myarray: "+str(myarray))
                    break

        context['myarray'] = myutil.myList2Str(myarray, False)
        context['cmd'] = 'Submit'
        return render(request, 'grade5/grade5_probability_spinner.html', context)
    if (state == 1):  # which means user clicked submit in the initial page
        submittedValue = request.GET['Submit']
        try:
            number = int(request.GET['number'])
        except:
            number = -1
        fractionstr = request.GET['fraction']
        myarrayStr = request.GET['myarray']
        myarray = myutil.myStr2List(myarrayStr)
        mydict = myutil.getItemsCount(myarray)
        sorted_by_values = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
        mySortedDict = dict(sorted_by_values)
        keys = list(mySortedDict.keys())
        if(number == int(keys[0])):
            success1 = 1
        else:
            success1 = 0
            
        fraction2 = Fraction(int(mySortedDict[keys[0]]), len(myarray))
        try:
            fraction1 = Fraction(fractionstr)
            if((fraction1._numerator == fraction2._numerator) and 
               (fraction1._denominator == fraction2._denominator)):
                success2 = 1
                tmpStr = str(fraction1._numerator)+"/"+str(fraction1._denominator)
                if(tmpStr != fractionstr.strip()):
                    context['simplifyFlag'] = ' Better to Simplify'
            else:
                success2 = 0
        except:
            print("except here!")
            success2 = 0
            
        if(submittedValue == 'GetAnswer'):
            success1 = 1
            success2 = 1
            number = int(keys[0])
            fractionstr = str(fraction2)
        
        context['myarray'] = myarrayStr
        if(success1 == 0) or (success2 == 0):
            print(str(success1)+"  "+str(success2))
            context['state'] = '1'
            if(success1 == 0):
                context['flag1'] = 'x'
            else:
                context['flag1'] = 'v'
            if(success2 == 0):
                context['flag2'] = 'x'
            else:
                context['flag2'] = 'v'
            context['cmd'] = 'Retry'
            context['button2'] = 'GetAnswer'
            if(number >= 0):
                context['number'] = number
            context['fraction'] = fractionstr
        else:
            context['state'] = '0'
            context['flag1'] = 'v'
            context['flag2'] = 'v'
            context['cmd'] = 'Next'
            context['button2'] = ''
            context['number'] = number
            context['fraction'] = fractionstr

        return render(request, 'grade5/grade5_probability_spinner.html', context)
