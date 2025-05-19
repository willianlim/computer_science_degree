from utils.excel_utils import ler_planilha


def visualizar_historico(id_usuario):
    """
    Exibe o histórico de músicas curtidas e descurtidas do usuário.
    """
    try:
        # Carregar a planilha de interações de músicas
        df_interacoes = ler_planilha("interacoes_musicas")
        df_musicas = ler_planilha("musicas")

        if df_interacoes.empty:
            print("❌ Nenhuma interação encontrada no histórico.")
            return

        # Filtrar interações do usuário
        interacoes_usuario = df_interacoes[df_interacoes["id_usuario"] == id_usuario]

        if interacoes_usuario.empty:
            print("❌ Nenhuma interação encontrada para o usuário.")
            return

        print("\n=== Histórico de Músicas ===")

        # Exibir músicas curtidas
        musicas_curtidas = interacoes_usuario[interacoes_usuario["curtida"] > 0]
        if not musicas_curtidas.empty:
            print("\n🎵 Músicas Curtidas:")
            for _, row in musicas_curtidas.iterrows():
                musica = df_musicas[df_musicas["id_musica"] == row["id_musica"]].iloc[0]
                print(f"- ID: {musica['id_musica']}, Nome: {musica['nome']}, Artista: {musica['artista']}")
        else:
            print("\n❌ Nenhuma música curtida encontrada.")

        # Exibir músicas descurtidas
        musicas_descurtidas = interacoes_usuario[interacoes_usuario["curtida"] < 0]
        if not musicas_descurtidas.empty:
            print("\n🎵 Músicas Descurtidas:")
            for _, row in musicas_descurtidas.iterrows():
                musica = df_musicas[df_musicas["id_musica"] == row["id_musica"]].iloc[0]
                print(f"- ID: {musica['id_musica']}, Nome: {musica['nome']}, Artista: {musica['artista']}")
        else:
            print("\n❌ Nenhuma música descurtida encontrada.")
    except Exception as e:
        print(f"❌ Erro ao visualizar histórico: {e}")