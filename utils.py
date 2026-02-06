import json
import os
import hashlib

ARQUIVO = "data.json"

# ====== Funções de visual ======
def print_box(text):
    """
    Imprime um texto dentro de um quadrado no console.
    """
    linha = "═" * 50
    print("\n" + linha)
    print(text.center(50))
    print(linha + "\n")

def input_numero(prompt):
    """
    Pede um número positivo ao usuário e trata erros.
    """
    while True:
        try:
            valor = float(input(prompt))
            if valor < 0:
                print("Digite um valor positivo!")
                continue
            return valor
        except ValueError:
            print("Digite apenas números!")

def hash_senha(senha):
    """
    Retorna o hash SHA256 da senha.
    """
    return hashlib.sha256(senha.encode()).hexdigest()

# ====== Funções de armazenamento ======
def salvar_dados(pessoas):
    """
    Salva a lista de pessoas no arquivo JSON.
    """
    with open(ARQUIVO, "w") as f:
        json.dump(pessoas, f, indent=4)

def carregar_dados():
    """
    Carrega os dados do JSON. Retorna lista vazia se o arquivo não existir ou estiver vazio.
    """
    if not os.path.exists(ARQUIVO) or os.path.getsize(ARQUIVO) == 0:
        return []
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
