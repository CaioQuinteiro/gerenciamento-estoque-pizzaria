from secrets import token_hex
from django.db import models
from produtos.models import Produto
from datetime import datetime

class ItemCompra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    qtde = models.IntegerField()
    data_validade = models.DateField()
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return self.descricao

class Compra(models.Model):
    descricao = models.CharField(max_length=50, null=True)
    item_compra = models.ManyToManyField(ItemCompra)
    protocolo = models.CharField(max_length=52, null=True, blank=True)
    data_compra = models.DateField()
    
    def __str__(self) -> str:
        return self.descricao
    
    def save(self, *args, **kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime('%d/%m/%Y-%H:%M:%S-') + token_hex(16)
        super(Compra, self).save(*args, **kwargs)

    def preco_total(self):
        preco_total = float(0)
        for item in self.item_compra.all():
            preco_total += float(item.preco)
            
        return preco_total