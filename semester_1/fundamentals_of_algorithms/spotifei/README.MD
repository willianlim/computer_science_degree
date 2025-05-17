pip install pandas openpyxl


spotifei/
├── main.py
│
├── controllers/
│   ├── user_controller.py
│   ├── admin_controller.py
│   └── music_controller.py
│
├── services/
│   ├── user_service.py
│   ├── playlist_service.py
│   ├── music_service.py
│   └── stats_service.py
│
├── models/
│   ├── usuario.py
│   ├── musica.py
│   └── playlist.py
│
├── utils/
│   ├── excel_utils.py      ← ✅ leitura e escrita no database.xlsx
│   ├── auth.py
│   └── validators.py
│
├── data/
│   └── database.xlsx       ← ✅ único arquivo de dados persistentes
│
├── tests/
│   └── test_login.py
│
└── README.md


📦 Nome do Design Utilizado
O padrão que estou utilizando é uma combinação entre:

1. Camadas da Arquitetura MVC adaptada (Model-View-Controller):
Models → Representam entidades como Usuário, Música, etc. (não obrigatório em scripts simples, mas útil para clareza e OO).

Controllers → Interface com o usuário (menus, inputs).

Services → Contêm a lógica de negócio (grande parte das regras).

Utils → Funções auxiliares reutilizáveis (como validação e persistência no Excel).

Data → Armazenamento.

❗ Nota: Em apps sem GUI, o "View" é a própria interação no terminal (print/input), e por isso incluímos esse papel dentro dos controllers/.

2. Domain-Driven Design leve
Estamos separando a lógica de domínio em arquivos especializados por contexto (usuários, playlists, músicas), favorecendo clareza e escalabilidade.

✔️ Vantagens dessa estrutura
Fácil de entender e evoluir.

Ideal para projetos didáticos e médios.

Ajuda a isolar responsabilidades (cada parte do projeto tem seu lugar).

Facilita testes e reutilização.

