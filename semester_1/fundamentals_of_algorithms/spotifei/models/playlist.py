class Playlist:
    def __init__(self, id_playlist, nome_playlist, id_usuario, data_hora_criacao=None):
        self.id_playlist = id_playlist
        self.nome_playlist = nome_playlist
        self.id_usuario = id_usuario
        self.data_hora_criacao = data_hora_criacao

    def to_dict(self):
        """Converte o objeto Playlist em um dicionário para salvar no DataFrame."""
        return {
            "id_playlist": self.id_playlist,
            "nome_playlist": self.nome_playlist,
            "id_usuario": self.id_usuario,
            "data_hora_criacao": self.data_hora_criacao,
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Playlist a partir de um dicionário."""
        return Playlist(
            id_playlist=data["id_playlist"],
            nome_playlist=data["nome_playlist"],
            id_usuario=data["id_usuario"],
            data_hora_criacao=data.get("data_hora_criacao"),
        )