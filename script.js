document.getElementById('encryptBtn').addEventListener('click', function() {
    sendData('encrypt');
});

document.getElementById('decryptBtn').addEventListener('click', function() {
    const keyInput = document.getElementById('keyInput').value;
    if (!keyInput.trim()) {
        alert('Please enter a key to decrypt.');
        return;
    }
    sendData('decrypt');
});

function updateHistory(action, inputText, resultText, keyUsed) {
    const historyDiv = document.getElementById('history');
    const entry = document.createElement('p');
    entry.textContent = action.toUpperCase() === 'ENCRYPT' ?
        `Encrypted "${inputText}" with key "${keyUsed}".` :
        `Attempted to decrypt "${inputText}" with key "${keyUsed}". Result: ${resultText}`;
    historyDiv.prepend(entry); // Prepend to make the latest action appear at the top
}

function sendData(action) {
    const inputText = document.getElementById('inputText').value;
    const key = document.getElementById('keyInput').value;
    const url = `http://127.0.0.1:5000/${action}`;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText, key: key }),
    })
    .then(response => response.json())
    .then(data => {
        const result = data.encrypted || data.decrypted;
        document.getElementById('result').textContent = `Result: ${result}`;
        updateHistory(action, inputText, result, key);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
}
