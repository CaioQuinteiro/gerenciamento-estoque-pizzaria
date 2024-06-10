from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.nome
