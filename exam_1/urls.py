from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.error),
    path('admin/', admin.site.urls),
    path('animeApp1/', include("animeApp1.urls")),
    path('animeApp2/', include("animeApp2.urls")),

]
