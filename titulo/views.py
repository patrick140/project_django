from django.shortcuts import HttpResponse, render

# Create your views here.

def listarTitulo(request):
    return render(request, 'titulo/cadastroTitulos.html')

def cadastrarTitulo(request):
    return render(request, 'titulo/listarTitulos.html')
