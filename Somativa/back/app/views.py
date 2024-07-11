from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import render

class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UsuarioCustomizadoView(CustomModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioCustomizadoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = UsuarioCustomizado.objects.filter(id=user.id)        
        return queryset

class CategoriaView(CustomModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (AllowAny,)


class LivroView(CustomModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = (AllowAny,)

class EmprestimoView(CustomModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = [IsAuthenticated]

    def criar_emprestimo(self, request):
        # Recuperar todos os empréstimos ativos do usuário
        emprestimos_ativos = Emprestimo.objects.filter(usuario=request.user, status='ativo')

        # Calcular o número total de livros emprestados pelos empréstimos ativos
        total_livros_emprestados = sum(emprestimo.livros.count() for emprestimo in emprestimos_ativos)

        # Verificar se o número total de livros emprestados é inferior a 3
        if total_livros_emprestados < 3:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Você já possui 3 livros emprestados. Não é possível criar um novo empréstimo.'}, status=status.HTTP_400_BAD_REQUEST)
    

