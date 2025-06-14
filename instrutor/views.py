from django.shortcuts import HttpResponse, render
from instrutor.models import Instrutor
from titulo.models import Titulo
from instrutor.forms import InstrutorForm

# Create your views here.

def listarInstrutor(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutor': lista_instrutor,
        
    }
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)

def CadastrarInstrutor(request):
    form = InstrutorForm(request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        instrutor = Instrutor(
            nome = dados_instrutor['nome'],
            rg = dados_instrutor['rg'],
            dataNascimento = dados_instrutor['dataNascimento'],
            telefone = dados_instrutor['telefone'],
            ddd = dados_instrutor['ddd'],
            codigo_titulo = dados_instrutor['codigo_titulo']
        )
        instrutor.save()
    return render(request, 'instrutor/cadastroInstrutor.html')

def CadastroInstrutor(request):
    cadastra_instrutor = Titulo.objects.all()
    contexto = {
        'titulo': cadastra_instrutor,
        
    }
    return render(request, 'instrutor/cadastroInstrutor.html', context=contexto)