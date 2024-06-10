from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=80)
    qtde_estoque = models.IntegerField()
    unidade_medida = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.nome

