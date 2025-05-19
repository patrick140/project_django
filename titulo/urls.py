from django.urls import path

from . import views

urlpatterns = [
    path("titulo/", views.index, name="index"),
]