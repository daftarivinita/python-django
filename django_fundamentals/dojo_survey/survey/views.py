from django.shortcuts import render, redirect

transports = ["bike", "car", "boat", "airplane"]

def index(request):
    context = {
        "transportation" : transports
    }
    return render(request, "index.html", context)
    

def submit(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['language'] = request.POST['language']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']
        if 'gender' in request.POST:
            request.session['gender'] = request.POST['gender']
        else:
            request.session['gender'] = "Not Specified"
        request.session['transport'] = request.POST.getlist('transport')
    return redirect("/result")

def result(request):
    return render(request, "result.html")
def back(request):
    return redirect("/")
   

#why request.session['name'] = request.POST['name'] not work inside result method.

#what if i do not put any input inside radio or checkbox, it throws an error. how to fix it?


