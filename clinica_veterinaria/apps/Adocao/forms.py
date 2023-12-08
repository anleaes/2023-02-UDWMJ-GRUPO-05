from django import forms
from .models import Adocao

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['data_de_entrada', 'raça', 'tipo']