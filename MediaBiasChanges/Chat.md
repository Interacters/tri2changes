<style>
    .chat-container {
      background: linear-gradient(145deg, #8568e694 0%, #586ed09f 100%);
      border-radius: 24px;
      padding: 32px;
      backdrop-filter: blur(10px);
      margin-bottom: 20px
    }

    .chat-container h1 {
      font-size: 1.75rem;
      margin: 0 0 8px;
      background: linear-gradient(90deg, #60a5fa, #a78bfa, #ec4899, #f59e0b, #60a5fa);
      background-size: 200% auto;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      font-weight: 700;
      letter-spacing: -0.5px;
      animation: gradientShift 3s linear infinite;
    }

    @keyframes gradientShift {
      0% {
        background-position: 0% center;
      }
      100% {
        background-position: 200% center;
      }
    }

    .chat-container p.description {
      margin: 0 0 28px;
      font-size: 0.95rem;
      color: #94a3b8;
      line-height: 1.6;
    }

    .chat-container p.description strong {
      color: #cbd5e1;
      font-weight: 600;
    }

    label {
      display: block;
      font-size: 0.9rem;
      margin-bottom: 8px;
      color: #e2e8f0;
      font-weight: 500;
      letter-spacing: 0.3px;
    }

    textarea {
      width: 100%;
      min-height: 110px;
      resize: vertical;
      padding: 14px 16px;
      font-size: 0.95rem;
      border-radius: 12px;
      border: 2px solid #334155;
      background: #5a5681ff;
      color: #e2e8f0;
      box-sizing: border-box;
      margin-bottom: 20px;
      font-family: inherit;
      transition: all 0.2s ease;
    }

    textarea::placeholder {
      color: #6f8eb8ff;
    }

    textarea:focus {
      outline: none;
      border-color: #60a5fa;
      box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.1);
    }

    select {
      width: 100%;
      padding: 14px 16px;
      font-size: 0.95rem;
      border-radius: 12px;
      border: 2px solid #334155;
      background: #3b4f7fff;
      color: #e2e8f0;
      box-sizing: border-box;
      margin-bottom: 24px;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.2s ease;
      appearance: none;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%2394a3b8' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 12px center;
      padding-right: 40px;
    }

    select:focus {
      outline: none;
      border-color: #60a5fa;
      box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.1);
    }

    select option {
      background: #0f172a;
      color: #e2e8f0;
      padding: 10px;
    }

    .actions {
      display: flex;
      gap: 10px;
      align-items: center;
    }

    button {
      flex: 1;
      padding: 14px 20px;
      border: none;
      border-radius: 12px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
      color: white;
      transition: all 0.3s ease;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
      position: relative;
      overflow: hidden;
    }

    button::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
      transition: left 0.5s ease;
    }

    button:hover::before {
      left: 100%;
    }

    button:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }

    button:active {
      transform: translateY(0);
    }

    button:disabled {
      opacity: 0.5;
      cursor: not-allowed;
      transform: none;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
    }

    button:disabled:hover {
      transform: none;
    }

    .status {
      font-size: 0.9rem;
      margin-top: 16px;
      min-height: 1.2em;
      color: #94a3b8;
      font-weight: 500;
    }

    .status.error {
      color: #f87171;
    }

    .status.success {
      color: #4ade80;
    }

    .response-box {
      margin-top: 20px;
      padding: 20px;
      border-radius: 16px;
      background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
      font-size: 0.95rem;
      max-height: 400px;
      overflow-y: auto;
      border: 2px solid #334155;
      white-space: pre-wrap;
      line-height: 1.7;
      box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.3);
    }

    .response-box::-webkit-scrollbar {
      width: 8px;
    }

    .response-box::-webkit-scrollbar-track {
      background: #0f172a;
      border-radius: 10px;
    }

    .response-box::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 10px;
    }

    .response-box::-webkit-scrollbar-thumb:hover {
      background: #475569;
    }

    .response-box .answer {
      color: #e2e8f0;
    }

    .response-box .label {
      font-weight: 700;
      font-size: 1.05rem;
      background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 12px;
      display: block;
    }
  </style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="ai-card">
    <h3>Source Intel Chat</h3>
    <p>Get help analyzing news sources with AI-powered suggestions</p>
    
    <label>News Source (Optional)</label>
    <textarea id="news-source" placeholder="Type a news source like 'Fox News', 'CNN', 'NBC'..." style="min-height: 60px;"></textarea>
    
    <!-- Smart Prompts -->
    <div id="smart-prompts-section" style="display: none;">
        <p class="chat-hint" style="margin: 8px 0 4px;">💡 Quick Prompts (Most Popular First)</p>
        <div class="ai-prompts" id="smart-prompts-grid"></div>
    </div>
    
    <label>Your Question</label>
    <textarea id="ai-message" placeholder="Ask a question about this news source..." required></textarea>
    
    <label>What do you want?</label>
    <select id="ai-mode" style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); color: #eaf6ff; margin-bottom: 12px;">
        <option value="hint">Hint</option>
        <option value="information">Information</option>
    </select>
    
    <div class="ai-controls">
        <button type="button" class="ai-btn primary" id="ai-send-btn">Send</button>
        <button type="button" class="ai-btn ghost" id="ai-clear-btn">Clear</button>
    </div>
    
    <div class="ai-status" id="ai-status"></div>
    <div class="ai-chat-log" id="ai-chat-log" style="display: none;"></div>
