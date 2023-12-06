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
    especializacao = models.CharField(max_length=255, choices=ESPECIALIZACAO_ESCOLHA)
    
    def __str__(self):
        return self.nome
