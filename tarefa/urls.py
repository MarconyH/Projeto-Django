from django.contrib import admin
from django.urls import path, include
from tarefa import views

urlpatterns = [
    #não usa parenteses pois os parametros foram passados na criação da função
    path('', views.home, name = 'home')
]