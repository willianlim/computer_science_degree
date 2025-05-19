import pandas as pd
from datetime import datetime
import uuid
from utils.excel_utils import ler_planilha, salvar_planilha, atualizar_planilha, remover_registro
from models.playlist import Playlist
from models.playlist_musica import PlaylistMusica
from unidecode import unidecode


def gerar_id(prefixo):
    """Gera um identificador único com um prefixo."""
    return f"{prefixo}_{uuid.uuid4().hex[:8]}"


def gerenciar_playlists(id_usuario):
    """
    Gerencia as playlists do usuário.
    """
    print("\n=== Gerenciar Playlists ===")
    while True:
        print("\n1 - Criar nova playlist")
        print("2 - Editar playlist")
        print("3 - Excluir playlist")
        print("4 - Adicionar música à playlist")
        print("5 - Remover música da playlist")
        print("6 - Visualizar playlists")
        print("7 - Visualizar histórico de músicas curtidas/descurtidas")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        opcoes = {
            "1": lambda: criar_playlist(input("Digite o nome da nova playlist: ").strip(), id_usuario),
            "2": lambda: editar_playlist(id_usuario),
            "3": lambda: excluir_playlist(id_usuario),
            "4": lambda: adicionar_musica_playlist(id_usuario),
            "5": lambda: remover_musica_da_playlist(id_usuario),
            "6": lambda: visualizar_playlists(id_usuario),
            "7": lambda: visualizar_historico(id_usuario),
        }

        if opcao == "0":
            print("\nRetornando ao menu principal...")
            break  # Sai do loop e retorna ao menu principal
        elif opcao in opcoes:
            opcoes[opcao]()
        else:
            print("❌ Opção inválida.")

def criar_playlist(nome_playlist, id_usuario):
    """
    Cria uma nova playlist e a salva na planilha.
    """
    if not nome_playlist:
        print("❌ O nome da playlist não pode ser vazio.")
        return

    try:
        df_playlists = ler_planilha("playlists")
        novo_id = gerar_id("pl")
        nova_playlist = Playlist(
            id_playlist=novo_id,
            nome_playlist=nome_playlist,
            id_usuario=id_usuario,
            data_hora_criacao=datetime.now(),
        )
        df_playlists = pd.concat([df_playlists, pd.DataFrame([nova_playlist.to_dict()])], ignore_index=True)
        salvar_planilha("playlists", df_playlists, coluna_unica="id_playlist")
        print(f"✅ Playlist '{nome_playlist}' criada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar a playlist: {e}")


def editar_playlist(id_usuario):
    """
    Edita o nome de uma playlist do usuário.
    """
    try:
        # Carregar as playlists
        df_playlists = ler_planilha("playlists")
        visualizar_playlists(id_usuario)

        # Solicitar o ID da playlist e o novo nome
        id_playlist = input("Digite o ID da playlist que deseja editar: ").strip()
        nova_playlist = input("Digite o novo nome da playlist: ").strip()

        # Verificar se o ID da playlist existe
        if id_playlist in df_playlists["id_playlist"].values:
            # Atualizar o registro na planilha
            atualizar_planilha(
                nome_planilha="playlists",
                identificador_coluna="id_playlist",
                identificador_valor=id_playlist,
                novos_dados={"nome_playlist": nova_playlist}
            )
            print(f"✅ Playlist '{id_playlist}' renomeada para '{nova_playlist}' com sucesso!")
        else:
            print("❌ Playlist não encontrada.")
    except Exception as e:
        print(f"❌ Erro ao editar a playlist: {e}")


def excluir_playlist(id_usuario):
    """
    Exclui uma playlist do usuário, removendo todas as informações relacionadas
    das entidades playlists e playlists_musicas.
    """
    try:
        # Exibir as playlists do usuário
        visualizar_playlists(id_usuario)

        # Solicitar o ID da playlist que deseja excluir
        id_playlist = input("Digite o ID da playlist que deseja excluir: ").strip()

        # Verificar se a playlist existe e pertence ao usuário
        df_playlists = ler_planilha("playlists")
        playlist_usuario = df_playlists[
            (df_playlists["id_playlist"] == id_playlist) &
            (df_playlists["id_usuario"] == id_usuario)
        ]

        if playlist_usuario.empty:
            print("❌ A playlist não pertence ao usuário atual ou não existe.")
            return

        # Remover a playlist da entidade playlists
        remover_registro("playlists", {"id_playlist": id_playlist})

        # Remover os relacionamentos da entidade playlists_musicas
        remover_registro("playlists_musicas", {"id_playlist": id_playlist})

        print(f"✅ Playlist '{id_playlist}' e suas associações foram removidas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao excluir a playlist: {e}")




