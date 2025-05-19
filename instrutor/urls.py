from django.urls import path

from . import views

urlpatterns = [
    path("instrutor/", views.index, name="index"),
]