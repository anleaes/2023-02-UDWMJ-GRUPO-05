from django.shortcuts import render, redirect, get_object_or_404
from Consulta.forms import ConsultaForm
from Consulta.models import Consulta


def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'listar_consultas.html', {'consultas': consultas})

def nova_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas.html')  #  aqui deve ser o redirect para listar consultas
    else:
        form = ConsultaForm()

    return render(request, 'nova_consulta.html', {'form': form}) 
# aqui deve ser o render do agendamento
# talvez seja necessario adicionar 
# 'Consulta/nova_consulta.html'

def excluir_consulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    
    if request.method == 'POST':
        consulta.delete()
        return redirect('listar_consultas')

#    return render(request, 'excluir_consulta.html', {'consulta': consulta})
    # essa linha poderá ser excluida se quiser.