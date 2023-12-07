from django.db import models
from Veterinario.models import Veterinario
from animals.models import Animal


class Consulta(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    observacao = models.TextField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Consulta marcada para: {self.animal.nome} no dia {self.data} às {self.hora} com o(a) Dr(a) {self.veterinario.nome}"
    
    
