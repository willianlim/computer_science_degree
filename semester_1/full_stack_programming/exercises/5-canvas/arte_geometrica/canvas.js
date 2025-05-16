let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d')

//quadrado azul
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'blue';
ctx.strokeStyle = 'blue';
ctx.fillRect(0,0,50,50);
ctx.strokeRect(0,0,50,50);
ctx.closePath();

//quadrado vermelho maior
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'red';
ctx.strokeStyle = 'red';
ctx.fillRect(249,0,50,50); //x=faz ele "andar"; y= mantem "colado" na linha superior; ultimos dois sao as dimensoes
ctx.strokeRect(249,0,50,50); 
ctx.closePath();

//quadrado vermelho menor
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'red';
ctx.strokeStyle = 'red';
ctx.fillRect(120,150,30,30); //x=faz ele "andar"; y= mantem "colado" na linha superior; ultimos dois sao as dimensoes
ctx.strokeRect(120,150,30,30); 
ctx.closePath();

//quadrado azul claro - lado direito
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'aqua';
ctx.strokeStyle = 'aqua';
ctx.fillRect(274,137,26,26); //x=faz ele "andar"; y= mantem "colado" na linha superior; ultimos dois sao as dimensoes
ctx.strokeRect(274,137,26,26); 
ctx.closePath();

//retangulo azul claro - lado esquerdo
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'aqua';
ctx.strokeStyle = 'aqua';
ctx.fillRect(0,125,26,50); //x=faz ele "andar"; y= mantem "colado" na linha superior; ultimos dois sao as dimensoes
ctx.strokeRect(0,125,26,50); 
ctx.closePath();

//quadrado preto
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'black';
ctx.fillRect(250,250,50,50);
ctx.closePath();

//quadrado branco - p/ o preto
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'white';
ctx.fillRect(250,250,25,25);
ctx.closePath();

//quadrado amarelo
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'yellow';
ctx.fillRect(0,250,50,50);
ctx.closePath();

//quadrado branco - p/ o amarelo
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'white';
ctx.fillRect(25,250,25,25);
ctx.closePath();

//linha azul
ctx.beginPath();
ctx.strokeStyle = 'blue';
ctx.moveTo(0, 0);
ctx.lineTo(150, 150);
ctx.stroke();
ctx.closePath();

//linha vermelha
ctx.beginPath();
ctx.strokeStyle = 'red';
ctx.moveTo(300, 0);
ctx.lineTo(150, 150);
ctx.stroke();
ctx.closePath();

//linha do meio horizontal
ctx.beginPath();
ctx.strokeStyle = 'green';
ctx.moveTo(0, 150);
ctx.lineTo(300, 150);
ctx.stroke();
ctx.closePath();

//linha do meio vertical
ctx.beginPath();
ctx.strokeStyle = 'blue';
ctx.moveTo(150, 150);
ctx.lineTo(150, 300);
ctx.stroke();
ctx.closePath();

//aro azul claro 
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'aqua';
ctx.strokeStyle = 'green';
ctx.arc(150,300,30,0, 2 * Math.PI); //x,y definem o centro do circulo
ctx.fill();
ctx.stroke();
ctx.closePath();

//bolinha do meio
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'aqua';
ctx.strokeStyle = 'blue';
ctx.arc(150,120,15,0, 2 * Math.PI); //x,y definem o centro do circulo
ctx.fill();
ctx.stroke();
ctx.closePath();

//aro verde 180
ctx.beginPath();
ctx.lineWidth = 2;
ctx.strokeStyle = 'green';
ctx.arc(150,150,60,1 * Math.PI, 2 * Math.PI); //x,y definem o centro do circulo
ctx.stroke();
ctx.closePath();

//aro lateral direita verde - cima
ctx.beginPath();
ctx.lineWidth = 2;
ctx.strokeStyle = 'green';
ctx.arc(150,150,80,1.75 * Math.PI, 2 * Math.PI); //x,y definem o centro do circulo
ctx.stroke();
ctx.closePath();

//aro lateral esquerda verde - cima
ctx.beginPath();
ctx.lineWidth = 2;
ctx.strokeStyle = 'green';
ctx.arc(150,150,80,1 * Math.PI, 1.25 * Math.PI); //x,y definem o centro do circulo
ctx.stroke();
ctx.closePath();

//aro lateral direita verde - baixo
ctx.beginPath();
ctx.lineWidth = 2;
ctx.strokeStyle = 'green';
ctx.arc(150,300,60,1.50 * Math.PI, 2 * Math.PI); //x,y definem o centro do circulo
ctx.stroke();
ctx.closePath();

//aro lateral esquerda verde - baixo
ctx.beginPath();
ctx.lineWidth = 2;
ctx.strokeStyle = 'green';
ctx.arc(150,300,80,1 * Math.PI, 1.5 * Math.PI); //x,y definem o centro do circulo
ctx.stroke();
ctx.closePath();

//bolinha do direita
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'yellow';
ctx.strokeStyle = 'green';
ctx.arc(75,225,15,0, 2 * Math.PI); //x,y definem o centro do circulo
ctx.fill();
ctx.stroke();
ctx.closePath();

//bolinha da direita
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'yellow';
ctx.strokeStyle = 'green';
ctx.arc(225,225,15,0, 2 * Math.PI); //x,y definem o centro do circulo
ctx.fill();
ctx.stroke();
ctx.closePath();

// texto
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'black';
ctx.font = "25px Arial"
ctx.textAlign = "center";
ctx.fillText("Canvas",150,50);
ctx.closePath();