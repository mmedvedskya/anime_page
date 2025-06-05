from django.urls import path
from . import views

app_name = "animeApp1"

urlpatterns = [
    path("", views.pages),
    # path("<path:path_value>", views.pages),
    path('welcome/', views.pages, name='Welcome'),
    path('directors/', views.pages, name='Directors'),
    path('top5/', views.pages, name='Top5'),
    # path('store/', views.pages, name='Store'),
    path('feedback/', views.pages, name='Feedback'),
    path('studio/', views.pages, name='Studio'),
]
