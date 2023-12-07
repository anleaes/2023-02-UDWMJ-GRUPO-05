from django.shortcuts import render, redirect
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

    return render(request, 'nova_consulta.html', {'form': form}) # aqui deve ser o render do agendamento
                                                                 # talvez seja necessario adicionar 
                                                                 # 'Consulta/nova_consulta.html'
