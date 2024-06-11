from django.urls import path
from . import views

urlpatterns = [
    path('nova_compra/', views.nova_compra, name="nova_compra"),
    path('listar_compra/', views.listar_compra, name="listar_compra"),
    path('compra/<str:identificador>', views.compra, name="compra"),
    path('gerar_oc/<str:identificador>', views.gerar_oc, name="gerar_oc"),
]