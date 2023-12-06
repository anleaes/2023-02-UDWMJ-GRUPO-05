from django.urls import path
from Veterinario import views

urlpatterns = [
    path('', views.listar_Veterinarios, name='listar_veterinarios'),
    path('cadastrar/', views.cadastrar_Veterinario, name='cadastrar_veterinario'),
    path('atualizar/<int:id>', views.atualizar_Veterinario, name='atualizar_veterinario'),
    path('excluir/<int:id>', views.excluir_Veterinario, name='excluir_veterinario'),
]