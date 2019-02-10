const REBUS_GENERATOR_ENDPOINT = "/puzzle";
var answer = "undefined";
var drawingData;

async function generateRebus(){
	document.getElementById('puzzle').innerHTML = "Loading...";

	const response = await fetch(REBUS_GENERATOR_ENDPOINT);
	drawingData = await response.json();

	document.getElementById('puzzle').innerHTML = drawingData.puzzle;
	document.getElementById("answer").innerHTML = "";

	answer = drawingData.answer.trim();
}

function showAnswer(){
	let answerSpace = document.getElementById("answer");
	if (answer === "undefined") {
		answerSpace.innerHTML = "You need to generate a rebus first!";
	} else {
		answerSpace.innerHTML = answer;
	}
}
