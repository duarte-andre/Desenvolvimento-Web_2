import { BACKEND_URL } from "~/models/app";
import type { Pagination } from "~/models/pagination";
import type { Livro } from "~/models/livros";
import axios from "axios";

export const getLivros = (numeroPagina: number = 0): Promise<Pagination<Livro>|null> => {
  return useFetch<Pagination<Livro>>(`${BACKEND_URL}/livros?page=${numeroPagina}`)
    .then(resposta => {
      return Promise.resolve(resposta.data.value);      
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    });
};

export const getLivroById = async (id: string) => {
  const response = await axios.get<Livro>(`${BACKEND_URL}/api/auth/livros/${id}/`);
  return response.data;
};
export const postLivro = async (livro: Livro) => {
  try {
    const { data, error } = await useFetch(`${BACKEND_URL}/api/auth/livros/`, {
      method: 'POST',
      body: livro
    });

    if (error.value) {
      throw new Error(error.value.message);
    }

    return data;
  } catch (error) {
    console.error("Erro ao adicionar livro: ", error);
    throw error;
  }
};
