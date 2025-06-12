from django.shortcuts import render, redirect
from titulo.models import Titulo
from titulo.forms import TituloForm
from instrutor.models import Instrutor

# Create your views here.

def listarTitulo(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulo': lista_titulos
    }
    
    return render(request, 'titulo/listarTitulos.html', context=contexto)

def cadastroTitulo(request):
    return render(request, 'titulo/cadastroTitulos.html')

# ação de cadastrar um titulo
def cadastrarTitulo(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao = dados_titulo['descricao']
        )
        titulo.save()
    return render(request, 'titulo/cadastroTitulos.html')

#excluir um titulo
def excluir(request, codigo):
    titulo = Titulo.objects.get(pk=codigo)

    instrutores = Instrutor.objects.filter(codigo_titulo=codigo)
    if not instrutores:
        titulo.delete()

    return redirect('titulo:listarTitulo')

