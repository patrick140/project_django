from django.shortcuts import render, redirect
from tiposdeatividade.models import tiposDeAtividade
from tiposdeatividade.forms import TiposDeAtividadeForm

# Create your views here.

def listarTiposAtividade(request):
    return render(request, 'tiposdeatividade/listarTiposAtividade.html')

def cadastroTiposAtividade(request):
    return render(request, 'tiposdeatividade/cadastroTiposAtividade.html')

def cadastraTiposAtividade(request):
    return

