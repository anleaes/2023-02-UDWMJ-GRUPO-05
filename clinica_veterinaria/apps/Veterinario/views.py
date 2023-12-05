from django.shortcuts import render, redirect
from Veterinario.forms import VeterinarioForm

def cadastrar_Veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso!')
        
        
    else:
        form = VeterinarioForm()
        
    return render(request, 'cadastrar_veterinario.html', {'forms': form})
