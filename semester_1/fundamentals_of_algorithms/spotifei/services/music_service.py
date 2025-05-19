from models.musica import Musica
from utils.excel_utils import ler_planilha, salvar_planilha, atualizar_planilha
from services.playlist_service import adicionar_musica_playlist


def buscar_musicas(id_usuario):
    """
    Busca músicas e permite ao usuário interagir com elas.
    
    :param id_usuario: ID do usuário que está interagindo com as músicas.
    """
    termo = input("Digite o nome da música: ").strip()
    if not termo:
        print("❌ O termo de busca não pode ser vazio.")
        return

    try:
        resultados = buscar_musicas_por_nome(termo)
        if resultados.empty:
            print("❌ Nenhuma música encontrada com esse nome.")
            return

        for index, row in resultados.iterrows():
            musica = Musica.from_dict(row)
            exibir_informacoes_musica(musica)
            interagir_com_musica(musica, id_usuario)

    except FileNotFoundError as e:
        print(f"❌ Arquivo não encontrado: {e}")
    except KeyError as e:
        print(f"❌ Coluna ou chave ausente: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def buscar_musicas_por_nome(termo):
    """
    Busca músicas pelo nome na planilha de músicas.
    """
    df_musicas = ler_planilha("musicas")
    return df_musicas[df_musicas["nome"].str.strip().str.lower() == termo.strip().lower()]

def exibir_informacoes_musica(musica):
    """
    Exibe as informações de uma música.
    """
    print(f"\n- Nome: {musica.nome}")
    print(f"  Data de Lançamento: {musica.ano_lancamento}")
    print(f"  Artista: {musica.id_artista}")
    print(f"  Curtidas: {musica.curtidas}")
    print(f"  Descurtidas: {musica.descurtidas}")

def interagir_com_musica(musica, id_usuario):
    """
    Permite ao usuário interagir com uma música (curtir, descurtir, adicionar à playlist).
    """
    while True:
        print("\nO que você gostaria de fazer com essa música?")
        print("1 - Curtir")
        print("2 - Descurtir")
        print("3 - Adicionar à playlist")
        print("0 - Ignorar")
        opcao = input("Escolha: ")

        if opcao == "1":
            musica.curtir()
            atualizar_planilha("musicas", "id_musica", musica.id_musica, {"curtidas": musica.curtidas})
            print(f"✅ Você curtiu a música '{musica.nome}'!")
        elif opcao == "2":
            musica.descurtir()
            atualizar_planilha("musicas", "id_musica", musica.id_musica, {"descurtidas": musica.descurtidas})
            print(f"✅ Você descurtiu a música '{musica.nome}'!")
        elif opcao == "3":
            adicionar_musica_playlist(id_usuario)
        elif opcao == "0":
            print("⏩ Música ignorada.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")