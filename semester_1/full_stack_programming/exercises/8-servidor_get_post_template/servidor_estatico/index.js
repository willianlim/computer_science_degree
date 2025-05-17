const express = require("express");
const path = require("path");
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// Simples banco em memória (objeto)
const usuarios = {};

// Rotas

// Página projetos (raiz)
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "projects.html"));
});

// Cadastro - GET exibe o formulário
app.get("/cadastra", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "cadastro.html"));
});

// Cadastro - POST recebe dados do form
app.post("/cadastra", (req, res) => {
  const { usuario, senha } = req.body;
  if (usuarios[usuario]) {
    return res.render("resposta", { mensagem: "Usuário já existe!" });
  }
  usuarios[usuario] = senha;
  res.render("resposta", { mensagem: "Cadastro realizado com sucesso!" });
});

// Login - GET exibe o formulário
app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "login.html"));
});

// Login - POST verifica credenciais
app.post("/login", (req, res) => {
  const { usuario, senha } = req.body;
  if (usuarios[usuario] && usuarios[usuario] === senha) {
    res.render("resposta", { mensagem: `Bem-vindo, ${usuario}! Login realizado.` });
  } else {
    res.render("resposta", { mensagem: "Usuário ou senha inválidos." });
  }
});

// Rodar servidor na porta 80
app.listen(3001, () => {
  console.log("Servidor rodando na porta 80");
});
// Remover rota GET para /cadastra (não precisa mais)
app.get("/cadastra", (req, res) => {
  // Redirecionar para /login para evitar rota quebrada
  res.redirect("/login");
});

// Rota GET /login serve a página com os dois formulários
app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "login.html"));
});