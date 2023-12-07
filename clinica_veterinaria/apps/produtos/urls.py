from produtos import views
from django.urls import path

urlpatterns = [
    path('', views.index_produto, name="index_produto"),
    path('create/', views.create_produto, name="create_produto"),
    path('update/<int:id>', views.update_produto, name="update_produto"),
    path('delete/<int:id>', views.delete_produto, name="delete_produto"),
    
]