from utils.excel_utils import ler_planilha


def login_usuario():
    """
    Realiza o login do usuário.

    Verifica se o e-mail e a senha fornecidos correspondem a um registro na base de dados.
    Retorna o tipo de usuário ("admin" ou "user") e os atributos do usuário ou administrador em caso de sucesso.

    Raises:
        FileNotFoundError: Se o arquivo de banco de dados não for encontrado.
        Exception: Para outros erros inesperados.
    """
    while True:
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()

        try:
            # Lê os dados das planilhas de usuários e administradores
            df_usuarios = ler_planilha("usuarios")
            df_administradores = ler_planilha("administradores")

            # Verifica se o e-mail existe na planilha de administradores
            admin = df_administradores[(df_administradores["email"] == email) & (df_administradores["senha"] == senha)]
            if not admin.empty:
                admin_atributos = admin.iloc[0].to_dict()  # Converte os atributos do administrador para um dicionário
                print(f"✅ Login bem-sucedido. Olá, {admin_atributos['nome']} (Administrador)!")
                return "admin", admin_atributos

            # Verifica se o e-mail existe na planilha de usuários
            usuario = df_usuarios[(df_usuarios["email"] == email) & (df_usuarios["senha"] == senha)]
            if not usuario.empty:
                usuario_atributos = usuario.iloc[0].to_dict()  # Converte os atributos do usuário para um dicionário
                print(f"✅ Login bem-sucedido. Olá, {usuario_atributos['nome']} (Usuário Comum)!")
                return "user", usuario_atributos

            # Caso o e-mail ou senha estejam incorretos
            print("❌ Email ou senha incorretos. Tente novamente.")
            return None, None
        except FileNotFoundError:
            print("❌ Arquivo de banco de dados não encontrado.")
            return None, None
        except Exception as e:
            print(f"❌ Ocorreu um erro ao realizar o login: {e}")
            return None, None