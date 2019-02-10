const REBUS_GENERATOR_ENDPOINT = "/puzzle";
var answer;
var drawingData;

async function generateRebus(){

	const response = await fetch(REBUS_GENERATOR_ENDPOINT);
	drawingData = await response.json();

	document.getElementById('puzzle').innerHTML = drawingData.puzzle;

	answer = drawingData.answer.trim();
}

function showAnswer(){
	let answerSpace = document.getElementById("answer");
	answerSpace.innerHTML = answer;
}
