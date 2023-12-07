from django.shortcuts import render, redirect
from servicos.models import Servicos
from servicos.forms import ServicosForm

def index_servico(request):
    servicos = Servicos.objects.all()
    context = {"servicos" : servicos}
    return render(request, "servicos/list_servicos.html", context)

def create_servico(request):
    if request.method == "POST":
        banho = request.POST.get("banho")
        tosa = request.POST.get("tosa")
        nome = request.POST.get("nome")
        animal = request.POST.get("animal")
        raca = request.POST.get("raca")

        servico = Servicos(banho=banho, tosa=tosa, nome=nome, animal=animal, raca=raca)
        servico.save()
        return redirect("index_servico")
    else:
        form = ServicosForm
        
    return render(request, "servicos/create_servicos.html", {"form" : form})

def update_servico(request, id):
    servico = Servicos.objects.get(id = id)
    form = ServicosForm(request.POST or None, instance = servico)
    if form.is_valid():
        form.save()
        return redirect("index_servico")
    return render(request, "servicos/update_servicos.html", {"form" : form, "servico": servico})

def delete_servico(request, id):
    servico = Servicos.objects.get(id = id)
    if request.method == "POST":
        servico.delete()
        return redirect("index_servico")
    return render(request, "servicos/delete_servicos.html", {"servico" : servico})