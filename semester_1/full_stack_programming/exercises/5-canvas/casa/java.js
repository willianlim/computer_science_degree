const canvas = document.getElementById('meuCanvas02');
const ctx = canvas.getContext('2d');

function piso () {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = 'gray';
    ctx.fillRect(0,450,800,350);
    ctx.closePath();
}
function parteazul01 () {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#458EFC';
    ctx.fillRect(0,440,150,400);
    ctx.closePath();
}
function parteazul02 () {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#458EFC';
    ctx.fillRect(0,650,430,800);
    ctx.closePath();
}
function circuloazul () {
    ctx.beginPath();
    ctx.fillStyle = '#458EFC';
    ctx.lineWidth = 2; 
    ctx.arc(420, 750, 100, 0, 2 * Math.PI);
    ctx.fill();
    ctx.closePath();
}
function circuloazul02 () {
    ctx.beginPath();
    ctx.fillStyle = '#458EFC';
    ctx.lineWidth = 2; 
    ctx.arc(52, 420, 100, 0, 2 * Math.PI);
    ctx.fill();
    ctx.closePath();
}
function arvore01 () {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#86471A';
    ctx.fillRect(150,250,60,200);
    ctx.closePath();
}
function folha01 () {
    ctx.beginPath();
    ctx.fillStyle = 'green';
    ctx.lineWidth = 2; 
    ctx.arc(180, 200, 80, 0, 2 * Math.PI);
    ctx.fill();
    ctx.closePath();
}
function arvore02 () {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#86471A';
    ctx.fillRect(680,430,60,200);
    ctx.closePath();
}
function folha02 () {
    ctx.beginPath();
    ctx.fillStyle = 'green';
    ctx.lineWidth = 2; 
    ctx.arc(710, 380, 80, 0, 2 * Math.PI);
    ctx.fill();
    ctx.closePath();
}
function casinha () {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#86471A';
    ctx.fillRect(320,200,230,250);
    ctx.closePath();
}
function janela01 () {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#47BDFD';
    ctx.fillRect(340,270,80,80);
    ctx.closePath();
}
function janela02 () {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#47BDFD';
    ctx.fillRect(450,270,80,80);
    ctx.closePath();
}
function telhado() {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#F5694D'; 
    ctx.moveTo(320, 200); 
    ctx.lineTo(435, 100); 
    ctx.lineTo(550, 200); 
    ctx.closePath(); 
    ctx.fill(); 
}
function porta() {
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = '#624423';
    ctx.fillRect(410,350,50,100);
    ctx.closePath();
}
function sol() {
    ctx.beginPath();
    ctx.fillStyle = 'yellow';
    ctx.lineWidth = 2; 
    ctx.arc(660, 120, 100, 0, 2 * Math.PI);
    ctx.fill();
    ctx.closePath();
}

piso ();

parteazul01 ();
parteazul02 ();
circuloazul ();
circuloazul02 ();

arvore01 ();
folha01 ();

arvore02 ();
folha02 ();

casinha ();
janela01 ();
janela02 ();
telhado ();
porta ();

sol ();