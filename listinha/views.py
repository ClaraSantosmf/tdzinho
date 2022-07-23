from django.shortcuts import render
from django.http import HttpResponse
from .models import Listar
# Create your views here.

def home(request):
    return render(request, 'listinha/home.html')

def listar_task(request):
    nome_task = request.POST["task_name"]
    squad = request.POST["squad"]
    descricao = request.POST["descricao"]
    Listar.objects.create(task_name=nome_task, squad=squad, descricao=descricao)
    contexto = Listar.objects.all()
    return render(request, 'listinha/home.html', {'tarefinhas': contexto})
