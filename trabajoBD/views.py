from django.shortcuts import render
from trabajoBD.models import Noticia, Reviews, Lanzamientos
from django.shortcuts import get_object_or_404
from django.db.models import Q

#Rest Framwork
from rest_framework import viewsets
from .serializer import NoticiaSerializer

#Consumo API
from urllib.request import urlopen
import json

# Create your views here.

def home(request):

    #Temperatura
    url= "https://api.gael.cl/general/public/clima/SCQN"
    datos = urlopen(url).read()
    clima = json.loads(datos)
    temperatura = clima["Temp"]

    noticiasCards = Noticia.objects.all()
    reviewsCards = Reviews.objects.all()
    lanzamientosCards = Lanzamientos.objects.all()

    return render(request,"index.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards, "climaStgo":temperatura})

def buscar(request):

    if request.GET["txtBusqueda"] is not None and request.GET["txtBusqueda"].strip() !=' ':

        busqueda = request.GET["txtBusqueda"]

        noticiasCards = Noticia.objects.filter(titulo__icontains=busqueda)
        reviewsCards = Reviews.objects.filter(titulo__icontains=busqueda)
        lanzamientosCards = Lanzamientos.objects.filter(titulo__icontains=busqueda)

        return render(request, "search.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards,"query":busqueda})
    
    else:
        mensaje:"no se ingresó información"

        return HttpResponse(mensaje)


def register(request):
    return render(request, "register.html")

def ps5news(request):

    noticiasCards = Noticia.objects.all()
    reviewsCards = Reviews.objects.all()
    lanzamientosCards = Lanzamientos.objects.all()

    return render(request, "ps5.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards})

def switchnews(request):    

    noticiasCards = Noticia.objects.all()
    reviewsCards = Reviews.objects.all()
    lanzamientosCards = Lanzamientos.objects.all()

    return render(request, "switch.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards})

def pcnews(request):  

    noticiasCards = Noticia.objects.all()
    reviewsCards = Reviews.objects.all()
    lanzamientosCards = Lanzamientos.objects.all()

    return render(request, "pc.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards})

def retronews(request):

    noticiasCards = Noticia.objects.all()
    reviewsCards = Reviews.objects.all()
    lanzamientosCards = Lanzamientos.objects.all()


    return render(request, "retro.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards})

def xboxnews(request):  

    noticiasCards = Noticia.objects.all()
    reviewsCards = Reviews.objects.all()
    lanzamientosCards = Lanzamientos.objects.all()
  
    return render(request, "xbox.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards})


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

#def password_reset(request):
#    return render(request, 'password_reset.html')

#def password_reset_done(request):
#    return render(request, 'password_reset_done.html')


#def password_reset_confirm(request):
#    return render(request, 'password_reset_confirm.html')


#def password_reset_complete(request):
#    return render(request, 'password_reset_complete.html')
