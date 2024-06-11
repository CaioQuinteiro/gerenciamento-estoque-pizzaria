from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from produtos.models import Produto
from .models import Compra

total_gasto = 0

@receiver(post_save, sender=Compra)
def update_estoque_and_valor_on_save(sender, instance, created, **kwargs):
    global total_gasto
    if created:
        instance.produto.qtde_estoque += instance.qtde
        instance.produto.save()
        total_gasto += instance.valor
    else:
        total_gasto -= instance.valor_antigo
        total_gasto += instance.valor

@receiver(post_delete, sender=Compra)
def update_estoque_and_valor_on_delete(sender, instance, **kwargs):
    global total_gasto
    instance.produto.qtde_estoque -= instance.qtde
    if instance.produto.qtde_estoque < 0:
        instance.produto.qtde_estoque = 0
    instance.produto.save()
    total_gasto -= instance.valor
    instance.produto.save()