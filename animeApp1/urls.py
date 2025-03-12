from django.urls import path
from . import views

app_name = "animeApp1"

urlpatterns = [
    path("", views.pages),
    # path("<path:path_value>", views.pages),
    path('welcome/', views.pages, name='Welcome'),
    path('directors/', views.pages, name='Directors'),
    path('top5/', views.pages, name='Top5'),
    path('store/', views.pages, name='Store'),
    path('studio/', views.pages, name='Studio'),
    path('education/', views.pages, name='Edu'),
    path('task/', views.task_11_01, name='Task_01'),
    path('task/<str:food>/', views.task_11_02, name='Task_02'),
    path('task/<str:food>/<str:cals>/', views.task_11_02, name='Task_02'),
]
