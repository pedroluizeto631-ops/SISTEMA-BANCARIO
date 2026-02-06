from utils import print_box, carregar_dados, salvar_dados, input_numero, hash_senha

# Carrega dados do arquivo
pessoas = carregar_dados()

# =========================
# Funções ADMIN
# =========================
def adicionar_pessoa():
    nome = input("Nome -> ")
    idade = input("Idade -> ")
    sexo = input("Sexo -> ").lower().strip()
    senha = input("Crie uma senha -> ")
    dados = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "SALDO": 0,
        "senha": hash_senha(senha)
    }
    pessoas.append(dados)
    salvar_dados(pessoas)
    print_box("Usuário cadastrado com sucesso!")

def listar_pessoas():
    if not pessoas:
        print_box("Cadastro vazio")
    else:
        for p in pessoas:
            print_box(f"{p['nome']} - {p['idade']} anos - {p['sexo']} - Saldo: R${p['SALDO']}")

# =========================
# Funções USUÁRIO
# =========================
def encontrar_usuario(nome):
    for p in pessoas:
        if p["nome"] == nome:
            return p
    return None

def login_usuario():
    nome = input("Digite seu nome -> ")
    usuario = encontrar_usuario(nome)
    if not usuario:
        print_box("Usuário não encontrado!")
        return None
    senha = input("Digite sua senha -> ")
    if hash_senha(senha) != usuario["senha"]:
        print_box("Senha incorreta!")
        return None
    print_box(f"Login realizado! Bem-vindo {nome}")
    return usuario

def menu_usuario(usuario):
    while True:
        print_box("MENU USUÁRIO")
        opcao = int(input(
            "[1] VER SALDO\n"
            "[2] DEPOSITAR\n"
            "[3] TRANSFERIR\n"
            "[4] SAIR\n"
            "Escolha -> "
        ))

        match opcao:
            case 1:
                print_box(f"Saldo atual: R${usuario['SALDO']}")
            case 2:
                valor = input_numero("Valor -> ")
                usuario["SALDO"] += valor
                salvar_dados(pessoas)
                print_box("Depósito feito!")
            case 3:
                valor = input_numero("Valor -> ")
                if valor > usuario["SALDO"]:
                    print_box("Saldo insuficiente!")
                else:
                    usuario["SALDO"] -= valor
                    salvar_dados(pessoas)
                    print_box("Transferência concluída!")
            case 4:
                break
            case _:
                print_box("Opção inválida!")

def cadastro_usuario():
    nome = input("Nome -> ")
    idade = input("Idade -> ")
    sexo = input("Sexo -> ").lower().strip()
    senha = input("Crie uma senha -> ")
    dados = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "SALDO": 0,
        "senha": hash_senha(senha)
    }
    pessoas.append(dados)
    salvar_dados(pessoas)
    print_box("Cadastro concluído com sucesso!")
    return dados

# =========================
# MENU PRINCIPAL
# =========================
def main():
    while True:
        print_box("BANCO LZT")
        opcao = int(input(
            "[1] ADMIN\n"
            "[2] USUÁRIO\n"
            "[3] SAIR\n"
            "Escolha -> "
        ))

        match opcao:
            case 1:
                while True:
                    print_box("MENU ADMIN")
                    adm = int(input(
                        "[1] CADASTRAR PESSOA\n"
                        "[2] LISTAR PESSOAS\n"
                        "[3] VOLTAR\n"
                        "Escolha -> "
                    ))

                    match adm:
                        case 1:
                            adicionar_pessoa()
                        case 2:
                            listar_pessoas()
                        case 3:
                            break
                        case _:
                            print_box("Opção inválida!")

            case 2:
                # Menu de login ou cadastro
                print_box("USUÁRIO")
                user_op = int(input(
                    "[1] LOGIN\n"
                    "[2] CADASTRO\n"
                    "Escolha -> "
                ))

                match user_op:
                    case 1:
                        usuario = login_usuario()
                        if usuario:
                            menu_usuario(usuario)
                    case 2:
                        usuario = cadastro_usuario()
                        menu_usuario(usuario)
                    case _:
                        print_box("Opção inválida!")

            case 3:
                print_box("Encerrando sistema...")
                break

            case _:
                print_box("Opção inválida!")

if __name__ == "__main__":
    main()
