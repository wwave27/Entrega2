from django.urls import path,include
from trabajoBD import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,logout_then_login

from django.urls import reverse, reverse_lazy
from django.conf import settings

urlpatterns = [
    path('index/', views.home, name="index"),
    path('registrarse/', views.register, name="registrarse"),
    path('ps5/', views.ps5news, name="ps5"),
    path('switch/', views.switchnews, name="switch"),
    path('pc/', views.pcnews, name="pc"),
    path('retro/', views.retronews, name="retro"),
    path('xbox/', views.xboxnews, name="xbox"),
    path('index/',LoginView.as_view(template_name='index.html'),name="login")
]