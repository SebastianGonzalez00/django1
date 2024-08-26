from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("texto", views.texto)
]