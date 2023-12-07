from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    preco = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome