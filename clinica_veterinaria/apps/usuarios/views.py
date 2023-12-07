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

def update_usuario(request, id):
    usuario = Usuario.objects.get(id = id)
    form = UsuarioForm(request.POST or None, instance = usuario)
    if form.is_valid():
        form.save()
        return redirect("index_usuario")
    return render(request, "usuarios/update_usuarios.html", {"form" : form, "usuario" : usuario})

def delete_usuario(request, id):
    usuario = Usuario.objects.get(id = id)
    if request.method == "POST":
        usuario.delete()
        return redirect("index_usuario")
    return render(request, "usuarios/delete_usuarios.html",{"usuario" : usuario})

def search_usuarios(request):
    template_name = 'usuarios/list_usuarios.html'
    query = request.GET.get('query')
    usuarios = Usuario.objects.filter(name=query)
    context = {
        'usuarios': usuarios,
    }
    return render(request,template_name, context)
