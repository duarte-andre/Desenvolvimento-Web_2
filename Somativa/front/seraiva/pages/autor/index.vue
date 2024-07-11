<script setup lang="ts">
import { reactive, ref } from 'vue';
import { postLivro } from '../../service/livros';
import type { Livro, FORMATO } from '../../models/livros';

import { navigateTo } from '#app';

const novoLivro = reactive<Livro>({
  id: 0,
  titulo: '',
  foto_capa: '',
  descricao: '',
  numero_paginas: 0,
  formato: 'ebook' as FORMATO, // ou 'fisico'
  numero_edicao: 1,
  ano_publicacao: 1, 
  categoria: { id: 1, nome: '' }, // Substitua com uma categoria padrão
  // ou outro status apropriado
  preco_emprestimo: 0,
  quantidade_disponivel: 0,
  estrelas: 0,
});

const mensagemErro = ref('');
const mensagemSucesso = ref('');

const enviarLivro = async () => {
  try {
    await postLivro(novoLivro);
    mensagemSucesso.value = 'Livro adicionado com sucesso!';
    setTimeout(() => {
      mensagemSucesso.value = '';
      navigateTo('/autor/livros'); // Navega para a lista de livros do autor
    }, 3000);
  } catch (error) {
    console.error("Erro ao adicionar livro: ", error);
    mensagemErro.value = 'Não foi possível adicionar o livro.';
    setTimeout(() => {
      mensagemErro.value = '';
    }, 3000);
  }
};
</script>

<template>
  <div class="autor-container">
    <h2>Adicionar Novo Livro</h2>
    <div v-if="mensagemErro" class="mensagem-erro">{{ mensagemErro }}</div>
    <div v-if="mensagemSucesso" class="mensagem-sucesso">{{ mensagemSucesso }}</div>
    <form @submit.prevent="enviarLivro">
      <label for="titulo">Título</label>
      <input type="text" id="titulo" v-model="novoLivro.titulo" required>

      <label for="foto_capa">Foto da Capa</label>
      <input type="text" id="foto_capa" v-model="novoLivro.foto_capa" required>

      <label for="descricao">Descrição</label>
      <textarea id="descricao" v-model="novoLivro.descricao" required></textarea>

      <label for="numero_paginas">Número de Páginas</label>
      <input type="number" id="numero_paginas" v-model="novoLivro.numero_paginas" required>

      <label for="formato">Formato</label>
      <select id="formato" v-model="novoLivro.formato" required>
        <option value="ebook">eBook</option>
        <option value="fisico">Físico</option>
      </select>

      <label for="numero_edicao">Número da Edição</label>
      <input type="number" id="numero_edicao" v-model="novoLivro.numero_edicao" required>

      <label for="categoria">Categoria</label>
      <input type="text" id="categoria" v-model="novoLivro.categoria.nome" required>

      <label for="status">Ano de Publicação</label>
      <input id="status" v-model="novoLivro.ano_publicacao" required>
      

      <label for="preco_emprestimo">Preço do Empréstimo</label>
      <input type="number" id="preco_emprestimo" v-model="novoLivro.preco_emprestimo" required>

      <label for="quantidade_disponivel">Quantidade Disponível</label>
      <input type="number" id="quantidade_disponivel" v-model="novoLivro.quantidade_disponivel" required>

      <label for="estrelas">Estrelas</label>
      <input type="number" id="estrelas" v-model="novoLivro.estrelas" required>

      <button type="submit">Adicionar Livro</button>
    </form>
  </div>
</template>

<style scoped>
.autor-container {
  width: 50%;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
}

label {
  display: block;
  margin: 10px 0 5px;
}

input, textarea, select, button {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}

.mensagem-erro {
  color: red;
}

.mensagem-sucesso {
  color: green;
}
</style>
