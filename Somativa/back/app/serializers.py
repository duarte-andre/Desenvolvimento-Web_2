from rest_framework import serializers
from .models import *

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id', 'email', 'telefone', 'cpf', 'endereco', 'is_active', 'groups', 'user_permissions']
        many = True

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        many = True


class LivroSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Livro
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    usuario = UsuarioCustomizadoSerializer(read_only=True)
    livros = LivroSerializer(many=True, read_only=True)

    class Meta:
        model = Emprestimo
        fields = '__all__'
        many = True



