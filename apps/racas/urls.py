from django.urls import path
from . import views

app_name = 'racas'

urlpatterns = [
    path('', views.list_racas, name='list_racas'),
    path('adicionar/', views.add_raca, name='add_raca'),
    path('editar/<int:id_raca>/', views.edit_raca, name='edit_raca'),
    path('excluir/<int:id_raca>/', views.delete_raca, name='delete_raca'),
]