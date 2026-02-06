from utils import print_box, hash_senha, salvar_dados
from usuario import encontrar_usuario

# ====== Funções de Admin ======
def adicionar_pessoa(pessoas):
    print_box("CADASTRO DE USUÁRIO (ADMIN)")
    nome = input("Nome -> ").strip()
    if encontrar_usuario(nome, pessoas):
        print_box("Usuário já existe!", cor="RED")
        return

    idade = input("Idade -> ").strip()
    sexo = input("Sexo -> ").lower().strip()
    senha = input("Senha -> ").strip()
    senha_hashed = hash_senha(senha)

    usuario = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "senha": senha_hashed,
        "SALDO": 0,
        "HISTORICO": []
    }

    pessoas.append(usuario)
    salvar_dados(pessoas)
    print_box("Usuário cadastrado com sucesso!", cor="GREEN")

def listar_pessoas(pessoas):
    print_box("LISTA DE USUÁRIOS")
    if not pessoas:
        print("Cadastro vazio".center(50))
    else:
        for u in pessoas:
            print(f"Nome: {u['nome']} | Idade: {u['idade']} | Sexo: {u['sexo']} | Saldo: R$ {u['SALDO']}")
    print("\n")
