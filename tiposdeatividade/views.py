from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Olá! Eu sou o index.")

def exibe_mensagem(request):
    t_html = '<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> </head> <body> </body> </html>'
    return HttpResponse(t_html)