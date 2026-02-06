from utils import print_box, input_numero, hash_senha, salvar_dados

# ====== Funções de Usuário ======
def encontrar_usuario(nome, pessoas):
    for u in pessoas:
        if u["nome"] == nome:
            return u
    return None

def criar_usuario(pessoas):
    print_box("CRIAR CONTA")
    nome = input("Nome -> ").strip()
    if encontrar_usuario(nome, pessoas):
        print_box("Usuario ja existe!", cor="RED")
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
    print_box("Conta criada com sucesso! Agora você pode fazer login.", cor="GREEN")

def login_usuario(pessoas):
    print_box("LOGIN")
    nome = input("Nome -> ").strip()
    usuario = encontrar_usuario(nome, pessoas)
    if not usuario:
        print_box("Usuario nao encontrado", cor="RED")
        return None

    senha = input("Senha -> ").strip()
    if usuario["senha"] != hash_senha(senha):
        print_box("Senha incorreta", cor="RED")
        return None

    print_box(f"Bem vindo {usuario['nome']}!", cor="GREEN")
    return usuario

def menu_usuario(usuario, pessoas):
    while True:
        print_box("MENU USUARIO")
        opcao = input(
            "[1] VER SALDO\n"
            "[2] DEPOSITAR\n"
            "[3] TRANSFERIR\n"
            "[4] VER HISTORICO\n"
            "[5] SAIR\n"
            "Escolha -> "
        ).strip()

        match opcao:
            case "1":
                print_box(f"Saldo atual: R$ {usuario['SALDO']}", cor="MAGENTA")

            case "2":
                valor = input_numero("Valor -> ")
                usuario["SALDO"] += valor
                usuario["HISTORICO"].append(f"Depósito: +R${valor}")
                salvar_dados(pessoas)
                print_box("Depósito feito!", cor="GREEN")

            case "3":
                destino_nome = input("Nome do destinatario -> ").strip()
                destino = encontrar_usuario(destino_nome, pessoas)
                if not destino:
                    print_box("Usuario destino nao encontrado", cor="RED")
                    continue

                valor = input_numero("Valor -> ")
                if valor > usuario["SALDO"]:
                    print_box("Saldo insuficiente!", cor="RED")
                else:
                    usuario["SALDO"] -= valor
                    destino["SALDO"] += valor
                    usuario["HISTORICO"].append(f"Transferência: -R${valor} para {destino_nome}")
                    destino["HISTORICO"].append(f"Recebido: +R${valor} de {usuario['nome']}")
                    salvar_dados(pessoas)
                    print_box("Transferência concluída!", cor="GREEN")

            case "4":
                print_box("HISTÓRICO DE TRANSAÇÕES")
                if not usuario["HISTORICO"]:
                    print("Histórico vazio".center(50))
                else:
                    for item in usuario["HISTORICO"]:
                        print("-", item)

            case "5":
                break

            case _:
                print_box("Opção inválida", cor="RED")

def menu_usuario_principal(pessoas):
    while True:
        print_box("USUARIO", cor="CYAN")
        opcao = input("[1] LOGIN\n[2] CRIAR CONTA\n[3] VOLTAR\nEscolha -> ").strip()

        match opcao:
            case "1":
                usuario = login_usuario(pessoas)
                if usuario:
                    menu_usuario(usuario, pessoas)
            case "2":
                criar_usuario(pessoas)
            case "3":
                break
            case _:
                print_box("Opção inválida", cor="RED")
