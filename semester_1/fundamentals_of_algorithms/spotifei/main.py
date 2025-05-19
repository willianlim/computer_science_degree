# Importa os controladores para gerenciar menus de usuário e administrador
from controllers.user_controller import menu_usuario
from controllers.admin_controller import menu_admin

# Importa funções de autenticação e cadastro
from utils.auth import login_usuario
from services.admin_service import cadastrar_administrador
from services.user_service import cadastrar_usuario

# Importa utilitário para exibir menus
from utils.menu_utils import exibir_menu

def main():
    """
    Função principal do programa Spotifei.

    Exibe o menu inicial com as opções de login, cadastro de usuário e cadastro de administrador.
    Gerencia o fluxo do programa com base na escolha do usuário.
    """
    while True:
        # Define as opções do menu principal
        opcoes = ["Login", "Cadastrar Novo Usuário", "Cadastrar Administrador"]

        # Exibe o menu e captura a escolha do usuário
        escolha = exibir_menu(opcoes)

        # Gerencia as opções escolhidas pelo usuário
        if escolha == "1":
            # Realiza o login e redireciona para o menu de administrador ou usuário
            perfil, usuario = login_usuario()
            if perfil is None:
                print("🔄 Retornando ao menu principal...")
                continue
            if perfil == "admin":
                menu_admin(usuario)  # Redireciona para o menu de administrador
            else:
                menu_usuario(usuario)  # Redireciona para o menu de usuário comum
        elif escolha == "2":
            # Cadastra um novo usuário
            cadastrar_usuario()
        elif escolha == "3":
            # Cadastra um novo administrador
            cadastrar_administrador()
        elif escolha == "0":
            # Encerra o programa
            print("👋 Encerrando o programa. Até logo!")
            exit()
        else:
            # Trata opções inválidas
            print("❌ Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    """
    Executa a função principal quando o arquivo é executado diretamente.
    """
    main()