from django.urls import path
from .views import cadastrar_Veterinario

urlpatterns = [
    path('cadastrar_veterinario/', cadastrar_Veterinario, name='cadastrar_veterinario'),
]