from django.urls import path

from . import views

app_name = 'titulo'

urlpatterns = [
    path('listaTitulo/', views.listarTitulo, name='listarTitulo'),
    path('cadastrarTitulo/', views.cadastrarTitulo, name='cadastrarTitulo'),
    path('cadastroTitulo/', views.cadastroTitulo, name='cadastroTitulo'),
    path('excluir/<int:codigo>', views.excluir, name='excluir_titulo'),
    path('carregar_titulo/<int:codigo>', views.carregar_titulo, name='carregar_titulo'),
    path('atualizar_titulo/', views.atualizar, name='atualizar_titulo'),
]