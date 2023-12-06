from django.shortcuts import render, redirect
from Veterinario.forms import VeterinarioForm
from Veterinario.models import Veterinario


def listar_Veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'listar_veterinarios.html', {'veterinarios': veterinarios})


def cadastrar_Veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)   # talvez seja necessario alterar por conta do nome 
        if form.is_valid():
            form.save()
            return redirect('lsitar_veterinarios') # redireciona para o index de veterinarios              
    else:
        form = VeterinarioForm()
        
    return render(request, 'cadastrar_veterinario.html', {'form': form})



def atualizar_Veterinario(request, id):
    veterinario = Veterinario.objects.get(id = id)
    form = VeterinarioForm(request.POST or None, instance = veterinario)
    if form.is_valid():
        form.save()
        return redirect('listar_veterinarios')
    return render(request, 'Veterinario/atualizar_veterinario.html', {"form" : form, 'veterinario': veterinario })


def excluir_Veterinario(request, id):
    veterinario = Veterinario.objects.get(id = id)
    if request.method == "POST":
        veterinario.delete()
        return redirect('listar_Veterinarios')
    return render(request, 'Veterinario/exluir_veterinario.html', {'veterinario': veterinario})