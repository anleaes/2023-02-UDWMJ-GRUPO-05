from django.shortcuts import render, redirect, get_object_or_404
from Consulta.forms import AdocaoForm
from Consulta.models import Adocao


def listar_adocoes(request):
    adocoes = Adocao.objects.all()
    return render(request, 'Adocao/listar_adocoes.html', {'adocoes': adocoes})

def nova_entrada(request):
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_adocoes')  #  aqui deve ser o redirect para listar consultas
    else:
        form = AdocaoForm()

    return render(request, 'Adocao/nova_entrada.html', {'form': form}) 
# aqui deve ser o render do agendamento
# talvez seja necessario adicionar 
# 'Consulta/nova_consulta.html'



