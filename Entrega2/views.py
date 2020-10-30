from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

def mainPage(request):
    
    #doc_externo = loader.get_template("index.html")
    doc_externo = get_template("index.html")
    documento = doc_externo.render()
    return HttpResponse(documento)
