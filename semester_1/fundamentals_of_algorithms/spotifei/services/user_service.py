import pandas as pd
import os

CAMINHO_DB = "data/database.xlsx"
CODIGO_ADMIN = "ADM2025"

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
                df.to_excel(writer, index=False, sheet_name="usuarios")

def cadastrar_usuario():
    # inicializar_excel()

    print("\n=== Cadastro de Novo Usuário ===")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    confirmacao = input("Confirme a senha: ").strip()
    codigo = input("Código de administrador (opcional): ").strip()

    if senha != confirmacao:
        print("❌ Senhas não coincidem.")
        return

    tipo = "admin" if codigo == CODIGO_ADMIN else "user"

    df = pd.read_excel(CAMINHO_DB, sheet_name="Usuario")

    if email in df["E-mail"].values:
        print("❌ Já existe um usuário com esse e-mail.")
        return

    novo_id = 1 if df.empty else df["ID_Usuario"].max() + 1

    novo_usuario = pd.DataFrame([{
        "ID_Usuario": novo_id,
        "Nome": nome,
        "E-mail": email,
        "Senha": senha,
        "Tipo": tipo
    }])

    df = pd.concat([df, novo_usuario], ignore_index=True)

    with pd.ExcelWriter(CAMINHO_DB, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, index=False, sheet_name="Usuario")

    print(f"✅ Usuário '{nome}' cadastrado como {tipo}!")

def login_usuario():
    # inicializar_excel()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    df = pd.read_excel(CAMINHO_DB, sheet_name="Usuario")

    user = df[(df["E-mail"] == email) & (df["Senha"] == senha)]
    if not user.empty:
        tipo = user.iloc[0]["Tipo"]
        nome = user.iloc[0]["Nome"]
        print(f"✅ Login bem-sucedido. Olá, {nome}!")
        return tipo, nome
    else:
        print("❌ Email ou senha inválidos.")
        return login_usuario()