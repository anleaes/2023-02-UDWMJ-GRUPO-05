from animals import views
from django.urls import path

urlpatterns = [
    path('', views.index_animal, name="index_animal"),
    path('create/', views.create_animal, name="create_animal"),
    path('update/<int:id>', views.update_animal, name="update_animal"),
    path('delete/<int:id>', views.delete_animal, name="delete_animal"),
]
