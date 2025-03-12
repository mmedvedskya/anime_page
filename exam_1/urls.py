from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.error),
    path('animeApp1/', include("animeApp1.urls")),
]
