// Define o tipo UsuarioCustomizado
export type UsuarioCustomizado = {
    id: number;
    email: string;
    telefone: string | null;
    endereco: string;
    cpf: string;
    is_active: boolean;
    groups: Array<any>;
    user_permissions: Array<any>;
}

export type Categoria = {
    id: number;
    nome: string;
}


// Define o tipo Livro (já definido anteriormente)
export type Livro = {
    id: number;
    nome: string;  // Mapeia titulo -> nome
    foto_capa: string;
    descricao: string;
    numero_paginas: number;
    formato: 'ebook' | 'fisico';
    numero_edicao: number;
    ano_publicacao: number;
    categoria: Categoria;  // Referência a uma categoria
    status: 'APROVADO' | 'PENDENTE' | 'CANCELADO';
    preco: number;  // Mapeia preco_emprestimo -> preco
    quantidade_disponivel: number;
    estrelas: number;
}

export enum STATUS {
    'APROVADO' = 'Aprovado',
    'PENDENTE' = 'Pendente',
    'CANCELADO' = 'Cancelado',
}

// Define o tipo Emprestimo
export type Emprestimo = {
    id: number;
    usuario: UsuarioCustomizado;  // Referência a um usuario
    data_realizacao: string;  // ISO date string
    data_devolucao: string;  // ISO date string
    valor_total: number;
    status: 'ativo' | 'atrasado' | 'devolvido';
    livros: Livro[];  // Array de livros
}

export type EmprestimoLivro = {
    livroFK: Livro;
    quantidade: number;
    emprestimoFK: Emprestimo;
}


export type EmprestimoLivroBody = {
    livroFK: number;
    quantidade: number;
    emprestimoFK: number;
}