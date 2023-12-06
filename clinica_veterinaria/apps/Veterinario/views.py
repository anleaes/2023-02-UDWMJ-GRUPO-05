from django.shortcuts import render, redirect
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


#def excluir_veterinario(request, id):
#  veterinario = Veterinario.objects.get(id=id)
#  if request.method == "POST":
#    veterinario.delete()
#    # return render(request, 'Veterinario/listar_veterinarios.html', {'veterinarios': veterinarios})
#    return redirect('listar_veterinarios')
#  return render(request, 'Veterinario/excluir_veterinario.html', {'veterinario': veterinario})

def excluir_veterinario(request, id):
    veterinario = Veterinario.objects.get(id=id)
    if request.method == "POST":
        veterinario.delete()
        return redirect('veterinario:listar_veterinarios')
    return render(request, 'Veterinario/excluir_veterinario.html', {'veterinario': veterinario})
