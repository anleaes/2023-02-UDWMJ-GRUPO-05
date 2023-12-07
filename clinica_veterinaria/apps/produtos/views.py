from django.shortcuts import render, redirect
from produtos.models import Produto
from produtos.forms import ProdutoForm

def index_produto(request):
    produtos = Produto.objects.all()
    context = {"produtos" : produtos}
    return render(request, "produtos/list_produtos.html", context)

def create_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        quantidade = request.POST.get("quantidade")
        preco = request.POST.get("preco")

        produto = Produto(nome=nome, descricao=descricao, quantidade=quantidade, preco=preco)
        produto.save()
        return redirect("index_produto")
    else:
        form = ProdutoForm
        
    return render(request, "produtos/create_produtos.html", {"form" : form})

def update_produto(request, id):
    produto = Produto.objects.get(id = id)
    form = ProdutoForm(request.POST or None, instance = produto)
    if form.is_valid():
        form.save()
        return redirect("index_produto")
    return render(request, "produtos/update_produtos.html", {"form" : form, "produto": produto})

def delete_produto(request, id):
    produto = Produto.objects.get(id = id)
    if request.method == "POST":
        produto.delete()
        return redirect("index_produto")
    return render(request, "produtos/delete_produtos.html", {"produto" : produto})