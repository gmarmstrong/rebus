var canvas = document.getElementById("rebusCanvas");
var ctx = canvas.getContext('2d');

var rot = Math.PI/64;

function thisIsPointless(){
	ctx.clearRect(0,0,canvas.width, canvas.height);
	ctx.translate(canvas.width/2, canvas.height/2);
	ctx.rotate(rot);
	ctx.font = "72px Comic Sans MS";
	ctx.fillStyle = "#FF69B4";
	ctx.textAlign = "center";
	ctx.fillText("CoMiNg SoOn", 0, 0);
	ctx.translate(-canvas.width/2, -canvas.height/2);
}

function generateRebus(){
	thisIsPointless();
	requestAnimationFrame(generateRebus, canvas);
}
