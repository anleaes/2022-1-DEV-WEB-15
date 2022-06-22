from django.urls import path
from . import views

app_name = 'internacao'

urlpatterns = [
    path('', views.list_internacoes, name='list_internacoes'),
    path('adicionar/', views.add_internacao, name='add_internacao'),
    path('editar/<int:id_internacao>/', views.edit_internacao, name='edit_internacao'),
    path('excluir/<int:id_internacao>/', views.delete_internacao, name='delete_internacao'),
]