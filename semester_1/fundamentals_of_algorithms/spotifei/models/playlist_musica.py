class PlaylistMusica:
    def __init__(self, id_playlist_musica, id_playlist, id_musica):
        self.id_playlist_musica = id_playlist_musica
        self.id_playlist = id_playlist
        self.id_musica = id_musica

    def to_dict(self):
        """Converte o objeto PlaylistMusica em um dicionário para salvar no DataFrame."""
        return {
            "id_playlist_musica": self.id_playlist_musica,
            "id_playlist": self.id_playlist,
            "id_musica": self.id_musica,
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto PlaylistMusica a partir de um dicionário."""
        return PlaylistMusica(
            id_playlist_musica=data["id_playlist_musica"],
            id_playlist=data["id_playlist"],
            id_musica=data["id_musica"],
        )