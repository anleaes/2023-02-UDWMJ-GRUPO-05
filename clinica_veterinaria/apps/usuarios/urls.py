from usuarios import views
from django.urls import path

urlpatterns = [
    path('', views.index_usuario, name="index_usuario"),
    path('create/', views.create_usuario, name="create_usuario"),
    path('update/<int:id>', views.update_usuario, name="update_usuario"),
    path('delete/<int:id>', views.delete_usuario, name="delete_usuario"),
    path('buscar/', views.search_usuarios, name='search_usuarios'),
    
]