document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    // Function to add a message to the chat
    function addMessage(message, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.innerHTML = `<p>${message}</p>`;
        
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to the bottom of the chat
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Simple response function (temporary)
    function getBotResponse(userMessage) {
        const lowerMessage = userMessage.toLowerCase();
        
        if (lowerMessage.includes('hello') || lowerMessage.includes('hi')) {
            return "Hello! I'm HealthBot, your medical AI assistant. How can I help you today?";
        } else if (lowerMessage.includes('symptom')) {
            return "I can help you understand your symptoms. Could you please describe what you're experiencing in more detail?";
        } else if (lowerMessage.includes('pain')) {
            return "I'm sorry to hear you're in pain. Could you tell me where the pain is located and how severe it is?";
        } else if (lowerMessage.includes('headache')) {
            return "Headaches can have various causes. Common types include tension headaches, migraines, and cluster headaches. Would you like to know more about any specific type?";
        } else if (lowerMessage.includes('fever')) {
            return "A fever is often a sign of infection. It's important to monitor your temperature and other symptoms. Would you like to know more about managing fever?";
        } else if (lowerMessage.includes('emergency')) {
            return "If this is a medical emergency, please call emergency services immediately. Would you like me to provide emergency contact numbers?";
        } else {
            return "I understand you're concerned about your health. Could you please provide more details about your symptoms or concerns?";
        }
    }

    // Function to handle user input
    function handleUserInput() {
        const message = userInput.value.trim();
        if (message) {
            // Add user message
            addMessage(message, true);
            userInput.value = '';

            // Show typing indicator
            const typingIndicator = document.createElement('div');
            typingIndicator.className = 'message bot-message';
            typingIndicator.innerHTML = '<div class="message-content"><p>HealthBot is typing...</p></div>';
            chatMessages.appendChild(typingIndicator);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            // Simulate bot response
            setTimeout(() => {
                // Remove typing indicator
                chatMessages.removeChild(typingIndicator);
                
                // Get and add bot response
                const response = getBotResponse(message);
                addMessage(response);
            }, 1000);
        }
    }

    // Event listeners
    sendButton.addEventListener('click', handleUserInput);
    
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleUserInput();
        }
    });

    // Sidebar navigation
    const navItems = document.querySelectorAll('nav ul li');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            navItems.forEach(navItem => navItem.classList.remove('active'));
            item.classList.add('active');
        });
    });
}); 