</div>

<script type="module">
import { pythonURI } from '{{site.baseurl}}/assets/js/api/config.js';
const PROMPTS_API_BASE = pythonURI || 'http://localhost:8404';
;
// Smart Prompts Feature
const PROMPT_TEMPLATES = [
    { id: 1, text: "What is the political bias of {source}?" },
    { id: 2, text: "Show me recent top stories from {source}" },
    { id: 3, text: "How does {source} compare to other news outlets?" },
    { id: 4, text: "What are the most controversial topics covered by {source}?" },
    { id: 5, text: "Is {source} a reliable news source?" }
];

const PROMPTS_REFRESH_INTERVAL = 5000;
let promptsWithClicks = [];
let currentSource = '';
let promptRefreshTimer;

const newsSourceInput = document.getElementById('news-source');
const smartPromptsSection = document.getElementById('smart-prompts-section');
const smartPromptsGrid = document.getElementById('smart-prompts-grid');
const aiMessageInput = document.getElementById('ai-message');
const aiModeSelect = document.getElementById('ai-mode');
const aiSendBtn = document.getElementById('ai-send-btn');
const aiClearBtn = document.getElementById('ai-clear-btn');
const aiStatusEl = document.getElementById('ai-status');
const aiChatLog = document.getElementById('ai-chat-log');

function havePromptClicksChanged(nextPrompts) {
    if (promptsWithClicks.length !== nextPrompts.length) return true;
    return nextPrompts.some(next => {
        const existing = promptsWithClicks.find(p => p.id === next.id);
        return !existing || existing.clicks !== next.clicks;
    });
}

// Load prompt click data
async function loadPromptClicks() {
    let nextPrompts;
    try {
        const response = await fetch(`${PROMPTS_API_BASE}/api/prompts/clicks`);
        if (response.ok) {
            const data = await response.json();
            nextPrompts = PROMPT_TEMPLATES.map(prompt => ({
                ...prompt,
                clicks: data[prompt.id] || 0
            }));
        } else {
            nextPrompts = PROMPT_TEMPLATES.map(prompt => ({ ...prompt, clicks: 0 }));
        }
    } catch (error) {
        console.warn('Could not load prompt clicks:', error);
        nextPrompts = PROMPT_TEMPLATES.map(prompt => ({ ...prompt, clicks: 0 }));
    }

    const changed = havePromptClicksChanged(nextPrompts);
    promptsWithClicks = nextPrompts;
    return changed;
}

// Render prompts sorted by popularity
function renderSmartPrompts(source) {
    const trimmedSource = (source || '').trim();
    if (!trimmedSource || trimmedSource.length < 2) {
        currentSource = '';
        smartPromptsSection.style.display = 'none';
        return;
    }

    currentSource = trimmedSource;
    const sorted = [...promptsWithClicks].sort((a, b) => b.clicks - a.clicks);
    smartPromptsGrid.innerHTML = '';
    
    sorted.forEach(prompt => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'ai-prompt-btn';
        
        const promptText = prompt.text.replace('{source}', trimmedSource);
        btn.innerHTML = `<span style="flex: 1;">${promptText}</span> <span style="background: rgba(255,255,255,0.15); padding: 2px 8px; border-radius: 10px; font-size: 0.8rem; font-weight: 700;">${prompt.clicks}</span>`;
        
        btn.addEventListener('click', () => handlePromptClick(prompt, trimmedSource));
        smartPromptsGrid.appendChild(btn);
    });

    smartPromptsSection.style.display = 'block';
}

