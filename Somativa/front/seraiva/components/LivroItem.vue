<script setup lang="ts">
import { useRouter } from 'vue-router';
import { computed } from "vue";
import { type Livro } from "../models/livros";
import { useCarrinho } from "../store/carrinho";

const props = defineProps<{ livro: Livro }>();
const emit = defineEmits(['eventoAdicionado']); 

const { adicionarNoCarrinho, getCarrinho, estaNoCarrinho } = useCarrinho();
const router = useRouter();

const adicionarItem = () => {
  adicionarNoCarrinho(props.livro);
  emit('eventoAdicionado');
  console.log("CARRINHO ATUAL: ", getCarrinho());
}

const livroNoCarrinho = computed(() => {
  return estaNoCarrinho(props.livro);   
});

const navegarParaDetalhes = () => {
  router.push({ path: `/livro/${props.livro.id}` });
}

// Função para renderizar estrelas
const renderStars = (estrelas: number) => {
  const totalEstrelas = 5;
  const filledStars = Math.round(estrelas);
  const emptyStars = totalEstrelas - filledStars;
  return '★'.repeat(filledStars) + '☆'.repeat(emptyStars);
}
</script>

<template>
  <section @click="navegarParaDetalhes" class="cartao" v-if="props.livro">
    <div class="check text-right">      
      <Checkbox v-model="livroNoCarrinho" :binary="true" :readonly="true"/>
    </div>
    <div class="livro-imagem">
      <img :src="props.livro.foto_capa" alt="Capa do Livro">
    </div>

    <h4 class="livro-nome">{{ props.livro.titulo }}</h4>

    <div class="estrelas">
      <span>{{ renderStars(props.livro.estrelas) }}</span>
    </div>

    <div class="livro-preco-disponibilidade">
      <span>R${{ props.livro.preco_emprestimo }} -</span>
      <div class="quantidade-disponivel">
        <label>Qtd. Disponível: </label>
        <span>{{ props.livro.quantidade_disponivel }} </span>
      </div>
    </div>

    <Button @click.stop="adicionarItem" class="botao-add" label="Adicionar" />
  </section>
</template>

<style scoped lang="scss">
.cartao {
  width: 300px;
  max-width: 300px;
  height: 450px; 
  max-height: 450px;
  background-color: white;
  border-radius: 1.5rem;
  margin: 1.5rem;
  cursor: pointer;
  border: 1px solid #ddd; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: transform 0.2s;

  &:hover {
    transform: scale(1.05);
  }

  .check {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    padding: 10px;
  }

  .livro-imagem {
    // width: 120px;
    // height: 200px;
    margin: 10px 0;
    img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-radius: 10px;
      border: 1px solid #ccc;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  }

  .livro-nome {
    font-size: 18px;
    font-weight: bold;
    margin: 10px 0;
    text-align: center;
  }

  .estrelas {
    font-size: 16px;
    color: #f5c518; 
    margin: 5px 0;
  }

  .livro-preco-disponibilidade {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 10px 0;
    

    span {
      font-size: 16px;
    }

    .quantidade-disponivel {
      font-size: 14px;
      label {
        font-weight: bold;
      }
    }
  }

  .botao-add {
    width: 200px;
    height: 2.5rem;
    margin: 15px 0;
    background-color: #ff9900; 
    border: none;
    border-radius: 5px;
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s;

    &:hover {
      background-color: #e68a00;
    }
  }
}
</style>
