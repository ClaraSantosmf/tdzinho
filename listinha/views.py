from django.shortcuts import render, resolve_url
from django.http import HttpResponseRedirect
from .models import Lista


def home(request):
    if request.method == 'POST':
        nome_task = request.POST["task_name"]
        squad = request.POST["squad"]
        descricao = request.POST["descricao"]

        Lista.objects.create(task_name=nome_task, squad=squad, descricao=descricao)

        return HttpResponseRedirect(resolve_url('home'))

    context = {
        'tasks_ativas': Lista.objects.filter(feito=True),
        'tasks_inativas': Lista.objects.filter(feito=False),
        'squads': Lista.SQUAD
    }

    return render(request, 'listinha/home.html', context=context)


def atualizar_status(request):
    nome_task = request.POST["task_name"]
    feito = request.POST["feito"]

    tasks = Lista.objects.get(task_name=nome_task)

    tasks.feito = feito

    tasks.save()

    return HttpResponseRedirect(resolve_url('home'))
