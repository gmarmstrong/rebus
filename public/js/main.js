var canvas = document.getElementById("rebusCanvas");
var ctx = canvas.getContext('2d');
const REBUS_GENERATOR_ENDPOINT = "/puzzle";
var answer;


async function generateRebus(){
	const response = await fetch(REBUS_GENERATOR_ENDPOINT);
	const drawingJson = await response.json();
	let drawingData = JSON.parse(drawingJson);

	answer = drawingData.answer;
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
		drawLine(rectElems[i]);
	}
	for (var i = 0; i < circElems.length; i++) {
		drawLine(circElems[i]);
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

function checkAnswer(){
	let givenAnswer = document.getElementById("answer").value;
	if (givenAnswer === answer) {
		alert("Yes!");
	}
}
