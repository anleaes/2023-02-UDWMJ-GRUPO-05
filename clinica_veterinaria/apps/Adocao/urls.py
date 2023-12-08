from django.urls import path
from Adocao import views

urlpatterns = [
    path('listar_adocoes', views.listar_adocoes, name='listar_adocoes'),
    path('cadastrar/', views.nova_entrada, name='nova_entrada'),
]