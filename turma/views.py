from django.shortcuts import HttpResponse, render

# Create your views here.

def listarTurma(request):
    return render(request, 'turma/listarTurmas.html')

def cadastrarTurma(request):
    return render(request, 'turma/cadastroTurma.html')

def registroAusencia(request):
    return render(request, 'turma/registroAusencia.html')
