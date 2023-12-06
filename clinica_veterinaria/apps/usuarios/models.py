from django.db import models

from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=200)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

