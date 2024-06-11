from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from .models import Produto
import json

def produtos(request):
    if request.method == "GET":
        produtos_list = Produto.objects.all()
        return render(request, 'produtos.html', {'produtos': produtos_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        qtde_estoque = request.POST.get('qtde_estoque')
        unidade_medida = request.POST.get('unidade_medida')

        produto = Produto(
            nome = nome,
            descricao = descricao,
            qtde_estoque = qtde_estoque,
            unidade_medida = unidade_medida
        )

        produto.save()

        return redirect('produtos')

def att_produto(request):
    id_produto = request.POST.get('id_produto')
    produto = Produto.objects.filter(id=id_produto)
    produto_json = json.loads(serializers.serialize('json', produto))[0]['fields']
    produto_id = json.loads(serializers.serialize('json', produto))[0]['pk']
    data = {'produto': produto_json, 'produto_id': produto_id}

    return JsonResponse(data)

def update_produto(request, id):
    body = json.loads(request.body)

    nome = body['nome']
    descricao = body['descricao']
    qtde_estoque = body['qtde_estoque']
    unidade_medida = body['unidade_medida']

    produto = get_object_or_404(Produto, id=id)

    try:
        produto.nome = nome
        produto.descricao = descricao
        produto.qtde_estoque = qtde_estoque
        produto.unidade_medida = unidade_medida
        produto.save()
        return JsonResponse({'status': '200','nome': nome, 'descricao': descricao, 'qtde_estoque': qtde_estoque, 'unidade_medida': unidade_medida})
    except:
        return JsonResponse({'status': '500'})


def lista_produto(request):
    if request.method == "GET":
        produtos = Produto.objects.all()
        produtos_json = json.loads(serializers.serialize('json', produtos))
        return JsonResponse(produtos_json, safe=False)

def delete_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produtos')