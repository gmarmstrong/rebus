const REBUS_GENERATOR_ENDPOINT = "/puzzle";
var answer;

async function generateRebus(){

	const response = await fetch(REBUS_GENERATOR_ENDPOINT);
	const drawingData = await response.json();
	for (var i = 0; i < drawingData.puzzle.length; i++) {
		document.getElementById('puzzle').innerHTML += drawingData.puzzle[i] + "\n";
	}

	answer = drawingData.answer.trim();
}

function getAnswer(){
	let answerSpace = document.getElementById("answer");
	answerSpace.innerHTML = answer;
}
