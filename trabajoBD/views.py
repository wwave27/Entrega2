from django.shortcuts import render
from trabajoBD.models import Noticia, Reviews, Lanzamientos

# Create your views here.

def home(request):

    noticiasCards = Noticia.objects.all()
    reviewsCards = Reviews.objects.all()
    lanzamientosCards = Lanzamientos.objects.all()

    return render(request,"index.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards})

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