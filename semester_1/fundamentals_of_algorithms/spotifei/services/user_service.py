import pandas as pd


CAMINHO_DB = "data/database.xlsx"

from utils.excel_utils import ler_planilha, salvar_planilha
from models.usuario import Usuario

def cadastrar_usuario():
    print("\n=== Cadastro de Novo Usuário ===")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    confirmacao = input("Confirme a senha: ").strip()

    if senha != confirmacao:
        print("❌ Senhas não coincidem.")
        return

    df = ler_planilha("usuarios")

    if email in df["email"].values:
        print("❌ Já existe um usuário com esse e-mail.")
        return

    # Gera um novo ID
    novo_id = 1 if df.empty else df["id_usuario"].max() + 1
    usuario = Usuario(novo_id, nome, email, senha)

    # Salva diretamente usando salvar_planilha
    salvar_planilha("usuarios", pd.DataFrame([usuario.to_dict()]), coluna_unica="id_usuario")
    print(f"✅ Usuário '{nome}' cadastrado com sucesso!")
