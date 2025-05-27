from django.shortcuts import HttpResponse, render

# Create your views here.

def listarInstrutor(request):
    return render(request, 'instrutor/listarInstrutores.html')