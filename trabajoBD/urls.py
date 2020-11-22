from django.urls import path,include
from trabajoBD import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,logout_then_login

from django.urls import reverse, reverse_lazy
from django.conf import settings

from rest_framework import routers
from .views import NoticiaViewSet

router = routers.DefaultRouter()
router.register('noticiaApi', NoticiaViewSet)

urlpatterns = [
    path('index/', views.home, name="index"),
    path('registrarse/', views.register, name="registrarse"),
    path('ps5/', views.ps5news, name="ps5"),
    path('switch/', views.switchnews, name="switch"),
    path('pc/', views.pcnews, name="pc"),
    path('retro/', views.retronews, name="retro"),
    path('xbox/', views.xboxnews, name="xbox"),
    path('buscar/', views.buscar, name="buscar"),
    path('logout/', views.buscar, name="logout"),
    path('api/', include(router.urls)),


]








