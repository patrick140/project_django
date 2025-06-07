from django.urls import path
from utilitarios import utils
from . import views

app_name = 'contatos'

urlpatterns = [
    path('carga/', views.popular_bd, name='popular'),
    path('contato/', views.contato, name='contato'),
]