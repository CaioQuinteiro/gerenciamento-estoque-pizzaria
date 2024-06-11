from secrets import token_hex, token_urlsafe
from django.db import models
from produtos.models import Produto
from fornecedores.models import Fornecedor
from datetime import datetime

class Compra(models.Model):
    descricao = models.CharField(max_length=50, null=True)
    protocolo = models.CharField(max_length=52, null=True, blank=True)
    qtde = models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_validade = models.DateField()
    data_compra = models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, default=0)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, default=0)
    identificador = models.CharField(max_length=24, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.descricao
    
    def save(self, *args, **kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime('%d/%m/%Y-%H:%M:%S-') + token_hex(16)
        if not self.identificador:
            self.identificador = token_urlsafe(16)
        super(Compra, self).save(*args, **kwargs)