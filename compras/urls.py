from django.urls import path
from . import views

urlpatterns = [
    path('nova_compra', views.nova_compra, name="nova_compra"),
]