from django.shortcuts import render, redirect
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm


def index_usuario(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios" : usuarios}
    return render(request, "usuarios/list_usuarios.html", context)

def create_usuario(request):
    if request.method == "POST":
        name = request.POST.get("name")
        cpf = request.POST.get("cpf")
        endereco = request.POST.get("endereco")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        
        usuario = Usuario(name=name, cpf=cpf, endereco=endereco, email=email, telefone=telefone)
        usuario.save()
        return redirect("index_usuario")
    else:
        form = UsuarioForm()
        
    return render(request, "usuarios/create_usuarios.html", {"form" : form})