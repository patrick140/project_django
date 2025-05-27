from django.urls import path

from . import views

app_name = 'instrutor'

urlpatterns = [
    path('listaInstrutor', views.listarInstrutor, name='listarInstrutor'),
]