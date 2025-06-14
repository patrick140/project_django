from django.urls import path

from . import views

app_name = 'instrutor'

urlpatterns = [
    path('listaInstrutor/', views.listarInstrutor, name='listarInstrutor'),
    path('cadastraInstrutor/', views.CadastrarInstrutor, name='CadastrarInstrutor'),
    path('cadastroInstrutor/', views.CadastroInstrutor, name='CadastroInstrutor'),
]