from django.urls import path

from . import views

app_name = 'tiposdeatividade'

urlpatterns = [
    path('listaTiposAtividade', views.listarTiposAtividade, name='listarTiposAtividade'),
    path('cadastraTiposAtividade', views.cadastroTiposAtividade, name='cadastroTiposAtividade'),
    ]