from controllers.user_controller import menu_usuario
from controllers.admin_controller import menu_admin
from utils.auth import login_menu
from services.admin_service import cadastrar_administrador

def main():
    while True:
        print("\n=== Spotifei ===")
        print("1 - Login")
        print("2 - Cadastrar Novo Usuário")
        print("3 - Cadastrar Administrador")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            perfil, usuario = login_menu()
            if perfil == "admin":
                menu_admin(usuario)
            else:
                menu_usuario(usuario)
        elif escolha == "2":
            from services.user_service import cadastrar_usuario
            cadastrar_usuario()
        elif escolha == "3":
            cadastrar_administrador()
        elif escolha == "0":
            exit()
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    main()