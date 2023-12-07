from django import forms
from servicos.models import Servicos

class ServicosForm(forms.ModelForm):
    class Meta:
        model = Servicos
        fields = ['banho', 'tosa', 'nome', 'animal', 'raca']