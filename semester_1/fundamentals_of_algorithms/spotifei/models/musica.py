class Musica:
    def __init__(self, id_musica, nome, id_artista, curtidas=0, descurtidas=0, ano_lancamento=None):
        self.id_musica = id_musica
        self.nome = nome
        self.id_artista = id_artista
        self.curtidas = curtidas
        self.descurtidas = descurtidas
        self.ano_lancamento = ano_lancamento  # Corrigido para corresponder ao banco de dados

    def curtir(self):
        """Incrementa o número de curtidas."""
        self.curtidas += 1

    def descurtir(self):
        """Incrementa o número de descurtidas."""
        self.descurtidas += 1

    def to_dict(self):
        """Converte o objeto Musica em um dicionário para salvar no DataFrame."""
        return {
            "id_musica": self.id_musica,
            "nome": self.nome,
            "id_artista": self.id_artista,
            "curtidas": self.curtidas,
            "descurtidas": self.descurtidas,
            "ano_lancamento": self.ano_lancamento,  # Corrigido para corresponder ao banco de dados
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Musica a partir de um dicionário."""
        return Musica(
            id_musica=data["id_musica"],
            nome=data["nome"],
            id_artista=data["id_artista"],
            curtidas=data.get("curtidas", 0),
            descurtidas=data.get("descurtidas", 0),
            ano_lancamento=data["ano_lancamento"],  # Corrigido para corresponder ao banco de dados
        )