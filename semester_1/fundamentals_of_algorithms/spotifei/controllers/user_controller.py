from services.music_service import buscar_musicas
from services.playlist_service import gerenciar_playlists
from services.stats_service import visualizar_historico
from utils.menu_utils import exibir_menu


def menu_usuario(usuario):
    """
    Menu principal para usuários comuns.
    
    :param usuario: Dicionário contendo os atributos do usuário logado.
    """
    print(f"🎵 Bem-vindo, {usuario['nome']} (usuário comum)!")
    while True:
        opcoes = ["Buscar músicas", "Visualizar histórico", "Gerenciar playlists"]
        escolha = exibir_menu(opcoes)

        if escolha == "1":
            buscar_musicas(usuario["id_usuario"])
        elif escolha == "2":
            visualizar_historico(usuario["id_usuario"])
        elif escolha == "3":
            gerenciar_playlists(usuario["id_usuario"])  # Passa apenas o id_usuario
        elif escolha == "0":
            break
        else:
            print("❌ Opção inválida.")