from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from trabajoBD.models import Usuario

def mainPage(request):
    
    #doc_externo = loader.get_template("index.html")
    doc_externo = get_template("index.html")
    documento = doc_externo.render()
    return HttpResponse(documento)

def buscarUsuario(request):
    return render(request,"buscar_usuario.html")

#def busca_usuario(request):
#    if request.GET["txtNombre"]:

#        usuario_buscar=request.GET["txtNombre"]

        # info_usuario=Usuario.objects.filter(nombre__icontains=usuario_buscar)

#        return render(request,"resultado_busqueda", {"usuario":info_usuario,"query":usuario_buscar})
#    else:
#        mensaje= "No se encontraron coincidencias."
#    return HttpResponse(mensaje)