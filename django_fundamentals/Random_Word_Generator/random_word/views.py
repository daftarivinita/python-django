from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
        request.session['lst'] = []
    word = get_random_string(length=14)
    request.session['num'] = word
    request.session['counter'] += 1

    request.session['lst'].append(word)
    return render(request, "index.html")

# def generate(request):
#     return redirect("/")

def reset(request):
    request.session.flush()
    return redirect("/")
    
    