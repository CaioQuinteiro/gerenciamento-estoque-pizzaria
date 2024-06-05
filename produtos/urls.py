from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos, name="produtos")
]