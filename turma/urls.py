from django.urls import path

from . import views

app_name = 'turma'

urlpatterns = [
    path('listaTurma', views.listarTurma, name='listarTurma'),
    path('cadastraTurma', views.cadastrarTurma, name='cadastrarTurma'),
    path('registraAusencia', views.registroAusencia, name='registroAusencia')
]