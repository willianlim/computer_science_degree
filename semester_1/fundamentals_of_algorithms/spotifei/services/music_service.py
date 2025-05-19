from models.musica import Musica
from utils.excel_utils import ler_planilha, salvar_planilha, atualizar_planilha
from services.playlist_service import adicionar_musica_playlist
import pandas as pd


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


def registrar_interacao(id_usuario, id_musica, status):
    """
    Registra a interação do usuário com uma música na planilha interacoes_musicas.
    
    :param id_usuario: ID do usuário que interagiu com a música.
    :param id_musica: ID da música que foi curtida ou descurtida.
    :param status: String indicando o status da interação ("curtiu" ou "descurtiu").
    """
    try:
        # Carregar a planilha de interações
        df_interacoes = ler_planilha("interacoes_musicas")
        df_musicas = ler_planilha("musicas")

        # Verificar se já existe uma interação para o usuário e a música
        interacao_existente = df_interacoes[
            (df_interacoes["id_usuario"] == id_usuario) &
            (df_interacoes["id_musica"] == id_musica)
        ]

        # Carregar os dados da música
        musica = df_musicas[df_musicas["id_musica"] == id_musica].iloc[0]
        curtidas_atual = musica["curtidas"]
        descurtidas_atual = musica["descurtidas"]

        if not interacao_existente.empty:
            # Atualizar a interação existente
            index = interacao_existente.index[0]
            interacao_anterior = interacao_existente.iloc[0]["status"]

            # Subtrair a interação anterior
            if interacao_anterior == "curtiu":
                curtidas_atual -= 1
            elif interacao_anterior == "descurtiu":
                descurtidas_atual -= 1

            # Atualizar a nova interação
            df_interacoes.at[index, "status"] = status
            df_interacoes.at[index, "data_interacao"] = pd.Timestamp.now()
        else:
            # Adicionar uma nova interação
            nova_interacao = {
                "id_usuario": id_usuario,
                "id_musica": id_musica,
                "status": status,
                "data_interacao": pd.Timestamp.now()
            }
            df_interacoes = pd.concat([df_interacoes, pd.DataFrame([nova_interacao])], ignore_index=True)

        # Adicionar a nova interação
        if status == "curtiu":
            curtidas_atual += 1
        elif status == "descurtiu":
            descurtidas_atual += 1

        # Atualizar a planilha de músicas
        atualizar_planilha("musicas", "id_musica", id_musica, {
            "curtidas": curtidas_atual,
            "descurtidas": descurtidas_atual
        })

        # Salvar a planilha de interações
        salvar_planilha("interacoes_musicas", df_interacoes, coluna_unica=["id_usuario", "id_musica"])
    except Exception as e:
        print(f"❌ Erro ao registrar interação: {e}")


def curtir_musica(id_usuario, musica):
    """
    Registra a interação de curtir uma música.
    
    :param id_usuario: ID do usuário que curtiu a música.
    :param musica: Objeto Musica que foi curtido.
    """
    try:
        # Registrar a interação na planilha interacoes_musicas
        registrar_interacao(id_usuario, musica.id_musica, status="curtiu")

        print(f"✅ Você curtiu a música '{musica.nome}'!")
    except Exception as e:
        print(f"❌ Erro ao curtir a música: {e}")


def descurtir_musica(id_usuario, musica):
    """
    Registra a interação de descurtir uma música.
    
    :param id_usuario: ID do usuário que descurtiu a música.
    :param musica: Objeto Musica que foi descurtido.
    """
    try:
        # Registrar a interação na planilha interacoes_musicas
        registrar_interacao(id_usuario, musica.id_musica, status="descurtiu")

        print(f"✅ Você descurtiu a música '{musica.nome}'!")
    except Exception as e:
        print(f"❌ Erro ao descurtir a música: {e}")


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
            curtir_musica(id_usuario, musica)
        elif opcao == "2":
            descurtir_musica(id_usuario, musica)
        elif opcao == "3":
            adicionar_musica_playlist(id_usuario)
        elif opcao == "0":
            print("⏩ Música ignorada.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")