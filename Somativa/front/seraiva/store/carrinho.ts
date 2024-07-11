// stores/carrinho.ts
import { defineStore } from 'pinia';
import type { Livro } from '~/models/livros';

export type CarrinhoItem = {
  livro: Livro;
  quantidade: number;
};

export type Carrinho = {
  livros: Array<CarrinhoItem>;
};

export const useCarrinho = defineStore('carrinhoStore', {
  state: (): Carrinho => ({
    livros: [],
  }),
  actions: {
    adicionarNoCarrinho(novoLivro: Livro) {
      const livroJaExiste = this.getLivroDoCarrinho(novoLivro);
      if (livroJaExiste) {
        livroJaExiste.quantidade += 1;
      } else {
        this.livros.push({ quantidade: 1, livro: novoLivro });
      }
    },
    removerDoCarinho(carrinhoItem: CarrinhoItem) {
      const posicaoNoCarrinho = this.getLivroDoCarrinhoIndex(carrinhoItem.livro);
      if (posicaoNoCarrinho !== -1) {
        this.livros.splice(posicaoNoCarrinho, 1);
      }
    },
    esvaziarCarrinho() {
      this.livros = [];
    },
  },
  getters: {
    estaNoCarrinho: (useCarrinho:Carrinho) => (produtoParaEncontrar: Livro): boolean =>{
      return useCarrinho.livros.findIndex(item=>item.livro.id === produtoParaEncontrar.id) !== -1;
  },
    getLivroDoCarrinho: (state) => (livroParaEncontrar: Livro) => {
      return state.livros.find(item => item.livro.id === livroParaEncontrar.id);
    },
    getLivroDoCarrinhoIndex: (state) => (livroParaEncontrar: Livro) => {
      return state.livros.findIndex(item => item.livro.id === livroParaEncontrar.id);
    },
    getCarrinho: (state) => (): CarrinhoItem[] => {
      return state.livros;
    },
    getValorLivro:  (useCarrinho : Carrinho) => (): Number => {
      let soma = 0;
      useCarrinho.livros.forEach(item=>{
        soma+= (item.livro.preco_emprestimo * item.quantidade)
      })
      return soma;
    },
 
  },
});
