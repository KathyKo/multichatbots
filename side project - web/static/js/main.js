// main.js
let currentBot = '';  // Global variable to store the current bot type

function loadBotChat(botType) {
    currentBot = botType;
    const chatContent = document.getElementById('chat-content');
    chatContent.innerHTML = `<p>Chat with ${botType} bot loaded.</p>`;
    // You can also initialize the chat area here if needed
}

function displayMessage(message, sender) {
    const chatContent = document.getElementById('chat-content');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = message;
    chatContent.appendChild(messageDiv);
}

document.addEventListener('DOMContentLoaded', function() {
    const sendButton = document.getElementById('send-button');
    const userInputField = document.getElementById('user-input');

    sendButton.addEventListener('click', function() {
        const userMessage = userInputField.value.trim();
        if (!userMessage) {
            return; // Don't send empty messages
        }
        
        displayMessage(userMessage, 'user');
        userInputField.value = ''; // Clear the input field

        // AJAX request to the Flask backend
        fetch('/respond', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: userMessage,
                bot_type: currentBot  // Send the current bot type with the request
            }),
        })
        .then(response => response.json())
        .then(data => {
            displayMessage(data.response, 'bot'); // Display the response from the bot
        })
        .catch(error => {
            console.error('Error:', error);
            displayMessage('Error communicating with the bot.', 'bot');
        });
    });
});
