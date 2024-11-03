let currentWords = [];
let currentIndex = 0;
let score = 0;
let attempts = 0;

document.getElementById('speechButton').addEventListener('click', recognizeSpeech);

function startGame() {
    const level = document.getElementById('level').value;
    fetch(`/pronunciation_game`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `level=${level}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.words) {
            currentWords = data.words;
            currentIndex = 0;
            score = 0;
            attempts = 0;
            document.getElementById('speechButton').disabled = false;
            showNextWord();
        } else {
            document.getElementById('word').innerText = data.error;
        }
    });
}

function showNextWord() {
    if (currentIndex < currentWords.length) {
        document.getElementById('word').innerText = `Telaffuz Et: ${currentWords[currentIndex]}`;
    } else {
        document.getElementById('word').innerText = `Oyun bitti! Skorunuz: ${score}`;
        document.getElementById('speechButton').disabled = true;
    }
}

function recognizeSpeech() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const speechResult = event.results[0][0].transcript.toLowerCase();
        document.getElementById('result').innerText = `Söylediğiniz kelime: ${speechResult}`;
        
        if (speechResult === currentWords[currentIndex].toLowerCase()) {
            score++;
            alert('Doğru!');
        } else {
            alert('Yanlış!');
        }
        attempts++;
        currentIndex++;
        showNextWord();
    };
}
