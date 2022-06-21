from django.urls import path
from . import views

app_name = 'consulta'

urlpatterns = [
    path('', views.list_consultas, name='list_consultas'),
    path('adicionar/', views.add_consulta, name='add_consulta'),
    path('editar/<int:id_consulta>/', views.edit_consulta, name='edit_consulta'),
    path('excluir/<int:id_consulta>/', views.delete_consulta, name='delete_consulta'),
    path('sucesso/', views.sucess_consulta, name='sucess_consulta'),
]