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
        <li>Go to the /compare/:date/:date1 page to compare in years the two ages. Format AAAA-MM-DD, example: /day/1990-12-26 </li>
        <li>Go to the /greather/:date/:date1 page to get the greather age of two birthdays. Format AAAA-MM-DD, example: /day/1990-12-26 </li>
        <li>Go to the star/sign/:day/:month page to get the star sign of a birthday. Format DD/MM, example: /star/sign/19/01 </li>
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
    
def signo_zodiacal(request, day, month):
    """
    Esta función toma como argumentos el día y el month de nacimiento de una persona,
    y devuelve su signo zodiacal.
    """
    day = int(day)
    month = int(month)
    # Comprobamos que los argumentos son válidos
    if not isinstance(day, int) or not isinstance(month, int):
        raise TypeError("Los argumentos deben ser enteros.")
    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError("La fecha ingresada no es válida.")
    # calculate all zodiacal sign
    if (month == 1 and day >= 21) or (month == 2 and day <= 19):
        return HttpResponse("Acuario")
    elif (month == 2 and day >= 20) or (month == 3 and day <= 20):
        return HttpResponse("Piscis")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 20):
        return HttpResponse("Aries")
    elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
        #return
        return HttpResponse("Tauro")
    elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
        return HttpResponse("Géminis")
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return HttpResponse("Cáncer")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 23):
        return HttpResponse("Leo")
    elif (month == 8 and day >= 24) or (month == 9 and day <= 23):
        return HttpResponse("Virgo")
    elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
        return HttpResponse("Libra")
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return HttpResponse("Escorpio")
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return HttpResponse("Sagitario")
    elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
        return HttpResponse("Capricornio")
    else:
        return HttpResponse("Fecha no válida")
