from django.urls import path
from Consulta import views

urlpatterns = [
    path('listar_consultas', views.listar_consultas, name='listar_consultas'),
    path('cadastrar/', views.nova_consulta, name='listar_consultas'),
    path('excluir/<int:id>', views.excluir_consulta, name='excluir_consulta'),
]


