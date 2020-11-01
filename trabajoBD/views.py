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

def pcnews(request):    
    return render(request, "pc.html")

def retronews(request):    
    return render(request, "retro.html")

def xboxnews(request):    
    return render(request, "xbox.html")