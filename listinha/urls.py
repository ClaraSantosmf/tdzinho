from django.urls import path
from listinha.views import atualizar_status, home

urlpatterns = [
    path('', home, name="home"),
    path('atualizar_status/', atualizar_status, name="atualizar_status"),
]