def adicionar_musica_playlist(id_usuario):
    """
    Adiciona uma música a uma playlist existente ou cria uma nova playlist,
    permitindo que o usuário insira o nome da música e escolha entre músicas com o mesmo nome.
    """
    try:
        # Solicitar o nome da playlist
        nome_playlist = input("Digite o nome da playlist: ").strip()
        if not nome_playlist:
            print("❌ O nome da playlist não pode ser vazio.")
            return

        # Solicitar o nome da música
        nome_musica = input("Digite o nome da música: ").strip()
        if not nome_musica:
            print("❌ O nome da música não pode ser vazio.")
            return

        # Buscar todas as músicas com o nome fornecido
        df_musicas = ler_planilha("musicas")
        musicas_encontradas = df_musicas[
            df_musicas["nome"].str.strip().str.lower().apply(unidecode) == unidecode(nome_musica.lower())
        ]

        if musicas_encontradas.empty:
            print(f"❌ Música '{nome_musica}' não encontrada.")
            return

        # Se houver mais de uma música com o mesmo nome, exibir opções para o usuário
        if len(musicas_encontradas) > 1:
            print("\n⚠️ Foram encontradas várias músicas com o mesmo nome:")
            for _, row in musicas_encontradas.iterrows():
                print(f"- ID: {row['id_musica']}, Nome: {row['nome']}, Artista: {row['id_artista']}, Ano: {row['ano_lancamento']}")

            # Solicitar que o usuário escolha o ID da música
            id_musica = input("\nDigite o ID da música desejada: ").strip()

            # Validar se o ID fornecido está entre as opções listadas
            if id_musica not in musicas_encontradas["id_musica"].astype(str).values:
                print("❌ ID da música inválido.")
                return
        else:
            # Se houver apenas uma música, usar o ID diretamente
            id_musica = musicas_encontradas.iloc[0]["id_musica"]

        # Carregar as playlists e os relacionamentos
        df_playlists = ler_planilha("playlists")
        df_playlist_musica = ler_planilha("playlists_musicas")

        # Buscar a playlist pelo nome
        playlist = buscar_playlist_por_nome(df_playlists, nome_playlist, id_usuario)
        if not playlist:
            print(f"⚠️ Playlist '{nome_playlist}' não encontrada. Criando nova...")
            criar_playlist(nome_playlist, id_usuario)

            # Recarregar o DataFrame após criar a playlist
            df_playlists = ler_planilha("playlists")
            playlist = buscar_playlist_por_nome(df_playlists, nome_playlist, id_usuario)

        # Verificar se a playlist foi encontrada após a criação
        if not playlist:
            print("❌ Erro: Não foi possível encontrar ou criar a playlist.")
            return

        # Verificar se a música já está na playlist
        if verificar_musica_na_playlist(df_playlist_musica, playlist.id_playlist, id_musica):
            print("⚠️ Essa música já está na playlist.")
            return

        # Adicionar a música à playlist
        adicionar_relacionamento_playlist_musica(df_playlist_musica, playlist.id_playlist, id_musica)
        print(f"✅ Música '{nome_musica}' adicionada à playlist '{nome_playlist}' com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao adicionar música à playlist: {e}")


def remover_musica_da_playlist(id_usuario):
    """
    Remove uma música de uma playlist do usuário.
    """
    try:
        # Carregar a tabela playlists_musicas
        df_playlist_musica = ler_planilha("playlists_musicas")
        visualizar_playlists(id_usuario)

        # Solicitar os IDs do usuário
        id_playlist = input("Digite o ID da playlist: ").strip()
        id_musica = input("Digite o ID da música que deseja remover: ").strip()

        # Converter os valores fornecidos pelo usuário para o tipo correto
        id_playlist = str(id_playlist)
        try:
            id_musica = int(id_musica)
        except ValueError:
            print("❌ O ID da música deve ser um número inteiro.")
            return

        # Verificar se a música está na playlist
        registro_existe = not df_playlist_musica[
            (df_playlist_musica["id_playlist"] == id_playlist) &
            (df_playlist_musica["id_musica"] == id_musica)
        ].empty

        if registro_existe:
            # Remover o registro da aba playlists_musicas
            remover_registro("playlists_musicas", {"id_playlist": id_playlist, "id_musica": id_musica})
            print(f"✅ Música '{id_musica}' removida da playlist '{id_playlist}' com sucesso!")
        else:
            print(f"❌ Música '{id_musica}' não encontrada na playlist '{id_playlist}'.")
    except Exception as e:
        print(f"❌ Erro ao remover música da playlist: {e}")


