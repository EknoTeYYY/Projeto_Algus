from pickletools import read_string1
import re
from webbrowser import get
from django.shortcuts import redirect, render,get_object_or_404
from .models import Produtos, Vendidos
from datetime import datetime

def index(request):
    return render(request, 'paginas/tela.html')

def prod(request):
    produtos = Produtos.objects.all().filter(user_id =request.user.id).order_by('nome')
    return render(request, 'paginas/produtos.html', {'produtos': produtos})
    
    
def criar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')

        produto = Produtos.objects.create(nome=nome, quantidade=quantidade, valor=valor, descricao=descricao, user_id=request.user.id)
        produto.save()

        return redirect('produto')
    else:
        return render(request, 'paginas/adc.html')


def relatar(request):
    relatorios = Vendidos.objects.all().filter(user_id=request.user.id)
    return render(request, 'paginas/relatorio.html', {'relatorios':relatorios})
    

def excluir(request, id):
    finalizar = get_object_or_404(Produtos, id=id)
    finalizar.delete()
    return redirect('produto')


def editar(request, id):
    editar = get_object_or_404(Produtos, id=id)
    if request.method == 'POST':
        editar.nome = request.POST.get('nome')
        editar.quantidade = request.POST.get('quantidade')
        editar.valor = request.POST.get('valor')
        editar.descricao = request.POST.get('descricao')
        editar.status = request.POST.get('status')
        print(editar.status)
        if editar.status == 'inativo':
            editar.status = True
        else:
            editar.status = False

        editar.save()
        return redirect('produto')
    else:
        return render(request, 'paginas/atualizar.html', {'editar':editar})

def diminuir(request, id):
    diminuir = get_object_or_404(Produtos, id=id)
    diminuir.quantidade -= 1
    if diminuir.quantidade == 0:
        diminuir.status = False
    elif diminuir.quantidade < 0:
        diminuir.quantidade = 0
    diminuir.save()
    add = Vendidos.objects.create(user=diminuir.user, nome=diminuir.nome, quantidade=diminuir.quantidade, valor=diminuir.valor, descricao=diminuir.descricao, data=datetime.now().strftime('%d/%m/%Y'))
    add.save()
    return redirect('produto')

def info(request, id):
    produtos = get_object_or_404(Produtos, id=id)
    return render(request, 'paginas/info.html', {'produtos':produtos})
