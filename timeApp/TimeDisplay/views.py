from django.shortcuts import render #HttpResponse
from time import localtime,strftime,time,strptime
from datetime import datetime

# Create your views here.
def index(request):
    context ={
        "time": strftime("%A,%Y-%B-%d %H:%M %p", localtime())
        #"time": strptime("%A,%Y-%B-%d %H:%M %p", gmtime())
        #"day": strptime("08-Aug-91","%A,%B")
        #"time": time.strptime("08-Aug-91","%d-%B-%y")
    }
    return render(request, "index.html", context)
    #return HttpResponse("This is my response!")

def time(request):
    datetime1 = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    return render(request,"index.html",datetime1)
print(datetime1)

