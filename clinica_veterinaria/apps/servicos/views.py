from django.shortcuts import render, redirect
from servicos.models import Servicos
from servicos.forms import ServicosForm

def index_servico(request):
    servicos = Servicos.objects.all()
    context = {"servicos" : servicos}
    return render(request, "servicos/list_servicos.html", context)