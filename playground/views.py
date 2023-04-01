from django.shortcuts import render
from django.http import HttpResponse
import wolframalpha

# Create your views here.
def say_hello(request):
	# Replace YOUR_APP_ID with your Wolfram API App ID
	client = wolframalpha.Client("GLYJRW-TEH7UK7VYL")

	# Get user input
	query = "solve (x+3)*6=8*x, x>0"

	# Send query to Wolfram API
	res = client.query(query)

	# Print the result
	#print(next(res.results).text)	
	return HttpResponse(next(res.results).text)
	#return HttpResponse("Hello, what's up!")
