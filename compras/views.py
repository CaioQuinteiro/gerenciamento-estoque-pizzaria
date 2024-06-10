from django.shortcuts import render
from .forms import FormCompra

def nova_compra(request):
    form = FormCompra()
    return render(request, 'nova_compra.html', {'form': form})
