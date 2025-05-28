from django.shortcuts import HttpResponse, render

# Create your views here.

def listarTiposAtividade(request):
    return render(request, 'tiposdeatividade/listarTiposAtividade.html')

def cadastroTiposAtividade(request):
    return render(request, 'tiposdeatividade/cadastroTiposAtividade.html')

