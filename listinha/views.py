from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'listinha/home.html')

def listar_task(request):
    nome_task = request.POST["task_name"]
    return HttpResponse("oi!")
    pass