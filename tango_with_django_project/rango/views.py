from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {}
    context_dict['boldmessage'] = "Ola BSI6, este texto veio da view"
    context_dict["autor"] = "Bruno Tissi"

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    texto = '''
    <h1> Sobre o Rango </h1>
    Essa e a pagina sobre o Rango.
    <br/><a href='/rango/'>Index</a>
    '''
    return HttpResponse(texto)
