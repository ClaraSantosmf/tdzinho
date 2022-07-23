from django.db import models


class Lista(models.Model):
    SQUAD = {
        ('i', 'infraestrutura'),
        ('v', 'vendas'),
        ('t', 'tech'),
        ('j', 'juridico')
    }

    _SQUAD_DICT = dict(
        i = 'infraestrutura',
        v = 'vendas',
        t = 'tech',
        j = 'juridico',
    )

    task_name = models.CharField(max_length=20)
    squad = models.CharField(choices=SQUAD, max_length=1)
    descricao = models.TextField(max_length=200)
    feito = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

    def squad_name(self):
        return self._SQUAD_DICT[self.squad]
