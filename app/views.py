from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    dt=datetime.datetime.now()
    d={'data':'Hey there priyA','datE':dt,'d':2,'c':0,'m':12}
    return render(request,'filters.html',d)