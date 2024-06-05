from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def produtos(request):
    if request.method == "GET":
        return render(request, 'produtos.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        qtde_estoque = request.POST.get('qtde_estoque')
        qtde_min = request.POST.get('qtde_min')
        data_validade = request.POST.get('data_validade')

        produto = Produto(
            nome = nome,
            qtde_estoque = qtde_estoque,
            qtde_min = qtde_min,
            data_validade = data_validade
        )

        produto.save()

        return HttpResponse('teste')
