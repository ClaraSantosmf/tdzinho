from django.db import models

# Create your models here.

class Listar(models.Model):
    task_name=models.CharField(max_length=20)
    squad=models.CharField(choices=(('infra','infraestrutura'), ('vendas', 'vendas'), ('tech', 'tech'),
                                    ('juridico', 'juridico')), max_length=10)
    descricao=models.TextField(max_length=200)
    ativo = models.BooleanField(default=False)
    def __str__(self):
        return self.task_name