from django.db import models

class Servicos(models.Model):
    banho = models.CharField(max_length=50)
    tosa = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    animal = models.CharField(max_length=100)
    raca = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome