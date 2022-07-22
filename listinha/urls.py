from django.contrib import admin
from django.urls import path, include
from listinha.views import home, listar_task

urlpatterns = [
    path('', home, name="home"),
    path('enviado/', listar_task, name="enviado"),
    ]
