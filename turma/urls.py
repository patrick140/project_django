from django.urls import path

from . import views

urlpatterns = [
    path("turma/", views.index, name="index"),
]