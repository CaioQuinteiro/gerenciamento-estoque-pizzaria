from django.urls import path
from . import views

urlpatterns = [
    path('', views.fornecedores, name="fornecedores"),
    path('atualiza_fornecedor/', views.att_fornecedor, name="atualiza_fornecedor"),
    path('update_fornecedor/<int:id>', views.update_fornecedor, name="update_fornecedor"),
    path('lista_fornecedor/', views.lista_fornecedor, name='lista_fornecedor'),
    path('delete_fornecedor/<int:id>/', views.delete_fornecedor, name='delete_fornecedor'),
]