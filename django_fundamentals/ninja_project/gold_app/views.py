from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

# Create your views here.

time = datetime.now().strftime("%m/%d/%Y %I:%M%p")
def index(request):
    if 'random' not in request.session:
        request.session['random'] = 0
        request.session["activities"] = []
        
    return render(request, "index.html")

def call(request, num, message):
    request.session['random'] += num
    request.session["activities"].append(message)
    return redirect('/')

def farm_submit(request):
    global time
    num = random.randint(10, 20)
    message = f"Earned {num} golds from the farm!({time}) "
    call(request, num, message)
    return redirect('/')




def cave_submit(request):
    global time
    num = random.randint(5, 10)
    message = f"Earned {num} golds from the cave!({time})"
    call(request, num, message)
    return redirect('/')

def house_submit(request):
    global time
    num = random.randint(0, 5)
    message = f"Earned {num} golds from the house!({time})"
    call(request, num, message)
    return redirect('/')

def casino_submit(request):
    global time
    num = random.randint(-50, 50)  
    if num < 0:
        message = f"Entered a Casino and lost {num} golds... Ouch...({time}) "
        request.session['result'] = "lose"
        
    else:
        message = f"Earned {num} golds from the casino!({time})"
        request.session['result'] = "win"
    call(request, num, message)
    
    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect('/')


