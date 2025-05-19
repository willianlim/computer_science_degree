def exibir_menu(opcoes):
    """
    Exibe um menu e retorna a opção escolhida pelo usuário.
    
    Args:
        opcoes (list): Lista de strings representando as opções do menu.
    
    Returns:
        str: A opção escolhida pelo usuário.
    """
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao}")
    print("0 - Sair")
    return input("Escolha uma opção: ")