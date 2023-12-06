from django.urls import path
from Veterinario import views


urlpatterns = [
    path('listar_veterinarios', views.listar_Veterinarios, name='listar_veterinarios'),
    path('cadastrar/', views.cadastrar_Veterinario, name='cadastrar_veterinario'),
    path('excluir/<int:id>', views.excluir_veterinario, name='excluir_veterinario'),
]