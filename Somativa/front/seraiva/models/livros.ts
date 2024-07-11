export type Categoria = {
    id: number;
    nome: string;
}



export enum STATUS {
    'APROVADO' = 'Aprovado',
    'PENDENTE' = 'Pendente',
    'CANCELADO' = 'Cancelado',
}

export enum FORMATO {
    'ebook' = 'e',
    'fisico' = 'f',
}




export type Livro = {
    id: number;
    titulo: string;  // Mapeia titulo -> nome
    foto_capa:string;
    descricao: string;
    numero_paginas: number;
    formato:FORMATO; //'ebook' | 'fisico';
    numero_edicao: number;
    ano_publicacao: number;  
    categoria: Categoria;  // Referência a uma categoria
    preco_emprestimo: number;  // Mapeia preco_emprestimo -> preco
    quantidade_disponivel: number;
    estrelas: number;
}

// const variavelType : Livro = {
//     id: 0,
//     nome: '',
//     foto_capa:'',
//     preco: 0,
//     quantidade_disponivel: 0,
//     descricao: '',
//     numero_edicao: 0,
//     ano_publicacao: 0,
//     estrelas:0,



    



    // }