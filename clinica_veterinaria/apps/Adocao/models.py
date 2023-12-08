from django.db import models

class Adocao(models.Model):

    AVES = 'Aves'
    GATO = 'Gato'
    CÃES = 'Cães'
    
    
    TIPO_ESCOLHA = [
        (AVES, 'Aves'),
        (GATO, 'Gato'),
        (CÃES, 'Cães'),
    ]
    
    raça = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, choices=TIPO_ESCOLHA)
    data_de_entrada = models.DateField()
    
    def __str__(self):
        return self.nome
