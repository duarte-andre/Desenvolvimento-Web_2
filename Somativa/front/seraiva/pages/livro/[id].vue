<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getLivroById } from '../../service/livros';

const route = useRoute();
const livro:any = ref();

const livroId = route.params.id

onMounted(async () => {
  try {
    console.log('Buscando livro com ID:', livroId); // Log para verificar ID
    const response = await getLivroById(livroId as string);
    console.log('Dados do livro:', response); // Log para verificar resposta
    livro.value = response;
  } catch (error) {
    console.error('Erro ao buscar dados do livro:', error);
  }
});
</script>

<template>
  <section class="book-details">
    <div v-if="livro" class="book-container">
      <div class="book-image-card">
        <img :src="livro.foto_capa" alt="Capa do Livro" />
      </div>
      <div class="book-info">
        <h1 class="book-title">{{ livro.titulo }}</h1>
        <p class="book-description">{{ livro.descricao }}</p>
        <p class="book-detail"><strong>Número de páginas:</strong> {{ livro.numero_paginas }}</p>
        <p class="book-detail"><strong>Formato:</strong> {{ livro.formato }}</p>
        <p class="book-detail"><strong>Edição:</strong> {{ livro.numero_edicao }}</p>
        <p class="book-detail"><strong>Categoria:</strong> {{ livro.categoria.nome }}</p>
        <p class="book-detail"><strong>Preço:</strong> R${{ livro.preco_emprestimo }}</p>
        <p class="book-detail"><strong>Quantidade disponível:</strong> {{ livro.quantidade_disponivel }}</p>
        <p class="book-detail"><strong>Estrelas:</strong> {{ livro.estrelas }}</p>
      </div>
    </div>
    <div v-else>
      <p>Carregando...</p>
    </div>
  </section>
</template>

<style scoped>
.book-details {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh; /* Full height */
  padding: 20px;
  background-color: #f7f7f7;
}

.book-container {
  display: flex;
  max-width: 1000px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-radius: 10px;
  overflow: hidden;
}

.book-image-card {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 320px;
  padding: 20px;
  background: #fff;
  border-right: 1px solid #ddd;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.book-image-card img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 10px;
}

.book-info {
  padding: 20px;
  flex: 1;
}

.book-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.book-description {
  font-size: 16px;
  margin-bottom: 20px;
}

.book-detail {
  font-size: 14px;
  margin-bottom: 8px;
}

.book-detail strong {
  font-weight: bold;
}
</style>
