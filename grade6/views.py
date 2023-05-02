from django.shortcuts import render

# Create your views here.

def grade6_home(request):
    return render(request, 'new/grade6home.html')