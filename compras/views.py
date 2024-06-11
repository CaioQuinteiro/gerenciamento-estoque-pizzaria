from django.shortcuts import redirect, render, get_object_or_404
from .models import Compra, Produto, Fornecedor
from .forms import FormServico
from django.http import HttpResponse, FileResponse
from fpdf import FPDF
from io import BytesIO

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

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Ordem de Compra', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def gerar_oc(request, identificador):
    compra = get_object_or_404(Compra, identificador=identificador)

    produto_nome = compra.produto.nome
    fornecedor_nome = compra.fornecedor.nome
    medida = compra.produto.unidade_medida

    pdf = PDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(240, 240, 240)

    largura_celula_label = 40
    largura_celula_valor = 150
    altura_celula = 10

    def add_line(label, value, fill=1):
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(largura_celula_label, altura_celula, label, 1, 0, 'L', fill)
        pdf.set_font('Arial', '', 12)
        pdf.cell(largura_celula_valor, altura_celula, value, 1, 1, 'L', fill)

    add_line('Produto:', produto_nome)
    add_line('Fornecedor:', fornecedor_nome)
    add_line('Quantidade:', f'{compra.qtde} {medida}')
    add_line('Valor:', f'R${compra.valor:.2f}')
    add_line('Data da Compra:', compra.data_compra.strftime('%d/%m/%Y'))
    add_line('Data de Validade:', compra.data_validade.strftime('%d/%m/%Y'))
    add_line('Protocolo:', compra.protocolo)

    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f"oc-{compra.protocolo}.pdf")
