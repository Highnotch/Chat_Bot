$(document).ready(function () {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatMessages.appendChild(messageElement);
    }

    sendButton.addEventListener('click', async () => {
        const userMessage = userInput.value;
        appendMessage('You', userMessage);
        userInput.value = '';

        // Make an AJAX request to your Flask backend to send the user message
        $.ajax({
            type: 'POST',
            url: '/generate',
            data: { components: userMessage },
            success: function (data) {
                const chatbotResponse = data.response;
                appendMessage('ChatBot', chatbotResponse);
            },
            error: function (error) {
                console.error(error);
            },
        });
    });
});
