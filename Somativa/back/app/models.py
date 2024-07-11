from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador


class UsuarioCustomizado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)

    objects = Gerenciador()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    
    def __str__(self):
        return self.nome

class Livro(models.Model):

    titulo = models.CharField(max_length=200)
    foto_capa = models.TextField()
    descricao = models.TextField()
    numero_paginas = models.IntegerField()
    formato = models.CharField(max_length=10, choices=[('ebook', 'Ebook'), ('fisico', 'Físico')])
    numero_edicao = models.IntegerField()
    ano_publicacao = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # FK
    preco_emprestimo = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_disponivel = models.IntegerField()
    estrelas = models.FloatField()

    def save(self, *args, **kwargs):
        # Verifica se o livro está sendo criado pela primeira vez (não está atualizando)
        if not self.pk:
            # Adicione aqui qualquer lógica adicional que você queira executar ao criar um novo livro
            # Por exemplo, você pode enviar uma notificação aos usuários sobre a disponibilidade do novo livro

            # Agora, salve o livro
            super().save(*args, **kwargs)
            
            # Depois de salvar o livro, você pode adicionar qualquer outra lógica necessária
            
        else:
            # Se o livro está sendo atualizado, apenas salve-o sem fazer nada adicional
            super().save(*args, **kwargs)


    def __str__(self):
        return self.titulo
    
STATUS = [
    ('APROVADO', 'Aprovado'),
    ('PENDENTE', 'Pendente'),
    ('CANCELADO', 'Cancelado'),
] 


class Emprestimo(models.Model):
    usuario = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE)  # FK
    data_realizacao = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS)
    livro = models.ForeignKey(Livro, related_name='emprestimoLivro', on_delete=models.CASCADE, null=True)
    quantidade = models.IntegerField(default=0)


def __str__(self):
        return f'Emprestimo {self.id} - {self.usuario.username}'


