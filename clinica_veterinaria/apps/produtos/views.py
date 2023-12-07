from django.shortcuts import render, redirect
from produtos.models import Produto
from produtos.forms import ProdutoForm

def index_produto(request):
    produtos = Produto.objects.all()
    context = {"produtos" : produtos}
    return render(request, "produtos/list_produtos.html", context)