// Handle prompt click
async function handlePromptClick(prompt, source) {
    const filledPrompt = prompt.text.replace('{source}', source);
    aiMessageInput.value = filledPrompt;

    try {
        const response = await fetch(`${PROMPTS_API_BASE}/api/prompts/${prompt.id}/click`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        
        if (response.ok) {
            const data = await response.json();
            const localPrompt = promptsWithClicks.find(p => p.id === prompt.id);
            if (localPrompt) localPrompt.clicks = data.clicks;
            renderSmartPrompts(source);
        }
    } catch (error) {
        console.error('Failed to increment click count:', error);
    }

    aiMessageInput.focus();
}

// Listen for news source input
let debounceTimeout;
if (newsSourceInput) {
    newsSourceInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimeout);
        const source = e.target.value.trim();
        debounceTimeout = setTimeout(() => renderSmartPrompts(source), 300);
    });
}

async function refreshPromptsFromServer() {
    const changed = await loadPromptClicks();
    if (changed && currentSource) {
        renderSmartPrompts(currentSource);
    }
}

function startPromptLiveUpdates() {
    clearInterval(promptRefreshTimer);
    promptRefreshTimer = setInterval(refreshPromptsFromServer, PROMPTS_REFRESH_INTERVAL);
}

// Show status
function showAIStatus(message, isError = false) {
    aiStatusEl.textContent = message;
    aiStatusEl.style.display = 'block';
    aiStatusEl.style.background = isError ? 'rgba(248, 113, 113, 0.15)' : 'rgba(122, 210, 249, 0.15)';
    aiStatusEl.style.border = isError ? '1px solid rgba(248, 113, 113, 0.3)' : '1px solid rgba(122, 210, 249, 0.3)';
    aiStatusEl.style.color = isError ? '#fca5a5' : '#7ad2f9';
}

aiSendBtn.addEventListener('click', async () => {
    const message = aiMessageInput.value.trim();
    const mode = aiModeSelect.value;

    if (!message) {
        showAIStatus('Please enter a message', true);
        return;
    }

    aiSendBtn.disabled = true;
    aiSendBtn.textContent = 'Thinking...';
    showAIStatus('Processing your request...');
    
    try {
        const response = await fetch(`${pythonURI}/api/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ type: mode, message: message })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error || `Server error: ${response.status}`);
        }

        const data = await response.json();
        
        // Add to chat log
        const userBubble = document.createElement('div');
        userBubble.className = 'chat-bubble user';
        userBubble.textContent = `You: ${message}`;
        
        const aiBubble = document.createElement('div');
        aiBubble.className = 'chat-bubble ai';
        aiBubble.innerHTML = `<strong>${data.type === 'hint' ? '💡 Hint' : '📚 Info'}:</strong> ${data.answer}`;
        
        aiChatLog.appendChild(userBubble);
        aiChatLog.appendChild(aiBubble);
        aiChatLog.style.display = 'block';
        aiChatLog.scrollTop = aiChatLog.scrollHeight;
        
        showAIStatus('Response received!');
        aiMessageInput.value = '';
        
        setTimeout(() => {
            aiStatusEl.style.display = 'none';
        }, 2000);
        
    } catch (error) {
        console.error(error);
        showAIStatus('Error: ' + error.message, true);
    } finally {
        aiSendBtn.disabled = false;
        aiSendBtn.textContent = 'Send';
    }
});

// Clear chat
aiClearBtn.addEventListener('click', () => {
    if (confirm('Clear conversation history?')) {
        aiChatLog.innerHTML = '';
        aiChatLog.style.display = 'none';
        aiMessageInput.value = '';
        newsSourceInput.value = '';
        smartPromptsSection.style.display = 'none';
        currentSource = '';
        showAIStatus('Chat cleared');
        setTimeout(() => {
            aiStatusEl.style.display = 'none';
        }, 2000);
    }
});

// Initialize
loadPromptClicks()
    .then(() => {
        const prefilledSource = newsSourceInput?.value?.trim();
        if (prefilledSource) {
            renderSmartPrompts(prefilledSource);
        }
    })
    .finally(() => {
        startPromptLiveUpdates();
    });
</script>