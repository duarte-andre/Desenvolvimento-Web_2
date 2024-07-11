import { BACKEND_URL } from "~/models/app";
import type { Emprestimo, EmprestimoLivro, EmprestimoLivroBody } from "../models/emprestiomo"; // Corrigido o nome do módulo 'emprestimo'

export const salvarEmprestimo = (emprestimo: Emprestimo): Promise<Emprestimo | null> => {
  return useFetch<Emprestimo>(`${BACKEND_URL}/livros/`, {
    method: 'POST',
    body: emprestimo
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    });
};

export const salvarEmprestimoLivro = (emprestimo: Array<EmprestimoLivro>): Promise<EmprestimoLivroBody | null> => {
  return useFetch<EmprestimoLivroBody>(`${BACKEND_URL}/emprestimo-livros/`, {
    method: 'POST',
    body: emprestimo
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    });
};

export const getEmprestimoById = (id: number): Promise<Emprestimo | null> => {
  return useFetch<Emprestimo>(`${BACKEND_URL}/emprestimos/${id}`, {
    method: 'GET'
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    });
};
