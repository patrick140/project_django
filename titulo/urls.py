from django.urls import path

from . import views

app_name = 'titulo'

urlpatterns = [
    path('listaTitulo', views.listarTitulo, name='listarTitulo'),
    path('cadastraTitulo', views.cadastrarTitulo, name='cadastrarTitulo')
]