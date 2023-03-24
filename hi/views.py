from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    #with dinamic date with form
    instructions = '''
    <h1>Welcome to the CI/CD testing app!</h1>
    <p>Here are some instructions:</p>
    <ul>
        <li>Go to the /hi/name page to say hi to your name.</li>
        <li>Go to the /day/date page to get your age. Format AAAA-MM-DD, example: /day/1990-12-26 </li>
    </ul>
    '''
    return HttpResponse(instructions)

def hi(request, name):
    return HttpResponse("Hello " + name + "!" + " Welcome to the CI/CD testing app.")

def day(request, date):
    date = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.now()
    age = today - date
    return HttpResponse("You are " + str(age.days//365) + " years old.")

def compareAge(request, date, date2):
    date = datetime.strptime(date, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')
    age = date - date2
    return HttpResponse("The difference of age is " + str(age.days//365) + " years.")

def greatherAge (request, date, date2):
    date = datetime.strptime(date, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')
    age = date - date2
    if age.days//365 < 0:
        return HttpResponse("The greather age is " + str(date) + " years.")
    else:
        return HttpResponse("The greather age is " + str(date2) + " years.")
