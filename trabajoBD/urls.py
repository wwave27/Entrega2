from django.urls import path
from trabajoBD import views

urlpatterns = [
    path('index/', views.home, name="index")
]