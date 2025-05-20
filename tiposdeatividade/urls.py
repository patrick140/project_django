from django.urls import path

from . import views

urlpatterns = [
    path("loureiro/", views.index, name="index"),
    path('exibemensagem', views.exibe_mensagem, name="Exibir_mensagem"),
]