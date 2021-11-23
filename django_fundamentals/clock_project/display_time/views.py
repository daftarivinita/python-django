from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def method_name(request):
    context = {
        "month": strftime("%b %d, %Y", gmtime()),
        "day": strftime("%A", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

#  strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
# 'Thu, 28 Jun 2001 14:17:15 +0000'