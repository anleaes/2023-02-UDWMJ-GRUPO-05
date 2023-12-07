from django.shortcuts import render, redirect, get_object_or_404
from Veterinario.forms import VeterinarioForm
from Veterinario.models import Veterinario

def listar_Veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'Veterinario/listar_veterinarios.html', {'veterinarios': veterinarios})