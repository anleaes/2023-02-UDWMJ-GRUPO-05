from django.shortcuts import render, redirect, get_object_or_404
from Consulta.forms import AdocaoForm
from Consulta.models import Adocao


def listar_adocoes(request):
    adocoes = Adocao.objects.all()
    return render(request, 'Adocao/listar_adocoes.html', {'adocoes': adocoes})



