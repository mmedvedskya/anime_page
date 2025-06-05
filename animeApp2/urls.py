from django.urls import path
from . import views

app_name = "animeApp2"

urlpatterns = [
    path("education/", views.my_edu, name="Edu"),
]
