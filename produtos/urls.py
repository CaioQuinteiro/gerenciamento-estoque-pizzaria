from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos, name="produtos"),
    path('atualiza_produto/', views.att_produto, name="atualiza_produto"),
    path('update_produto/<int:id>', views.update_produto, name="update_produto")
]