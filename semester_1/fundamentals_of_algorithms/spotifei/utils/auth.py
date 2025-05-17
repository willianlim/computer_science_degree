from services.user_service import cadastrar_usuario, login_usuario

def login_menu():
    while True:
        print("\\n=== Spotifei ===")
        print("1 - Login")
        print("2 - Cadastrar novo usuário")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            return login_usuario()
        elif escolha == "2":
            cadastrar_usuario()
        elif escolha == "0":
            exit()
        else:
            print("❌ Opção inválida.")