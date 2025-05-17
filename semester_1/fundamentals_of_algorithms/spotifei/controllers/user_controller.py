


def menu_usuario(usuario):
    print(f"🎵 Bem-vindo, {usuario} (usuário comum)!")
    # controllers/user_controller.py
    while True:
        print("\n👤 Menu do Usuário")
        print("1 - Buscar músicas")
        print("2 - Curtir música")
        print("3 - Visualizar histórico")
        print("4 - Gerenciar playlists")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            ...
        elif opcao == "4":
            ...
        elif opcao == "0":
            break
