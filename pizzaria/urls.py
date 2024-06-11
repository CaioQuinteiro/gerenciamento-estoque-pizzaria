from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('compras/', include('compras.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('auth/', include('usuarios.urls')),
]
