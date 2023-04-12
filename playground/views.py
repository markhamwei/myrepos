from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import wolframalpha
import json

# Create your views here.


def say_hello(request):
    # Replace YOUR_APP_ID with your Wolfram API App ID
    client = wolframalpha.Client("GLYJRW-TEH7UK7VYL")

    # Get user input
    query = "solve (x+3)*6=8*x, x>0"

    # Send query to Wolfram API
    res = client.query(query)

    # Print the result
    # print(next(res.results).text)
    return HttpResponse(next(res.results).text)
    # return HttpResponse("Hello, what's up!")


def calculate(request):
    # Replace YOUR_APP_ID with your Wolfram API App ID
    client = wolframalpha.Client("GLYJRW-TEH7UK7VYL")
    context = {'content': '', 'year': '2023'}

    # request_body = request.body

    try:
        # Extract the values from the dictionary
        question = request.GET['question']

        # Send query to Wolfram API
        res = client.query(question)
        context['content'] = next(res.results).text

        # Return a response
        return render(request, 'answer.html', context)

    except Exception:
        # Return a bad request response if the request data cannot be decoded or parsed
        context['content'] = 'Invalid query string'
        return render(request, 'answer.html', context)


def my_query(request):
    return render(request, 'query.html')