# def visualizar_playlists(id_usuario):
#     """
#     Exibe todas as playlists do usuário.
#     """
#     try:
#         df_playlists = ler_planilha("playlists")
#         playlists_usuario = df_playlists[df_playlists["id_usuario"] == id_usuario]

#         if playlists_usuario.empty:
#             print("❌ Nenhuma playlist encontrada.")
#         else:
#             print("\n🎵 Suas Playlists:")
#             for _, row in playlists_usuario.iterrows():
#                 print(f"- ID: {row['id_playlist']}, Nome: {row['nome_playlist']}")
#     except Exception as e:
#         print(f"❌ Erro ao visualizar playlists: {e}")


def visualizar_playlists(id_usuario):
    """
    Exibe todas as playlists do usuário e as músicas relacionadas a cada playlist.
    """
    try:
        # Carregar as tabelas necessárias
        df_playlists = ler_planilha("playlists")
        df_playlist_musica = ler_planilha("playlists_musicas")
        df_musicas = ler_planilha("musicas")

        # Filtrar as playlists do usuário
        playlists_usuario = df_playlists[df_playlists["id_usuario"] == id_usuario]

        if playlists_usuario.empty:
            print("❌ Nenhuma playlist encontrada.")
        else:
            print("\n🎵 Suas Playlists:")
            for _, playlist in playlists_usuario.iterrows():
                print(f"- ID: {playlist['id_playlist']}, Nome: {playlist['nome_playlist']}")

                # Filtrar as músicas relacionadas à playlist
                musicas_relacionadas = df_playlist_musica[
                    df_playlist_musica["id_playlist"] == playlist["id_playlist"]
                ]

                if musicas_relacionadas.empty:
                    print("   Nenhuma música associada a esta playlist.")
                else:
                    print("   Músicas:")
                    for _, relacao in musicas_relacionadas.iterrows():
                        musica = df_musicas[df_musicas["id_musica"] == relacao["id_musica"]]
                        if not musica.empty:
                            musica_info = musica.iloc[0]
                            print(f"     - ID: {musica_info['id_musica']}, Nome: {musica_info['nome']}, "
                                  f"Artista: {musica_info['id_artista']}, Ano: {musica_info['ano_lancamento']}")
                        else:
                            print(f"     ❌ Música com ID {relacao['id_musica']} não encontrada na planilha 'musicas'.")
    except Exception as e:
        print(f"❌ Erro ao visualizar playlists: {e}")





def buscar_playlist_por_nome(df_playlists, nome_playlist, id_usuario):
    """
    Busca uma playlist pelo nome e ID do usuário.
    """
    playlist_data = df_playlists[
        (df_playlists["nome_playlist"].str.lower() == nome_playlist.lower()) &
        (df_playlists["id_usuario"] == id_usuario)
    ]
    if not playlist_data.empty:
        return Playlist.from_dict(playlist_data.iloc[0].to_dict())
    return None


def verificar_musica_na_playlist(df_playlist_musica, id_playlist, id_musica):
    """
    Verifica se uma música já está associada a uma playlist.
    """
    return not df_playlist_musica[
        (df_playlist_musica["id_playlist"] == id_playlist) &
        (df_playlist_musica["id_musica"] == id_musica)
    ].empty


def adicionar_relacionamento_playlist_musica(df_playlist_musica, id_playlist, id_musica):
    """
    Adiciona um relacionamento entre uma playlist e uma música.
    """
    novo_id = gerar_id("plm")
    nova_relacao = PlaylistMusica(
        id_playlist_musica=novo_id,
        id_playlist=id_playlist,
        id_musica=id_musica,
    )
    df_playlist_musica = pd.concat([df_playlist_musica, pd.DataFrame([nova_relacao.to_dict()])], ignore_index=True)
    salvar_planilha("playlists_musicas", df_playlist_musica, coluna_unica="id_playlist_musica")