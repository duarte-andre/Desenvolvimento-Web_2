export type UsuarioCustomizado = {
    id: number;
    email: string;
    telefone: string;
    cpf: string;
    endereco: string;
    is_active: boolean;
    groups: Array<string | number>;
    user_permissions: Array<string>;
}