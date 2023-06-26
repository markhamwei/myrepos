from django.shortcuts import render, redirect
from django.http import HttpResponse
#import wolframalpha

# Create your views here.
def my_page(request):
	# Replace YOUR_APP_ID with your Wolfram API App ID
	#client = wolframalpha.Client("GLYJRW-TEH7UK7VYL")

	# Get user input
	#query = "solve (x+3)*6=8*x, x>0"

	# Send query to Wolfram API
	#res = client.query(query)

	# Print the result
	#print(next(res.results).text)	
	#return HttpResponse(next(res.results).text)
	if(request.user.is_authenticated):
		return render(request, 'grade5/myhome.html')
	else:
		return redirect('/login')
