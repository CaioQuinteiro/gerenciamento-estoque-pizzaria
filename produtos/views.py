from django.shortcuts import render
from django.http import HttpResponse

def produtos(request):
    return HttpResponse('Estou em Produtos')
