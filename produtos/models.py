from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    qtde_estoque = models.IntegerField()
    qtde_min = models.IntegerField()
    data_validade = models.DateField()

    def __str__(self) -> str:
        return self.nome

