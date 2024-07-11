<script setup lang="ts">
import { computed } from "vue";
import { useCarrinho, type CarrinhoItem } from "../../store/carrinho";
import { navigateTo } from "#app";
const {data} = useAuth();
const { getCarrinho, removerDoCarinho, getValorLivro, } = useCarrinho();
import {type UsuarioCustomizado } from "../../models/usuarios";

if (data.value?.results[0] as UsuarioCustomizado == null){
  navigateTo('/login')
}

//pegando os itens que estão no carrinho e salvando
//na variavel
const itensNoCarrinho = computed<Array<CarrinhoItem>>(()=>getCarrinho());
const valorTotal = computed(() => getValorLivro().toPrecision(2));

console.log("itens No carrinho.....", itensNoCarrinho);

const deletarDoCarrinho = (itemParaRemover: CarrinhoItem) => {
  removerDoCarinho({
    livro: itemParaRemover.livro,
    quantidade: 0
  });
}

const salvarPedido = () => {
  
      };

</script>

<template>
  <main class="carrinho-container flex flex-column align-items-center">
    <h2 class="mt-4 mb-4">🛒 Seu carrinho de compras</h2>
    <table class="carrinho-tabela">
      <thead>
        <tr class="text-center">
          <td>Item</td>
          <td>Livro</td>
          <td>Titulo</td>
          <td>Categoria</td>
          <td>Preço</td>
          <td>Quantidade</td>
          <td>Subtotal</td>
          <td>Ação</td>
        
        </tr>
      </thead>
      <tbody>
        <tr v-for="(itemCarrinho, index) in itensNoCarrinho" :key="index" class="text-center">
          <td>{{ index + 1 }}</td>
          <td><img class="Livro" :src="itemCarrinho.livro.foto_capa" alt="foto livro" /></td>
          <td>{{ itemCarrinho.livro.titulo }}</td>
          <td>{{ itemCarrinho.livro.categoria.nome }}</td>
          <td>R$ {{ itemCarrinho.livro.preco_emprestimo }}</td>
          <td>{{ itemCarrinho.quantidade }}</td>
          <td>R$ {{ itemCarrinho.quantidade * itemCarrinho.livro.preco_emprestimo }}</td>
          <td>
            <Button @click="deletarDoCarrinho(itemCarrinho)" label=""><i class="pi pi-trash"></i></Button>
          </td>
        </tr>
        <br>
        <section class="flex flex-row align-items-center justify-content-center valor-total ">
            <span class="mr-2 flex flex-column align-items-center">Valor Total: </span>
            <span> R${{ valorTotal }}</span>
        </section>
      </tbody>    
    </table>
    <Button @click="salvarPedido" class="mt-2 botao-pedido bg-primary" label="Fechar pedido"></Button>

  </main>
</template>

<style scoped lang="scss">
$largura-tabela: 70vw;

.carrinho-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 0px);
  background-color: #f3f4f6;
  background-repeat: repeat;
  background-size: cover;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

h2 {
  color: #333;
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  text-align: center;
}

.carrinho-tabela {
  width: $largura-tabela;
  max-width: 90%;
  background-color: white;
  border-radius: 0.5rem;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

thead {
  background-color: #e5e7eb;
  text-transform: uppercase;
  font-size: 0.9rem;

  tr {
    border-bottom: 2px solid #ddd;
  }
}

td, th {
  padding: 1rem;
  text-align: center;
  border-bottom: 1px solid #ddd;
}

.Livro {
  width: 80px;
  height: 100px;
  border: 1px solid #ddd;
  border-radius: 0.25rem;
  object-fit: cover;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

Button {
  background-color: #2563eb;
  color: white;
  border: none;
  border-radius: 0.25rem;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: #1d4ed8;
  }

  .pi-trash {
    font-size: 1.2rem;
  }
}

.valor-total {
  font-weight: bold;
  font-size: 1.2rem;
  margin-top: 1rem;
  text-align: center;
}


.botao-pedido {
  background-color: #2563eb;
  color: #fff;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  &:hover {
    background-color: #059669;
  }
}
</style>
