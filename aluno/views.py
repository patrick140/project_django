from django.shortcuts import HttpResponse, render

# Create your views here.

def inicio(request):
    return render(request, 'templates/escola.html')

def listar(request):
    return render(request, 'aluno/listarAluno.html')

def cadastrar(request):
    return render(request, 'aluno/cadastroAluno.html')