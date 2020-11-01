from django.urls import path,include
from trabajoBD import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.home, name="index"),
    path('registrarse/', views.register, name="registrarse"),
    path('ps5/', views.ps5news, name="ps5"),
    path('switch/', views.switchnews, name="switch"),
    path('pc/', views.switchnews, name="pc"),
    path('retro/', views.switchnews, name="retro"),
    path('xbox/', views.switchnews, name="xbox"),
]