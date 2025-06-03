const http = require('http');
const express = require('express');
const colors = require('colors');
const bodyParser = require('body-parser');
const mongodb = require('mongodb');
const path = require('path');

const MongoClient = mongodb.MongoClient;
const uri = 'mongodb+srv://willianrosendodelima:MOnYS2ox4eaKlUgi@fei.b6docph.mongodb.net/?retryWrites=true&w=majority&appName=FEI';
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

const app = express();

app.use(express.static('./public'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.set('view engine', 'ejs');
app.set('views', './views');

client.connect().then(() => {
    const dbo = client.db("create_and_read");
    const biblioteca = dbo.collection("usuarios");
    const usuariosAuth = dbo.collection("usuarios_auth");
    const carros = dbo.collection("carros");

    // Página inicial
    app.get('/', (req, res) => {
        res.sendFile(path.join(__dirname, 'public', 'login.html'));
    });

    // Cadastro de usuário
    app.post("/cadastro", async (req, res) => {
        const { nome, email, senha } = req.body;

        const existente = await usuariosAuth.findOne({ email });
        if (existente) {
            return res.render('redirect', { redirect: "E-mail já cadastrado!" });
        }

        await usuariosAuth.insertOne({ nome, email, senha });
        res.render('redirect', { redirect: "Cadastro realizado com sucesso!" });
    });

    // Login de usuário
    app.post("/login", async (req, res) => {
        const { email, senha } = req.body;
        const usuario = await usuariosAuth.findOne({ email, senha });

        if (!usuario) {
            return res.render('redirect', { redirect: "Login inválido!" });
        }

        const carrosLista = await carros.find().toArray();
        res.render('listaCarros', { carros: carrosLista });
    });

    // Página de cadastro de carros
    app.get('/carros/cadastrar', (req, res) => {
        res.render('cadastroCarro');
    });

    // Inserir carro
    app.post('/carros/inserir', async (req, res) => {
        const novoCarro = {
            marca: req.body.marca,
            modelo: req.body.modelo,
            ano: parseInt(req.body.ano),
            qtde_disponivel: parseInt(req.body.qtde_disponivel)
        };
        await carros.insertOne(novoCarro);
        const carrosLista = await carros.find().toArray();
        res.render('listaCarros', { carros: carrosLista });
    });

    // Listar carros
    app.get('/carros', async (req, res) => {
        const carrosLista = await carros.find().toArray();
        res.render('listaCarros', { carros: carrosLista });
    });

    // Formulário de edição de carro
    app.get('/carros/editar/:id', async (req, res) => {
        const carro = await carros.findOne({ _id: new mongodb.ObjectId(req.params.id) });
        res.render('editarCarro', { carro });
    });

    // Submissão da edição
    app.post('/carros/editar/:id', async (req, res) => {
        const id = new mongodb.ObjectId(req.params.id);
        const novosDados = {
            marca: req.body.marca,
            modelo: req.body.modelo,
            ano: parseInt(req.body.ano),
            qtde_disponivel: parseInt(req.body.qtde_disponivel)
        };
        await carros.updateOne({ _id: id }, { $set: novosDados });
        const carrosLista = await carros.find().toArray();
        res.render('listaCarros', { carros: carrosLista });
    });

    // Vender carro (decrementa 1 unidade)
    app.get('/carros/vender/:id', async (req, res) => {
        const id = new mongodb.ObjectId(req.params.id);
        const carro = await carros.findOne({ _id: id });
        if (carro.qtde_disponivel > 0) {
            await carros.updateOne({ _id: id }, { $inc: { qtde_disponivel: -1 } });
        }
        const carrosLista = await carros.find().toArray();
        res.render('listaCarros', { carros: carrosLista });
    });

    // Remover carro
    app.get('/carros/remover/:id', async (req, res) => {
        const id = new mongodb.ObjectId(req.params.id);
        await carros.deleteOne({ _id: id });
        const carrosLista = await carros.find().toArray();
        res.render('listaCarros', { carros: carrosLista });
    });

    // Criação de post da biblioteca
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

    // Visualização de posts
    app.get('/posts', async (req, res) => {
        try {
            const posts = await biblioteca.find().toArray();
            res.render('posts', { posts });
        } catch (err) {
            res.send("Erro ao buscar posts");
        }
    });

    const server = http.createServer(app);
    server.listen(3000, () => {
        console.log('Servidor rodando na porta 3000'.rainbow);
    });

}).catch(err => {
    console.error("Erro ao conectar ao MongoDB:", err);
});