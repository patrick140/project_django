from django.shortcuts import HttpResponse, render

# Create your views here.

def contato(request):
    return render(request, 'utilitarios/contato.html')
