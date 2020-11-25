"""Entrega2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Entrega2.views import mainPage
from Entrega2.views import buscarUsuario
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib.auth.views import LoginView,logout_then_login,LogoutView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('MundoGamer/', include('trabajoBD.urls')),
    path('login/',LoginView.as_view(template_name='login.html'),name="login"),
    path('accounts/login/',LoginView.as_view(template_name='logout.html'),name="logout"),   
    path('accounts/profile/',LoginView.as_view(template_name='index.html'),name="accounts/profile"),
    path('logout/',logout_then_login,name="logout"),
    path('oauth/', include('social_django.urls', namespace='social')),
    url('^', include('django.contrib.auth.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)