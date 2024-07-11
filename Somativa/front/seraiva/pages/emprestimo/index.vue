<template>
  <div class="emprestimo-container">
    <h1>Informações do Empréstimo</h1>
    <div v-if="emprestimo">
      <h2>Usuário</h2>
      <p><strong>ID:</strong> {{ emprestimo.usuario.id }}</p>
      <p><strong>Email:</strong> {{ emprestimo.usuario.email }}</p>
      <p><strong>Telefone:</strong> {{ emprestimo.usuario.telefone || 'Não informado' }}</p>
      <p><strong>Endereço:</strong> {{ emprestimo.usuario.endereco }}</p>
      <p><strong>CPF:</strong> {{ emprestimo.usuario.cpf }}</p>
      <p><strong>Status:</strong> {{ emprestimo.status }}</p>
      
      <h2>Livros Emprestados</h2>
      <ul>
        <li v-for="livro in emprestimo.livros" :key="livro.id">
          <p><strong>Nome:</strong> {{ livro.nome }}</p>
          <p><strong>Descrição:</strong> {{ livro.descricao }}</p>
          <p><strong>Ano de Publicação:</strong> {{ livro.ano_publicacao }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Carregando informações do empréstimo...</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { getEmprestimoById } from '../../service/emprestimo';
import type { Emprestimo } from '../../models/emprestiomo';

export default defineComponent({
  data() {
    return {
      emprestimo: null as Emprestimo | null
    };
  },
  methods: {
    async fetchEmprestimo(id: number) {
      try {
        const resposta = await getEmprestimoById(id);
        if (resposta) {
          this.emprestimo = resposta; // Atribua a resposta à variável emprestimo
        }
      } catch (error) {
        console.error('Erro ao buscar informações do empréstimo:', error);
      }
    }
  },
  mounted() {
    const emprestimoId = 1; // Substitua pelo ID do empréstimo desejado
    this.fetchEmprestimo(emprestimoId);
  }
});
</script>

<style lang="scss" scoped>
.emprestimo-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 20px;
}

h1 {
  color: blue;
}

p {
  font-size: 18px;
}

h2 {
  color: darkblue;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 20px;
}
</style>
