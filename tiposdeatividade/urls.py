from django.urls import path

from . import views

app_name = 'tiposdeatividade'

urlpatterns = [
    path('listaTiposAtividade/', views.listarTiposAtividade, name='listarTiposAtividade'),
    path('cadastraTiposAtividade/', views.cadastraTiposAtividade, name='cadastraTiposAtividade'),
    path('cadastroTiposAtividade/', views.cadastroTiposAtividade, name='cadastroTiposAtividade'),
    # path('excluir/<int:codigo>', views.excluir, name='ecluir_atividade'),
    ]