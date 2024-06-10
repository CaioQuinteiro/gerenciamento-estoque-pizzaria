from django.shortcuts import redirect, render, get_object_or_404

from compras.models import Compra
from .forms import FormServico
from django.http import HttpResponse

def nova_compra(request):
    if request.method == "GET":  
        form = FormServico()
        return render(request, 'nova_compra.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return redirect('nova_compra')
        else:
            return render(request, 'nova_compra.html', {'form': form})
        
def listar_compra(request):
    if request.method == "GET":
        compra = Compra.objects.all()
        return render(request, 'listar_compra.html', {'compras': compra})

def compra(request, identificador):
    compra = get_object_or_404(Compra, identificador=identificador)
    return render(request, 'compra.html', {'compra': compra})


