from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from .models import Fornecedor
import json

def fornecedores(request):
    if request.method == "GET":
        fornecedores_list = Fornecedor.objects.all()
        return render(request, 'fornecedores.html', {'fornecedores': fornecedores_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        fornecedor = Fornecedor(
            nome = nome,
            email = email,
            telefone = telefone,
        )

        fornecedor.save()

        return redirect('fornecedores')

def att_fornecedor(request):
    id_fornecedor = request.POST.get('id_fornecedor')
    fornecedor = Fornecedor.objects.filter(id=id_fornecedor)
    fornecedor_json = json.loads(serializers.serialize('json', fornecedor))[0]['fields']
    fornecedor_id = json.loads(serializers.serialize('json', fornecedor))[0]['pk']
    data = {'fornecedor': fornecedor_json, 'fornecedor_id': fornecedor_id}

    return JsonResponse(data)

def update_fornecedor(request, id):
    body = json.loads(request.body)

    nome = body['nome']
    email = body['email']
    telefone = body['telefone']

    fornecedor = get_object_or_404(Fornecedor, id=id)

    try:
        fornecedor.nome = nome
        fornecedor.email = email
        fornecedor.telefone = telefone
        fornecedor.save()
        return JsonResponse({'status': '200','nome': nome, 'email': email, 'telefone': telefone})
    except:
        return JsonResponse({'status': '500'})

    return JsonResponse({'teste': 'teste'})

def lista_fornecedor(request):
    if request.method == "GET":
        fornecedor = Fornecedor.objects.all()
        fornecedores_json = json.loads(serializers.serialize('json', fornecedores))
        return JsonResponse(fornecedores_json, safe=False)

def delete_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    fornecedor.delete()
    return redirect('fornecedores')