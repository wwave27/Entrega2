from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def register(request):
    return render(request, "register.html")

def ps5news(request):
    return render(request, "ps5.html")

def switchnews(request):    
    return render(request, "switch.html")