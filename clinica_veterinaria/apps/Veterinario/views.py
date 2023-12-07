from django.shortcuts import render, redirect, get_object_or_404
from Veterinario.forms import VeterinarioForm
from Veterinario.models import Veterinario

def listar_Veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'Veterinario/listar_veterinarios.html', {'veterinarios': veterinarios})

def cadastrar_Veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)   # talvez seja necessario alterar por conta do nome 
        if form.is_valid():
            form.save()
            return redirect("listar_veterinarios") # redireciona para o index de veterinarios              
    else:
        form = VeterinarioForm()
        
    return render(request, 'Veterinario/cadastrar_veterinario.html', {'form': form})


def excluir_veterinario(request, id):
    veterinario = get_object_or_404(Veterinario, pk=id)
    veterinario.delete()
    return redirect('listar_veterinarios')