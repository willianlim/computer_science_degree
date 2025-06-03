const http = require('http');
const express = require('express');
const colors = require('colors');
const bodyParser = require('body-parser');
const mongodb = require('mongodb');
const path = require('path');

// Conexão com MongoDB.
const MongoClient = mongodb.MongoClient;
const uri = 'mongodb+srv://willianrosendodelima:wHfFvPVLOO3pCXSE@fei.b6docph.mongodb.net/?retryWrites=true&w=majority&appName=FEI';
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

const app = express();

// Configurações do Express.
app.use(express.static('./public')); // Arquivo estáticos.
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.set('view engine', 'ejs');
app.set('views', './views');

// Conectar ao MongoDB antes de iniciar o servidor.
client.connect().then(() => {
    const dbo = client.db("create_and_read");
    const biblioteca = dbo.collection("usuarios");

    // Rota principal (abre home.html).
    app.get('/', (req, res) => {
        res.sendFile(path.join(__dirname, 'public', 'home.html'));
    });

    // Rota POST: Criação de novo post.
    app.post("/inicio", (req, res) => {
        const data = {
            db_titulo: req.body.titulo,
            db_resumo: req.body.resumo,
            db_conteudo: req.body.conteudo
        };

        biblioteca.insertOne(data, (err) => {
            if (err) {
                res.render('resposta', { resposta: "Erro ao criar o post!" });
            } else {
                res.render('resposta', { resposta: "Post criado com sucesso!" });
            }
        });
    });

    // Rota GET: Visualização dos posts salvos (READ).
    app.get('/posts', async (req, res) => {
        try {
            const posts = await biblioteca.find().toArray();
            res.render('posts', { posts });
        } catch (err) {
            res.send("Erro ao buscar posts");
        }
    });

    // Iniciar servidor.
    const server = http.createServer(app);
    server.listen(3000, () => {
        console.log('Servidor rodando na porta 3000'.rainbow);
    });

}).catch(err => {
    console.error("Erro ao conectar ao MongoDB:", err);
});
