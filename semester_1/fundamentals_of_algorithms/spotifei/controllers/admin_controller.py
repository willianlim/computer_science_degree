def menu_admin(usuario):
    print(f"🎵 Bem-vindo, {usuario} (usuário comum adm)!")
    # controllers/user_controller.py
    while True:
        print("\n👤 Menu do Usuário adm")
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
