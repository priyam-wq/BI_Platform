// Initialize icons
lucide.createIcons();

const form = document.getElementById('query-form');
const input = document.getElementById('query-input');
const chatContainer = document.getElementById('chat-container');

function addMessage(text, isUser = false, tokens = null) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${isUser ? 'user' : 'bot'}`;
    
    const avatarDiv = document.createElement('div');
    avatarDiv.className = 'avatar';
    
    const iconName = isUser ? 'user' : 'bot';
    avatarDiv.innerHTML = `<i data-lucide="${iconName}"></i>`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'content';
    contentDiv.textContent = text;
    
    if (tokens) {
        const tokensDiv = document.createElement('div');
        tokensDiv.className = 'token-pill';
        tokensDiv.innerHTML = `<i data-lucide="zap" style="width:12px;height:12px"></i> ${tokens.input} In | ${tokens.output} Out`;
        contentDiv.appendChild(tokensDiv);
    }
    
    msgDiv.appendChild(avatarDiv);
    msgDiv.appendChild(contentDiv);
    
    chatContainer.appendChild(msgDiv);
    lucide.createIcons();
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function showTyping() {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message bot typing-msg';
    msgDiv.id = 'typing-indicator';
    
    msgDiv.innerHTML = `
        <div class="avatar"><i data-lucide="bot"></i></div>
        <div class="content" style="padding: 15px 25px;">
            <div class="typing-indicator">
                <span></span><span></span><span></span>
            </div>
        </div>
    `;
    
    chatContainer.appendChild(msgDiv);
    lucide.createIcons();
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function removeTyping() {
    const indicator = document.getElementById('typing-indicator');
    if (indicator) indicator.remove();
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = input.value.trim();
    if (!query) return;
    
    // Add user message
    addMessage(query, true);
    input.value = '';
    
    // Show typing
    showTyping();
    
    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });
        
        const data = await response.json();
        removeTyping();
        
        if (data.status === 'success') {
            addMessage(data.insight, false, data.tokens);
        } else {
            addMessage('Error: ' + data.message);
        }
    } catch (err) {
        removeTyping();
        addMessage('Failed to connect to the server. Is the backend running?');
    }
});
