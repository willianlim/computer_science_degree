import pandas as pd
import os

CAMINHO_DB = "data/database.xlsx"

def inicializar_excel():
    if not os.path.exists(CAMINHO_DB):
        df = pd.DataFrame(columns=["ID_Usuario", "Nome", "E-mail", "Senha", "Tipo"])
        with pd.ExcelWriter(CAMINHO_DB, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="usuarios")
    else:
        try:
            pd.read_excel(CAMINHO_DB, sheet_name="usuarios")
        except:
            df = pd.DataFrame(columns=["ID_Usuario", "Nome", "E-mail", "Senha", "Tipo"])
            with pd.ExcelWriter(CAMINHO_DB, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
                df.to_excel(writer, index=False, sheet_name="Usuario")

def cadastrar_administrador():
    # inicializar_excel()

    print("\n=== Cadastro de Administrador ===")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    confirmacao = input("Confirme a senha: ").strip()

    if senha != confirmacao:
        print("❌ Senhas não coincidem.")
        return

    df = pd.read_excel(CAMINHO_DB, sheet_name="Usuario")

    if email in df["E-mail"].values:
        print("❌ Já existe um usuário com esse e-mail.")
        return

    novo_id = 1 if df.empty else df["ID_Usuario"].max() + 1

    novo_administrador = pd.DataFrame([{
        "ID_Usuario": novo_id,
        "Nome": nome,
        "E-mail": email,
        "Senha": senha,
        "Tipo": "admin"
    }])

    df = pd.concat([df, novo_administrador], ignore_index=True)

    with pd.ExcelWriter(CAMINHO_DB, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, index=False, sheet_name="usuarios")

    print(f"✅ Administrador '{nome}' cadastrado com sucesso!")