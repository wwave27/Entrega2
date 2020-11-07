from django.shortcuts import render
from trabajoBD.models import Noticia, Reviews, Lanzamientos
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def home(request):

    noticiasCards = Noticia.objects.all()
    reviewsCards = Reviews.objects.all()
    lanzamientosCards = Lanzamientos.objects.all()

    return render(request,"index.html",{"noticiasCards":noticiasCards,"reviewsCards":reviewsCards, "lanzamientosCards":lanzamientosCards})

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

