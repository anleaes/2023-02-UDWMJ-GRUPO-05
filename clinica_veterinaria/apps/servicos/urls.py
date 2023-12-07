from servicos import views
from django.urls import path

urlpatterns = [
    path('', views.index_servico, name="index_servico"),
    path('create/', views.create_servico, name="create_servico"),
    path('update/<int:id>', views.update_servico, name="update_servico"),
    path('delete/<int:id>', views.delete_servico, name="delete_servico"),
    
]