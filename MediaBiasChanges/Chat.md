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
<div class="intro-text">
   <h2>AI Chatbox with History</h2>
    <p>Type your question about a news source you're stuck on, choose whether you want a <strong>Hint</strong> or <strong>Information</strong>, then send. You can even ask about popular shows!
      Your conversation history is saved below!
    </p>
</div>
<div class="chat-container">
    <form id="chat-form">
      <label for="message">Your message</label>
      <textarea id="message" placeholder="Ask a question here..." required></textarea>

      <label for="mode">What do you want?</label>
      <select id="mode">
        <option value="hint">Hint</option>
        <option value="information">Information</option>
      </select>

      <div class="actions">
        <button type="submit" id="send-btn">Send</button>
        <button type="button" id="clear-history-btn">Clear History</button>
      </div>
    </form>

    <div id="status" class="status"></div>
    <div id="response" class="response-box" style="display:none;"></div>

    <div class="history-section">
      <h3>Conversation History</h3>
      <div class="stats" id="stats"></div>
      <div id="history-list"></div>
    </div>
  </div>

  <script>
    // ===== REQUIREMENT: LIST/COLLECTION TYPE =====
    // This array stores all conversation history
    let conversationHistory = [];

    // DOM Elements
    const form = document.getElementById('chat-form');
    const messageInput = document.getElementById('message');
    const modeSelect = document.getElementById('mode');
    const statusEl = document.getElementById('status');
    const responseEl = document.getElementById('response');
    const sendBtn = document.getElementById('send-btn');
    const clearHistoryBtn = document.getElementById('clear-history-btn');
    const historyList = document.getElementById('history-list');
    const statsEl = document.getElementById('stats');

    // ===== REQUIREMENT: STUDENT-DEVELOPED PROCEDURE =====
    // Procedure name: processConversationHistory
    // Parameters: historyArray (list), filterType (string), maxItems (number)
    // Return type: array
    // Purpose: Filter and process conversation history based on criteria
    function processConversationHistory(historyArray, filterType, maxItems) {
      // ===== ALGORITHM WITH SEQUENCING, SELECTION, AND ITERATION =====
      
      // SEQUENCING: Steps execute in order
      let filteredHistory = [];
      let hintCount = 0;
      let infoCount = 0;
      
      // ITERATION: Loop through each item in history
      for (let i = 0; i < historyArray.length; i++) {
        let item = historyArray[i];
        
        // SELECTION: Conditional logic to filter and count
        if (filterType === 'all' || item.type === filterType) {
          filteredHistory.push(item);
        }
        
        // Count different types
        if (item.type === 'hint') {
          hintCount++;
        } else if (item.type === 'information') {
          infoCount++;
        }
        
        // SELECTION: Stop if we've reached maxItems
        if (filteredHistory.length >= maxItems) {
          break;
        }
      }
      
      // Return processed data
      return {
        filtered: filteredHistory,
        stats: {
          total: historyArray.length,
          hints: hintCount,
          information: infoCount
        }
      };
    }

    // Helper procedure to add item to history
    function addToHistory(question, answer, type) {
      const timestamp = new Date().toLocaleString();
      conversationHistory.push({
        question: question,
        answer: answer,
        type: type,
        timestamp: timestamp
      });
      
      // ===== REQUIREMENT: CALLS TO PROCEDURE =====
      updateHistoryDisplay();
    }

    // Display history using our procedure
    function updateHistoryDisplay() {
      // ===== REQUIREMENT: CALLS TO PROCEDURE =====
      // Call our student-developed procedure
      const result = processConversationHistory(conversationHistory, 'all', 50);
      
      // Update statistics
      statsEl.textContent = `Total conversations: ${result.stats.total} | Hints: ${result.stats.hints} | Information: ${result.stats.information}`;
      
      // Display filtered history
      if (result.filtered.length === 0) {
        historyList.innerHTML = '<p style="color: #999;">No conversation history yet. Start chatting!</p>';
        return;
      }
      
      historyList.innerHTML = '';
      
      // Show most recent first
      for (let i = result.filtered.length - 1; i >= 0; i--) {
        const item = result.filtered[i];
        const historyItem = document.createElement('div');
        historyItem.className = 'history-item';
        historyItem.innerHTML = `
          <div class="history-question">Q: ${item.question}</div>
          <div class="history-type">${item.type === 'hint' ? '💡 Hint' : '📚 Information'} - ${item.timestamp}</div>
          <div class="history-answer">${item.answer}</div>
        `;
        historyList.appendChild(historyItem);
      }
    }

    // Show status message
    function showStatus(message, type) {
      statusEl.textContent = message;
      statusEl.className = `status ${type} show`;
    }

    // Form submission handler
    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      const message = messageInput.value.trim();
      const mode = modeSelect.value;

      if (!message) {
        showStatus('Please enter a message.', 'error');
        return;
      }

      sendBtn.disabled = true;
      showStatus('Thinking...', 'info');
      responseEl.style.display = 'none';

      try {
        const backendUrl = 'http://localhost:8001/api/chat';

        const res = await fetch(backendUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            type: mode,
            message: message
          })
        });

        if (!res.ok) {
          const errorData = await res.json().catch(() => ({}));
          throw new Error(errorData.error || `Server error: ${res.status}`);
        }

        const data = await res.json();

        showStatus('Response received!', 'success');

        if (data.answer) {
          responseEl.style.display = 'block';
          responseEl.innerHTML = `
            <div class="label">${data.type === 'hint' ? '💡 Hint:' : '📚 Information:'}</div>
            <div class="answer">${data.answer}</div>
          `;
          
          // Add to history
          addToHistory(message, data.answer, data.type);
          
          // Clear input
          messageInput.value = '';
        }

      } catch (err) {
        console.error(err);
        showStatus('Error: ' + err.message, 'error');
        responseEl.style.display = 'none';
      } finally {
        sendBtn.disabled = false;
      }
    });

    // Clear history button
    clearHistoryBtn.addEventListener('click', () => {
      if (confirm('Are you sure you want to clear all conversation history?')) {
        conversationHistory = [];
        updateHistoryDisplay();
        showStatus('History cleared!', 'success');
      }
    });

    // Initialize display
    updateHistoryDisplay();
  </script>