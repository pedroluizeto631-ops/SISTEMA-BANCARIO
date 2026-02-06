📌 Sistema Bancário

Um projeto em Python que simula um sistema bancário simples com funcionalidades básicas como cadastro de usuário, login, depósitos, saques e extratos. É ideal pra treinar lógica, estrutura de pastas, modularização e fundamentos de programação 🐍💡

🚀 Funcionalidades

Esse sistema permite, através de um menu no terminal:

✔️ Criar novos usuários

✔️ Autenticar usuários (login)

✔️ Realizar depósitos

✔️ Realizar saques

✔️ Visualizar extratos

✔️ Armazenar dados no arquivo data.json

(Detalhe: o projeto lê e salva usuários e contas nesse JSON para persistência simples sem banco de dados 🗃️)




Principais arquivos:

🧠 main.py — Ponto de entrada do sistema, controla o menu principal

👤 usuario.py — Lógica de criação e autenticação de usuários

🔧 utils.py — Funções utilitárias (leitura/escrita de dados, validações etc.)

⚙️ admin.py — Funções administrativas

📄 data.json — Banco de dados simples (JSON) onde usuários e contas são salvos


📌 Como Usar
1. Clone o Repositório
git clone https://github.com/pedroluizeto631-ops/SISTEMA-BANCARIO.git

2. Navegue até a pasta
cd SISTEMA-BANCARIO

3. Execute o sistema
python main.py


👆 Certifique‑se de ter o Python 3 instalado no seu sistema.


📚 Exemplo de Fluxo

O usuário escolhe Registrar novo usuário

Depois faz Login com e‑mail e senha

No menu após login:

Realiza depósitos

Realiza saques

Visualiza extrato

Sai do sistema quando quiser

🛠️ Tecnologias

🧾 Linguagem: Python 3
📦 Persistência: arquivo JSON
📌 Estilo: modular, organizado por responsabilidades de arquivos


✨ Boas Práticas

Esse projeto é ótimo pra:

Treinar manipulação de arquivos em Python

Entender estrutura de projetos modulares

Trabalhar com menus interativos no terminal

Aprender boas práticas de entrada/saída e validação de dados
============================================================

📄 License

Esse projeto está sob a MIT License — ou seja, você pode usar, modificar e distribuir livremente 🤝
