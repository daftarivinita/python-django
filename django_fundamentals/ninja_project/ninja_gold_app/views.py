from django.shortcuts import render, redirect
import random
from datetime import datetime

locations = {
    "farm" : (10, 20),
    "cave" : (5,10),
    "house": (2,5),
    "casino": (-50, 50)
}
# Create your views here.
def index1(request):
    # 
    if 'counter' not in request.session or 'activities' not in request.session:
        request.session['counter'] = 0
        request.session['activities'] = []
    
    return render(request, "index.html")



def process_money(request):
    time = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    request.session['result'] = 'win'
    if request.method == "POST":
        gold = request.session['counter']
        location = request.POST['location']
        building = locations[location]
        goldEarned = random.randint(building[0], building[1])
        gold = gold + goldEarned
        request.session['counter'] = gold
        
        
    if goldEarned <0:
        message = f'<li class = "lose">Enterd a {location} and lost {goldEarned} ouch... ({time})</li>'
        #request.session['result'] = "lose"
    else: 
        message = f'<li class = "win">Earned {goldEarned} golds from the {location}({time})</li>'
        #request.session['result'] = 'win'
    request.session['activities'].append(message)
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')