from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fiveth(request):
    return render(request,'fiveth.html')
def sixth(request):
    return render(request,'sixth.html')
def demon(request):
    return HttpResponse('<h1>Demon Slayer<h1>')