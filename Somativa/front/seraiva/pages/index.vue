<script setup lang="ts">
import { getLivros } from "../service/livros";
import { type Livro } from "../models/livros";
import { type Ref, ref } from "vue";
import { useToast } from "primevue/usetoast";
const toast = useToast();

const show = () => {
    toast.add({ severity: 'success', summary: 'Livro Adicionado', detail: 'Acesse-o em seu carrinho', life: 3000 });
};

const livros: Ref<Array<Livro>> = ref([]);

const atualizarLivros = () => {
  getLivros().then((livrosEncontrados) => {
    console.log("Livros Encontrados: ", livrosEncontrados?.results[0]);
    livros.value = livrosEncontrados?.results ?? [];
  });
};

atualizarLivros();
</script>

<template>
  <main class="home-container">
    <!-- <h1 class="text-with-background">Desfrute de nossos livros :)</h1> -->
    <div class="grid-container">
      <div v-for="(livro, index) in livros" :key="index" class="grid-item">
        <LivroItem :key="index" :livro="livro" @evento-adicionado="show"/>
      </div>
    </div>
  </main>
</template>

<style scoped lang="scss">
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin: 0;
  padding: 2rem;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: #f5f5f5;
}

// .text-with-background {
//   color: #fff;
//   background: linear-gradient(to right, #333, #777);
//   padding: 1rem 2rem;
//   border-radius: 0.5rem;
//   box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
//   font-size: 2rem;
//   font-weight: bold;
//   text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
//   margin-bottom: 2rem;
// }

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  width: 100%;
  max-width: 1200px;
  padding: 0 1rem;
}

.grid-item {
  display: flex;
  justify-content: center;
}

.p-toast-summary {
  padding: 1.5rem !important;
}
</style>
