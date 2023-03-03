function getUserInput() {
    var userInput = alert("Please type in the input bar or use the microphone for audio input",);
}
function showOutput() {
    let input = document.getElementById("input").value;
    let output = document.getElementById("output");
    if (input !== "") {
        output.style.display = "block";
    } else {
        output.style.display = "none";
    }
}

