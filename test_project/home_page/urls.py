from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home_page-home"),
    path("welcome/",views.welcome,name ="home_page-welcome"),
]
