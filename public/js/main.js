var canvas = document.getElementById("rebusCanvas");
var ctx = canvas.getContext('2d');
const REBUS_GENERATOR_ENDPOINT = "/puzzle";
var answer;

var x = canvas.width/2;
var y = canvas.height/2;
var vx = 4;
var vy = 4;
var loadingBouncer;

function loading(){
	ctx.clearRect(0,0,canvas.width, canvas.height);

	ctx.fillText("Loading...", x, y);
	x += vx;
	y += vy;
	if (x >= canvas.width || x <= 0) {
		vx *= -1;
	}
	if (y >= canvas.height || y < 0) {
		vy *= -1;
	}
}

function animateLoading(){
	loadingBouncer = requestAnimationFrame(animateLoading, canvas);
	loading();
}

async function generateRebus(){
	ctx.fillStyle = "black";
	ctx.font = "40px Arial";
	ctx.textAlign = "center";
	animateLoading();

	const response = await fetch(REBUS_GENERATOR_ENDPOINT);
	const drawingData = await response.json();

	cancelAnimationFrame(loadingBouncer);
	ctx.textAlign = "start";

	answer = drawingData.answer.trim().toLowerCase();
	let txtElems = drawingData.elements.textElements;
	let lineElems = drawingData.elements.shapeElements.lines;
	let rectElems = drawingData.elements.shapeElements.rects;
	let circElems = drawingData.elements.shapeElements.circles;
	let imgElems = drawingData.elements.imageElements;


	ctx.clearRect(0,0,canvas.width, canvas.height);
	for (var i = 0; i < txtElems.length; i++) {
		drawTextElement(txtElems[i]);
	}
	for (var i = 0; i < lineElems.length; i++) {
		drawLine(lineElems[i]);
	}
	for (var i = 0; i < rectElems.length; i++) {
		drawRect(rectElems[i]);
	}
	for (var i = 0; i < circElems.length; i++) {
		drawCircle(circElems[i]);
	}
	for (var i = 0; i < imgElems.length; i++) {
		loadImage(imgElems[i]);
	}
}

function drawTextElement(obj){
	//console.log(obj);
	ctx.font = obj.font;
	ctx.fillStyle = obj.color;
	ctx.fillText( obj.text, obj.x, obj.y);
}

function drawLine(obj){
	ctx.beginPath();
	ctx.moveTo(obj.x1, obj.y1);
	ctx.lineTo(obj.x2, obj.y2);
	ctx.strokeStyle = obj.color;
	ctx.stroke();
}

function drawRect(obj){
	if (obj.fill) {
		ctx.fillStyle = obj.color;
		ctx.fillRect(obj.x, obj.y, obj.width, obj.height);
	} else {
		ctx.strokeStyle = obj.color;
		ctx.strokeRect(obj.x, obj.y, obj.width, obj.height);
	}
}

function drawCircle(obj){
	if (obj.fill) {
		ctx.fillStyle = obj.color;
		ctx.beginPath();
		ctx.arc(obj.x, obj.y, obj.radius, 0, 2*Math.PI);
		ctx.closePath();
		ctx.fill();
	} else {
		ctx.strokeStyle = obj.color;
		ctx.beginPath();
		ctx.arc(obj.x, obj.y, obj.radius, 0, 2*Math.PI);
		ctx.closePath();
		ctx.stroke();
	}
}

function loadImage(obj){
	let img = new Image();
	img.drawingData = obj;
	img.onload = drawImage;
	img.src = obj.src;
}

function drawImage(){
	ctx.drawImage(this, this.drawingData.x, this.drawingData.y);
}

function getAnswer(){
	let answerSpace = document.getElementById("answer");
	answerSpace.innerHTML = answer;
}
