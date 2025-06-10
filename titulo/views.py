from django.shortcuts import render
from titulo.models import Titulo

# Create your views here.

def listarTitulo(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulo': lista_titulos
    }
    
    return render(request, 'titulo/listarTitulos.html', context=contexto)

def cadastrarTitulo(request):
    return render(request, 'titulo/cadastroTitulos.html')
