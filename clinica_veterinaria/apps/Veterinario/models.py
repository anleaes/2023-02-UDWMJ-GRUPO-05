from django.db import models


class Veterinario(models.Model):
    AVES = 'Aves'
    GATO = 'Gato'
    CÃES = 'Cães'
    OUTRO = 'Outro'
    
    ESPECIALIZACAO_ESCOLHA = [
        (AVES, 'Aves'),
        (GATO, 'Gato'),
        (CÃES, 'Cães'),
        (OUTRO, 'Outro'),
    ]
    
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    especializacao = models.CharField(max_length=255, choices=ESPECIALIZACAO_ESCOLHA)
    
    
    def __str__(self):
        return self.nome