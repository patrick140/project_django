from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Olá! Eu sou o index e vim por turma/.")
