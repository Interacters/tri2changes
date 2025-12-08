---
layout: post
title: "English Essay Help"
permalink: /digital-famine/media-lit/submodule_2/
parent: "Analytics/Admin"
team: "Scratchers"
submodule: 2
categories: [CSP, Submodule, Analytics/Admin]
tags: [analytics, submodule, curators]
breadcrumb: true
microblog: true
author: "Interactors"
date: 2025-12-2
---
## Bias Media Sources
<div class="page-content">
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  min-height: 100vh;
  background: url('{{ site.baseurl }}/MediaBiasChanges/media/assets/spacebackground.jpg') no-repeat center center fixed;
  background-size: cover;
  background-color: #061226;
  padding: 20px;
}

/* Center everything */
.page-content {
  max-width: 1400px;
  margin: 0 auto;
}

.intro-text {
  background: rgba(0,0,30,0.85);
  padding: 20px;
  border-radius: 12px;
  font-family: "Inter", system-ui, sans-serif;
  font-size: 1.05rem;
  margin-bottom: 20px;
  line-height: 1.5;
  color: #e2e8f0;
}
.game-container {
    background: linear-gradient(135deg, #353e74ff, #9384d5ff);
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    margin: 20px 0;
    font-family: system-ui, -apple-system, sans-serif;
}
.game-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid rgba(255,255,255,0.5);
}

.player-info {
    display: flex;
    gap: 20px;
    align-items: center;
}

.info-pill {
    background: rgba(255,255,255,0.5);
    padding: 8px 15px;
    border-radius: 20px;
    font-weight: 600;
    color: #2c5282;
}

.bins-container {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin: 20px 0;
}

.bin {
    flex: 1;
    min-height: 150px;
    background: rgba(255,255,255,0.4);
    border: 2px dashed #4299e1;
    border-radius: 10px;
    padding: 15px;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.bin.highlight {
    background: rgba(255,255,255,0.6);
    border-color: #2b6cb0;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(66,153,225,0.2);
}

.bin-label {
    font-weight: 600;
    color: #2c5282;
    margin-bottom: 10px;
}

.images-area {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    padding: 20px;
    background: rgba(255,255,255,0.3);
    border-radius: 10px;
    min-height: 100px;
}

.image {
    width: 80px;
    height: 80px;
    padding: 8px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    cursor: grab;
    transition: transform 0.2s ease, opacity 0.2s ease;
}

.image:hover {
    transform: translateY(-2px);
}

.image.dragging {
    opacity: 0.5;
    transform: scale(0.95);
}

.controls {
    display: flex;
    justify-content: flex-end;
    gap: 15px;
    margin-top: 20px;
}

.btn {
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    border: none;
}

.btn-primary {
    background: #4299e1;
    color: white;
}

.btn-ghost {
    background: rgba(255,255,255,0.5);
    color: #2c5282;
}

.btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(66,153,225,0.2);
}

.leaderboard {
  /* darker, more visible card for leaderboard */
  background: linear-gradient(180deg, rgba(95, 73, 174, 0.18), rgba(60, 97, 156, 0.4));
  border-radius: 10px;
  padding: 20px;
  margin-top: 20px;
  color: #ffffffff; /* light text on darker background */
  border: 1px solid rgba(255,255,255,0.04);
}

.leaderboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.leaderboard-table {
    width: 100%;
    border-collapse: collapse;
}

.leaderboard-table th,
.leaderboard-table td {
  padding: 10px;
  text-align: left;
  color: inherit; /* use leaderboard color (light) */
}

.leaderboard-table tr:nth-child(even) {
  background: rgba(255,255,255,0.02);
}

/* --- Source Intel Chat styles --- */
.ai-card {
  background: linear-gradient(160deg, #3b3567ff, #33417aff);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  padding: 18px;
  margin: 30px 0 10px;
  color: #eaf6ff;
  box-shadow: 0 12px 30px rgba(0,0,0,0.25);
}
.ai-card h3 {
  margin-top: 0;
  margin-bottom: 8px;
  color: #e4f1ff;
}
.ai-card p {
  margin-top: 4px;
  color: #c8d7eb;
}
.ai-card label {
  font-weight: 600;
  display: block;
  margin: 12px 0 6px;
}
.ai-card textarea {
  width: 100%;
  min-height: 90px;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.1);
  padding: 10px;
  background: rgba(255,255,255,0.05);
  color: #eaf6ff;
  resize: vertical;
}
.ai-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}
.ai-btn {
  flex: 1;
  min-width: 160px;
  padding: 10px 14px;
  border: none;
  border-radius: 10px;
  color: #0e2038;
  font-weight: 700;
  cursor: pointer;
  transition: transform 0.15s ease, box-shadow 0.2s ease;
}
.ai-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 14px rgba(0,0,0,0.25);
}
.ai-btn.primary { background: #7ad2f9; }
.ai-btn.secondary { background: #9be7c4; }
.ai-btn.ghost {
  background: rgba(255,255,255,0.1);
  color: #d6e6ff;
  border: 1px solid rgba(255,255,255,0.15);
}
.ai-status {
  margin-top: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  display: none;
  font-weight: 600;
}
.ai-chat-log {
  margin-top: 16px;
  background: rgba(0,0,0,0.25);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 10px;
  max-height: 320px;
  overflow-y: auto;
  padding: 12px;
}
.chat-bubble {
  padding: 10px 12px;
  border-radius: 10px;
  margin-bottom: 10px;
  line-height: 1.45;
}
.chat-bubble.user {
  background: rgba(122,210,249,0.12);
  border: 1px solid rgba(122,210,249,0.3);
}
.chat-bubble.ai {
  background: rgba(155,231,196,0.12);
  border: 1px solid rgba(155,231,196,0.3);
}
.chat-hint {
  color: #9bb3d6;
  font-size: 0.95rem;
}
</style>

<div class="game-container">
    <div class="game-header">
        <div class="player-info">
            <div class="info-pill" id="player-name">Player: Guest</div>
            <div class="info-pill" id="timer">Time: 0:00</div>
        </div>
        <button class="btn btn-primary" id="auth-btn">Sign In</button>
    </div>
    
    <div class="bins-container">
        <div class="bin" data-bin="Left">
            <div class="bin-label">Left</div>
            <div class="bin-content"></div>
        </div>
        <div class="bin" data-bin="Center">
            <div class="bin-label">Center</div>
            <div class="bin-content"></div>
        </div>
        <div class="bin" data-bin="Right">
            <div class="bin-label">Right</div>
            <div class="bin-content"></div>
        </div>
    </div>

    <div class="images-area" id="images"></div>

    <div class="controls">
    <button class="btn btn-ghost" id="reset-btn">Reset</button>
    <button class="btn btn-ghost" id="autofill-images" title="Autofill images">Autofill</button>
    <button class="btn btn-primary" id="submit-btn">Submit Score</button>
    </div>

    <div class="leaderboard">
        <div class="leaderboard-header">
            <h3>Top Players</h3>
            <button class="btn btn-ghost" id="refresh-lb">Refresh</button>
        </div>
        <table class="leaderboard-table">
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Player</th>
                    <th>Time</th>
                </tr>
            </thead>
            <tbody id="leaderboard-body">
                <!-- Leaderboard data will be inserted here -->
            </tbody>
        </table>
    </div>
</div>
  <style>
    .chat-container {
      background: linear-gradient(145deg, #8373b9b3 0%, #5c77b6c1 100%);
      width: 480px;
      border-radius: 24px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5),
                  0 0 0 1px rgba(255, 255, 255, 0.05);
      padding: 32px;
      backdrop-filter: blur(10px);
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
<div class="chat-container">
    <h3>AI Chatbox with History</h3>
    <p class="description">
      Type your question, choose whether you want a <strong>Hint</strong> or <strong>Information</strong>, then send.
      Your conversation history is saved below!
    </p>

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

<!-- REPLACE YOUR ENTIRE SCRIPT SECTION WITH THIS -->
<script type="module">
import {pythonURI} from '{{site.baseurl}}/assets/js/api/config.js';

// Register name with backend
async function registerPlayer(name) {
    try {
        const response = await fetch(pythonURI + '/api/media/person/get', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: name })
        });
        if (response.ok) {
            const data = await response.json();
            console.log('Player registered:', data);
            return data;
        } else {
            console.error('Failed to register player:', response.status);
            return null;
        }
    } catch (error) {
        console.error('Error registering player:', error);
        return null;
    }
}
// expose register for global usage
window.registerPlayer = registerPlayer;

// Build modal DOM
function buildSignInModal() {
    const modal = document.createElement('div');
    modal.id = 'auth-modal';
    modal.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(0,0,0,0.8);display:flex;align-items:center;justify-content:center;z-index:10000;';
    modal.innerHTML = `
        <div style="background:linear-gradient(135deg, #353e74ff, #9384d5ff);padding:40px;border-radius:20px;box-shadow:0 10px 40px rgba(0,0,0,0.3);text-align:center;max-width:420px;">
            <h2 style="color:#ffffff;margin-bottom:10px;font-size:1.6rem;">Sign In</h2>
            <p style="color:#c8d7eb;margin-bottom:18px;">Enter your name to save your scores</p>
            <input type="text" id="signin-name-input" placeholder="Your Name" style="width:100%;padding:12px;border-radius:10px;border:2px solid #4299e1;font-size:1rem;margin-bottom:14px;background:rgba(136, 134, 172, 0.9);" />
            <div style="display:flex;gap:10px;">
                <button id="signin-cancel-btn" style="flex:1;padding:12px;border-radius:10px;background:rgba(255,255,255,0.2);color:white;font-weight:700;border:none;cursor:pointer;">Cancel</button>
                <button id="signin-submit-btn" style="flex:1;padding:12px;border-radius:10px;background:#4299e1;color:white;font-weight:700;border:none;cursor:pointer;">Sign In</button>
            </div>
            <p id="signin-error" style="color:#ff6b6b;margin-top:10px;display:none;font-size:0.9rem;"></p>
        </div>
    `;
    return modal;
}

// Show sign-in modal on-demand (called by #auth-btn)
window.showSignInPrompt = async function() {
    // if modal already present, focus input
    if (document.getElementById('auth-modal')) {
        const input = document.getElementById('signin-name-input');
        if (input) input.focus();
        return;
    }
    const modal = buildSignInModal();
    document.body.appendChild(modal);

    const input = document.getElementById('signin-name-input');
    const submitBtn = document.getElementById('signin-submit-btn');
    const cancelBtn = document.getElementById('signin-cancel-btn');
    const errorMsg = document.getElementById('signin-error');

    cancelBtn.addEventListener('click', () => modal.remove());

    submitBtn.addEventListener('click', async () => {
        const name = input.value.trim();
        if (name.length < 2) {
            errorMsg.textContent = 'Name must be at least 2 characters';
            errorMsg.style.display = 'block';
            return;
        }
        submitBtn.disabled = true;
        submitBtn.textContent = 'Signing in...';

        let result = true;
        try {
            if (typeof window.registerPlayer === 'function') {
                result = await window.registerPlayer(name);
            }
        } catch (err) {
            console.warn('registerPlayer call failed or not available', err);
            result = true;
        }

        if (result) {
            // persist name and reload so other module picks it up (simplest reliable approach)
            sessionStorage.setItem('playerName', name);
            window.location.reload();
        } else {
            errorMsg.textContent = 'Failed to sign in. Please try again.';
            errorMsg.style.display = 'block';
            submitBtn.disabled = false;
            submitBtn.textContent = 'Sign In';
        }
    });

    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') submitBtn.click();
    });

    input.focus();
};

// Sign out (clears session and reloads)
window.signOut = function() {
    sessionStorage.removeItem('playerName');
    window.location.reload();
};

// Update auth button text/handler
window.updateAuthButton = function() {
    const authBtn = document.getElementById('auth-btn');
    if (!authBtn) return;
    const name = sessionStorage.getItem('playerName');
    if (name) {
        authBtn.textContent = 'Sign Out';
        authBtn.onclick = () => window.signOut();
    } else {
        authBtn.textContent = 'Sign In';
        authBtn.onclick = () => window.showSignInPrompt();
    }
};

// Initialize auth state when DOM is ready
window.addEventListener('DOMContentLoaded', () => {
    window.updateAuthButton();
});
</script>
  

<script type="module">
    console.log("✅ Game script loaded");
    import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

    // Configuration
    const IMAGE_BASE = '{{site.baseurl}}/media/assets/';
    const imageFiles = [
        { src: "atlanticL.png", company: "Atlantic", bin: "Left" },
        { src: "buzzfeedL.png", company: "Buzzfeed", bin: "Left" },
        { src: "cnnL.png", company: "CNN", bin: "Left" },
        { src: "epochR.png", company: "Epoch Times", bin: "Right" },
        { src: "forbesC.png", company: "Forbes", bin: "Center" },
        { src: "hillC.png", company: "The Hill", bin: "Center" },
        { src: "nbcL.png", company: "NBC", bin: "Left" },
        { src: "newsweekC.png", company: "Newsweek", bin: "Center" },
        { src: "nytL.png", company: "NY Times", bin: "Left" },
        { src: "voxL.png", company: "Vox", bin: "Left" },
        { src: "wtR.png", company: "Washington Times", bin: "Right" },
        { src: "bbcC.png", company: "BBC", bin: "Center" },
        { src: "callerR.png", company: "The Daily Caller", bin: "Right" },
        { src: "dailywireR.png", company: "Daily Wire", bin: "Right" },
        { src: "federalistR.png", company: "Federalist", bin: "Right" },
        { src: "foxR.png", company: "Fox News", bin: "Right" },
        { src: "marketwatchC.png", company: "MarketWatch", bin: "Center" },
        { src: "newsmaxR.png", company: "Newsmax", bin: "Right" },
        { src: "nprL.png", company: "NPR", bin: "Left" },
        { src: "reutersC.png", company: "Reuters", bin: "Center" },
        { src: "wsjC.png", company: "Wall Street Journal", bin: "Center" },
        { src: "abcL.png", company: "ABC", bin: "Left"},
        { src: "timeL.png", company: "Time", bin: "Left"},
        { src: "yahooL.png", company: "Yahoo News", bin: "Left"},
        { src: "newsnationC.png", company: "News Nation", bin: "Center"},
        { src: "reasonC.png", company: "Reason News", bin: "Center"},
        { src: "sanC.png", company: "SAN News", bin: "Center"},
        { src: "nypR.png", company: "New York Post", bin: "Right"},
        { src: "upwardR.png", company: "Upward News", bin: "Right"},
        { src: "cbnR.png", company: "CBN", bin: "Right"}
    ];

    // ===== Shared localStorage utility =====
const STORAGE_KEY = 'biasGameData_v1';
const DEFAULT_DATA = {
  profiles: {},
  gameState: {},
  meta: { lastModule: null, showInstructions: true },
  _version: 1
};

function _safeGet(key) {
  try { return localStorage.getItem(key); }
  catch (err) { console.warn('localStorage read error', err); return null; }
}

function _safeSet(key, value) {
  try { localStorage.setItem(key, value); }
  catch (err) { console.warn('localStorage write error', err); }
}

function loadData() {
  const raw = _safeGet(STORAGE_KEY);
  if (!raw) return JSON.parse(JSON.stringify(DEFAULT_DATA));
  try {
    const parsed = JSON.parse(raw);
    // Merge with defaults to tolerate older/partial formats
    const merged = Object.assign({}, DEFAULT_DATA, parsed);
    merged.profiles = Object.assign({}, DEFAULT_DATA.profiles, parsed.profiles || {});
    merged.gameState = Object.assign({}, DEFAULT_DATA.gameState, parsed.gameState || {});
    merged.meta = Object.assign({}, DEFAULT_DATA.meta, parsed.meta || {});
    return merged;
  } catch (err) {
    console.warn('Failed to parse storage; returning defaults', err);
    return JSON.parse(JSON.stringify(DEFAULT_DATA));
  }
}

function saveData(data) {
  try {
    data._version = DEFAULT_DATA._version;
    _safeSet(STORAGE_KEY, JSON.stringify(data));
  } catch (err) {
    console.warn('Failed to save storage', err);
  }
}

function clearGameStateForIds(ids = []) {
  const data = loadData();
  if (!data.gameState) data.gameState = {};
  ids.forEach(id => {
    if (Object.prototype.hasOwnProperty.call(data.gameState, id)) {
      delete data.gameState[id];
    }
  });
  saveData(data);
}

    // CHANGED: Removed lives variable
    let currentPlayer = "Guest";
    let placedImages = new Set();
    let timerHandle = null;
    let gameStarted = false;

    // CHANGED: Removed livesDisplay reference
    const playerDisplay = document.getElementById('player-name');
    const timerDisplay = document.getElementById('timer');
    const bins = document.querySelectorAll('.bin');
    const imagesArea = document.getElementById('images');

    // TIMER UTILITIES - NEW
    function startTimer() {
        const startedAt = Date.now();
        let seconds = 0;
        const interval = setInterval(() => {
            seconds++;
            updateTimerDisplay(seconds);
        }, 1000);
        
        return {
            stop: () => {
                clearInterval(interval);
                const total = Math.round((Date.now() - startedAt) / 1000);
                return total;
            },
            getSeconds: () => seconds
        };
    }

    function updateTimerDisplay(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        if (timerDisplay) {
            timerDisplay.textContent = `Time: ${minutes}:${secs.toString().padStart(2, '0')}`;
        }
    }

    // CHANGED: Removed lives and score updates
    function updateDisplays() {
        playerDisplay.textContent = `Player: ${currentPlayer}`;
    }

    function slugify(text) {
  return 'img-' + String(text).toLowerCase().replace(/[^\w]+/g, '_').replace(/^_+|_+$/g, '');
}

    function createImageCard(file, index) {
        const img = document.createElement('img');
        img.src = IMAGE_BASE + file.src;
        img.alt = file.company;
        img.className = 'image';
        img.draggable = true;
        img.dataset.bin = file.bin;
        img.dataset.company = file.company;
        // CHANGED: stable id based on company name (slug) so saved placements persist across reloads
        img.dataset.id = slugify(file.company);

        img.addEventListener('dragstart', (e) => {
            // Start timer on first interaction
            if (!gameStarted) {
                gameStarted = true;
                timerHandle = startTimer();
                console.log("⏱️ Timer started!");
            }
            
            e.target.classList.add('dragging');
            e.dataTransfer.setData('text/plain', e.target.dataset.id);
        });

        img.addEventListener('dragend', (e) => {
            e.target.classList.remove('dragging');
        });

        return img;
    }

    // CHANGED: Removed lives reset
    function initGame() {
        imagesArea.innerHTML = '';
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');
        placedImages.clear();
        gameStarted = false;
        
        // Stop any existing timer
        if (timerHandle) {
            timerHandle.stop();
            timerHandle = null;
        }
        
        // Reset timer display
        if (timerDisplay) {
            timerDisplay.textContent = 'Time: 0:00';
        }
        
        updateDisplays();

        const getRandomSubset = (arr, count) => {
            return [...arr]
                .sort(() => 0.5 - Math.random())
                .slice(0, count);
        };

        const leftImages = imageFiles.filter(img => img.bin === "Left");
        const centerImages = imageFiles.filter(img => img.bin === "Center");
        const rightImages = imageFiles.filter(img => img.bin === "Right");

        // Load storage and try to reuse previous round's image set (by stable ids)
        const data = loadData();
        data.meta = data.meta || {};

        let selectedImages = null;
        if (Array.isArray(data.meta.roundImages) && data.meta.roundImages.length === 21) {
            // map saved ids back to files (ensure all are present)
            const idMap = new Map(imageFiles.map(f => [slugify(f.company), f]));
            const files = data.meta.roundImages.map(id => idMap.get(id)).filter(Boolean);
            if (files.length === 21) {
                selectedImages = files;
            }
        }

        // If no valid saved round, pick a new random set and persist its ids
        if (!selectedImages) {
            selectedImages = [
                ...getRandomSubset(leftImages, 7),
                ...getRandomSubset(centerImages, 7),
                ...getRandomSubset(rightImages, 7)
            ].sort(() => 0.5 - Math.random());

            data.meta.roundImages = selectedImages.map(f => slugify(f.company));
            saveData(data);
        }

        // create and append cards for the selectedImages
        selectedImages.forEach((file) => {
            const card = createImageCard(file);
            imagesArea.appendChild(card);
        });

    // ===== restore saved placements for images shown =====
    document.querySelectorAll('img.image').forEach(img => {
        const id = img.dataset.id;
        const zone = data.gameState && data.gameState[id];
        if (zone) {
            const bin = document.querySelector(`.bin[data-bin="${zone}"]`);
            if (bin) {
                bin.querySelector('.bin-content').appendChild(img);
                placedImages.add(id);
                img.style.opacity = '1';
                img.style.cursor = 'grab';
            }
        }
    });
    // ensure lastModule meta
    data.meta.lastModule = 'sortingGame';
    saveData(data);
    }

    // Autofill helper
    function autofillImageGame(showAlert = false) {
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');
        const imgs = Array.from(document.querySelectorAll('img.image'));
        let correctCount = 0;
        const data = loadData();
        data.gameState = data.gameState || {};

        imgs.forEach(img => {
            const target = img.dataset.bin;
            const id = img.dataset.id;
            const bin = Array.from(document.querySelectorAll('.bin')).find(b => b.dataset.bin === target);
            if (bin) {
                bin.querySelector('.bin-content').appendChild(img);
                img.style.opacity = '1';
                img.style.cursor = 'grab';
                placedImages.add(id);
                data.gameState[id] = target; // persist
                correctCount++;
            }
        });

        saveData(data);
        updateDisplays();
        if (showAlert) alert(`Autofill placed ${correctCount} images into their correct bins.`);
    }

    // CHANGED: Images can be moved freely between bins
    bins.forEach(bin => {
        bin.addEventListener('dragover', e => {
            e.preventDefault();
            bin.classList.add('highlight');
        });

        bin.addEventListener('dragleave', () => {
            bin.classList.remove('highlight');
        });

        bin.addEventListener('drop', e => {
            e.preventDefault();
            bin.classList.remove('highlight');
            
            const id = e.dataTransfer.getData('text/plain');
            const img = document.querySelector(`[data-id="${id}"]`);
            
            if (!img) return;

            // Remove from placedImages if moving to a different bin
            placedImages.delete(id);
            
            // Place the image in the new bin
            bin.querySelector('.bin-content').appendChild(img);
            placedImages.add(id);
            
            // Reset opacity to show it's movable
            img.style.opacity = '1';
            img.style.cursor = 'grab';

            // ===== persist placement =====
    const data = loadData();
    data.gameState = data.gameState || {};
    data.gameState[id] = bin.dataset.bin;
    saveData(data);
    // ===== end persist =====
    
    updateDisplays();
        });
    });

async function fetchUser() {
    // Check if name is already set from name entry modal
    const savedName = sessionStorage.getItem('playerName');
    if (savedName) {
        currentPlayer = savedName;
        updateDisplays();
        return;
    }
    
    // Fallback to old method
    try {
        const response = await fetch(pythonURI + '/api/person/get', fetchOptions);
        if (response.ok) {
            const data = await response.json();
            currentPlayer = data.name || data.username || 'Guest';
        }
    } catch (err) {
        console.warn('Failed to fetch user:', err);
    }
    updateDisplays();
}

async function postScore(username, finalTime) {
    try {
        const response = await fetch(`${pythonURI}/api/media/score/${encodeURIComponent(username)}/${finalTime}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });
        if (!response.ok) throw new Error('Failed to save score');
        fetchLeaderboard();
    } catch (err) {
        console.error('Error saving score:', err);
    }
}

    async function fetchLeaderboard() {
    const tbody = document.getElementById('leaderboard-body');
    try {
        const response = await fetch(pythonURI + '/api/media/leaderboard');
        if (!response.ok) throw new Error('Failed to fetch leaderboard');
        const data = await response.json();
        
        tbody.innerHTML = '';
        data.forEach((entry, index) => {
            const row = tbody.insertRow();
            row.insertCell().textContent = entry.rank || (index + 1);
            row.insertCell().textContent = entry.username || 'Unknown';
            // CHANGED: Use 'time' instead of 'score' and format it
            const timeInSeconds = entry.time || 0;
            const minutes = Math.floor(timeInSeconds / 60);
            const seconds = timeInSeconds % 60;
            row.insertCell().textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        });
    } catch (err) {
        console.error('Error fetching leaderboard:', err);
        tbody.innerHTML = '<tr><td colspan="3">Unable to load leaderboard</td></tr>';
    }
}

    function showCongrats() {
        // create overlay
        const msg = document.createElement('div');
        msg.style.position = 'fixed';
        msg.style.top = '0';
        msg.style.left = '0';
        msg.style.width = '100vw';
        msg.style.height = '100vh';
        msg.style.background = 'rgba(0,0,0,0.55)';
        msg.style.display = 'flex';
        msg.style.alignItems = 'center';
        msg.style.justifyContent = 'center';
        msg.style.zIndex = '9999';

        // modal content (no links, neutral message)
        msg.innerHTML = `
          <div style="background: #6a75c8ff;padding:28px;border-radius:14px;box-shadow:0 8px 32px rgba(0,0,0,0.2);text-align:center;max-width:420px;">
            <h2 style="color: #546dbeff;margin-bottom:8px;">Congratulations!</h2>
            <p style="color: #e6f0ff;margin:0 0 18px;font-size:1.05rem;">
              Congratulations on mastering media bias.
            </p>
            <button id="return-to-game" style="padding:10px 18px;border-radius:8px;background:#4299e1;color:white;border:none;cursor:pointer;font-weight:700;">
              Return to Game
            </button>
          </div>
        `;

        document.body.appendChild(msg);

        // close modal on button click
        const btn = document.getElementById('return-to-game');
        if (btn) {
          btn.addEventListener('click', () => {
            msg.remove();
          });
        }
    }

    function showIncorrectFeedback(incorrectImages) {
        const modal = document.createElement('div');
        modal.style.position = 'fixed';
        modal.style.top = '0';
        modal.style.left = '0';
        modal.style.width = '100vw';
        modal.style.height = '100vh';
        modal.style.background = 'rgba(0,0,0,0.7)';
        modal.style.display = 'flex';
        modal.style.alignItems = 'center';
        modal.style.justifyContent = 'center';
        modal.style.zIndex = '9999';
        
        const imageGrid = incorrectImages.map(img => 
            `<div style="display:flex;align-items:center;gap:12px;margin:10px 0;padding:10px;background:rgba(255,100,100,0.15);border-radius:8px;">
                <img src="${img.src}" alt="${img.name}" style="width:50px;height:50px;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.2);">
                <div style="text-align:left;">
                    <div style="font-weight:700;color:#ff6b6b;font-size:1.05rem;">${img.name}</div>
                    <div style="font-size:0.9rem;color:#ffb3b3;">Currently in: ${img.currentBin}</div>
                </div>
            </div>`
        ).join('');
        
        modal.innerHTML = `
            <div style="background:linear-gradient(135deg, #2d3561, #4a5080);padding:30px;border-radius:18px;box-shadow:0 12px 40px rgba(0,0,0,0.4);max-width:500px;max-height:80vh;overflow-y:auto;">
                <h2 style='color:#ffd6d6;margin-bottom:8px;text-align:center;'>⚠️ Incorrect Placements</h2>
                <p style='color:#c8d7eb;text-align:center;margin-bottom:20px;font-size:1rem;'>
                    ${incorrectImages.length} source${incorrectImages.length > 1 ? 's are' : ' is'} in the wrong bin. Keep trying!
                </p>
                <div style="margin:20px 0;">
                    ${imageGrid}
                </div>
                <button id="close-feedback" style='width:100%;margin-top:15px;padding:12px;border-radius:10px;background:#4299e1;color:white;font-weight:700;border:none;cursor:pointer;font-size:1.05rem;'>
                    Try Again
                </button>
            </div>
        `;
        
        document.body.appendChild(modal);
        
        document.getElementById('close-feedback').addEventListener('click', () => {
            modal.remove();
        });
        
        // Also close on background click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.remove();
            }
        });
    }
async function submitFinalTime(username, elapsed) {
    try {
        const response = await fetch(`${pythonURI}/api/media/score/${encodeURIComponent(username)}/${elapsed}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });
        if (!response.ok) throw new Error('Failed to save score');
        console.log(`✅ Score saved: ${username} - ${elapsed}s`);
        fetchLeaderboard();
    } catch (err) {
        console.error('Error saving score:', err);
        alert('Failed to save your score. Please try again.');
    }
}

    window.addEventListener('DOMContentLoaded', () => {
        console.log("🚀 DOM fully loaded — initializing game & buttons");

        initGame();
        console.log("✅ Game initialized automatically");

        const resetBtn = document.getElementById('reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                console.log("🔁 Reset clicked");
                // clear saved placements only for images currently on the board
                const ids = Array.from(document.querySelectorAll('img.image')).map(i => i.dataset.id);
                clearGameStateForIds(ids);

                // also clear the persisted round selection so a fresh random set is chosen
                const data = loadData();
                if (data.meta && data.meta.roundImages) {
                    delete data.meta.roundImages;
                    saveData(data);
                }

                initGame();
            });
        }

        const autofillBtn = document.getElementById('autofill-images');
        if (autofillBtn) {
            autofillBtn.addEventListener('click', () => {
                console.log("✨ Autofill clicked");
                autofillImageGame(true);
            });
        }

        // CHANGED: Submit validates and shows incorrect placements
        const submitBtn = document.getElementById('submit-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                console.log("📨 Submit clicked");

                const totalImages = document.querySelectorAll('.image').length;
                const placedCount = placedImages.size;

                if (placedCount < totalImages) {
                    alert(`You haven't placed all the images yet! You've placed ${placedCount} out of ${totalImages}.`);
                    return;
                }

                // Check for correct placement and collect incorrect ones
                let incorrectImages = [];
                document.querySelectorAll('.bin').forEach(bin => {
                    bin.querySelectorAll('.image').forEach(img => {
                        if (img.dataset.bin !== bin.dataset.bin) {
                            incorrectImages.push({
                                name: img.dataset.company,
                                currentBin: bin.dataset.bin,
                                src: img.src
                            });
                        }
                    });
                });

                if (incorrectImages.length > 0) {
                    showIncorrectFeedback(incorrectImages);
                    return;
                }

                // Stop timer and get final time
                if (timerHandle) {
                    const elapsed = timerHandle.stop();

                    // Persist prompts + attempt locally (minimal addition)
                    try {
                      const d = loadData();
                      d.attempts = d.attempts || [];
                      const prompts = (d.meta && d.meta.currentChatPrompts) ? d.meta.currentChatPrompts.slice() : [];
                      d.attempts.push({ username: currentPlayer || 'Guest', time: Number(elapsed) || 0, at: Date.now(), prompts });
                      // clear ephemeral prompts for next run
                      if (d.meta) delete d.meta.currentChatPrompts;
                      saveData(d);
                    } catch (err) {
                      console.warn('save attempt with prompts failed', err);
                    }

                    submitFinalTime(currentPlayer, elapsed);
                    
                    const minutes = Math.floor(elapsed / 60);
                    const seconds = elapsed % 60;
                    alert(`Completed in ${minutes}:${seconds.toString().padStart(2, '0')}!`);
                    
                    showCongrats();
                    initGame();
                } else {
                    alert("Timer not started. Please play the game first!");
                }
            });
        }
    });

    // Initialize
    window.onload = () => {
        console.log("🌎 Window fully loaded — starting game");
        fetchUser();
        initGame();
        fetchLeaderboard();
        setInterval(fetchLeaderboard, 30000);
    };
</script>

<!-- Citation Generator -->
<style>
  .cite-card { background: linear-gradient(160deg,  #555dc2d2, #564ea0ff); color:#e6f2ff; padding:18px; border-radius:12px; margin:20px 0; }
  .cite-row { display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-top:8px; }
  .cite-label { min-width:110px; font-weight:700; color:#d6e9ff; }
  .cite-input, .cite-select { flex:1; padding:8px; border-radius:6px; border:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02); color:inherit; }
  .cite-actions { display:flex; gap:10px; margin-top:12px; justify-content:flex-end; }
  .cite-btn { padding:8px 12px; border-radius:8px; border:none; cursor:pointer; font-weight:700; }
  .cite-btn.primary { background:#7ad2f9; color:#082033; }
  .cite-btn.ghost { background:rgba(255,255,255,0.06); color:#d6e6ff; border:1px solid rgba(255,255,255,0.04); }
  .cite-output { margin-top:12px; background:rgba(0,0,0,0.25); padding:12px; border-radius:8px; font-family:system-ui, -apple-system, sans-serif; color:#eaf6ff; }
  .cite-small { font-size:0.9rem; color:#9fb7da; margin-top:6px; }
</style>

<div class="cite-card" id="citation-tool">
  <h3 style="margin:0 0 8px 0;">Citation Generator</h3>
  <div class="cite-row">
    <div class="cite-label">Style</div>
    <select id="cite-style" class="cite-select">
      <option value="apa">APA</option>
      <option value="mla">MLA (9th ed.)</option>
      <option value="chicago">Chicago (author-date)</option>
    </select>
  </div>

  <div class="cite-row">
    <div class="cite-label">Author(s)</div>
    <input id="cite-author" class="cite-input" placeholder="e.g., Doe, J.; Last, F." />
  </div>

  <div class="cite-row">
    <div class="cite-label">Date</div>
    <input id="cite-date" class="cite-input" placeholder="e.g., 2025, May 10 or 2025" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Title</div>
    <input id="cite-title" class="cite-input" placeholder="Article title (no italics markup)" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Source</div>
    <input id="cite-source" class="cite-input" placeholder="e.g., The New York Times" />
  </div>

  <div class="cite-row">
    <div class="cite-label">URL</div>
    <input id="cite-url" class="cite-input" placeholder="https://..." />
    <button id="cite-fetch-metadata" class="cite-btn ghost" title="Fetch metadata from URL" style="margin-left:8px;min-width:120px;">Fetch from URL</button>
  </div>

  <div class="cite-actions">
    <button id="cite-generate" class="cite-btn primary">Generate</button>
    <button id="cite-copy" class="cite-btn ghost">Copy</button>
    <button id="cite-save" class="cite-btn ghost" title="Save locally">Save</button>
    <button id="cite-load" class="cite-btn ghost" title="Load last">Load</button>
  </div>

  <div id="cite-output" class="cite-output" aria-live="polite"></div>
  <div class="cite-small">Formats: APA, MLA (9th ed.), Chicago (author-date). Saved citations are stored locally in your browser.</div>
</div>

<script>
(function(){
  const styleEl = document.getElementById('cite-style');
  const authorEl = document.getElementById('cite-author');
  const dateEl = document.getElementById('cite-date');
  const titleEl = document.getElementById('cite-title');
  const sourceEl = document.getElementById('cite-source');
  const urlEl = document.getElementById('cite-url');
  const outEl = document.getElementById('cite-output');
  const fetchBtn = document.getElementById('cite-fetch-metadata');

  // DEV default -> ensure this points to your Flask backend (no trailing slash)
if (!window.fetchProxyBase) {
    window.fetchProxyBase = 'http://localhost:8001/api/media';
    console.info('fetchProxyBase defaulted to', window.fetchProxyBase);
}

  const KEY = 'biasGame_citations_v1';

  function safe(val, fallback='') { return (val || '').trim(); }

  function fmtAPA({author, date, title, source, url}) {
    const d = date || 'n.d.';
    const auth = author || 'Doe, J.';
    const src = source ? `${source}.` : '';
    const link = url ? ` ${url}` : '';
    return `${auth} (${d}). ${title ? `<i>${title}</i>` : '<i>Untitled</i>'} ${src}${link}`;
  }

  function fmtMLA9({author, date, title, source, url}) {
    // Simple MLA 9th ed web citation: Author. "Title." Source, Day Month Year, URL.
    const auth = author ? `${author}.` : 'Doe, John.';
    const t = title ? `"${title}."` : `"Untitled."`;
    const src = source ? `${source},` : '';
    const d = date ? `${date},` : '';
    const link = url ? ` ${url}` : '';
    return `${auth} ${t} ${src} ${d}${link}`.replace(/\s+/g,' ').trim();
  }

  function fmtChicago({author, date, title, source, url}) {
    // Chicago author-date simple web citation: Author. Year. "Title." Source. URL.
    const auth = author || 'Doe, John';
    const year = (date || '').split(',')[0].trim() || 'n.d.';
    const t = title ? `"${title}."` : `"Untitled."`;
    const src = source ? `${source}.` : '';
    const link = url ? ` ${url}` : '';
    return `${auth}. ${year}. ${t} ${src}${link}`.replace(/\s+/g,' ').trim();
  }

  function generate() {
    const payload = {
      author: safe(authorEl.value),
      date: safe(dateEl.value),
      title: safe(titleEl.value),
      source: safe(sourceEl.value),
                     url: safe(urlEl.value)
    };
    const style = styleEl.value;
    let citation = '';
    if (style === 'mla') citation = fmtMLA9(payload);
    else if (style === 'chicago') citation = fmtChicago(payload);
    else citation = fmtAPA(payload);

    outEl.innerHTML = citation;
    return citation;
  }

  function copyToClipboard(text) {
    if (!navigator.clipboard) {
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); } catch (e) {}
      ta.remove();
      alert('Citation copied (fallback).');
      return;
    }
    navigator.clipboard.writeText(text).catch(() => { alert('Copy failed.'); });
  }

  function save() {
    const citation = generate();
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    saved.push({ citation, at: Date.now() });
    localStorage.setItem(KEY, JSON.stringify(saved.slice(-50)));
    alert('Citation saved locally.');
  }

  function loadLast() {
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    if (!saved.length) { alert('No saved citations.'); return; }
    const last = saved[saved.length - 1];
    outEl.innerHTML = last.citation;
  }

  async function tryFetchHtml(url) {
    // Try direct fetch first (may fail due to CORS)
    try {
      const r = await fetch(url, { method: 'GET', mode: 'cors' });
      if (r.ok) return await r.text();
    } catch (err) {
      console.warn('Direct fetch failed (CORS?), will try proxy', err);
    }
    // Fallback to AllOrigins public proxy (rate-limited). Replace with your own proxy for production.
    try {
      const proxy = 'https://api.allorigins.win/raw?url=' + encodeURIComponent(url);
      const r2 = await fetch(proxy);
      if (r2.ok) return await r2.text();
    } catch (err) {
      console.warn('Proxy fetch failed', err);
    }
    return null;
  }

  function parseMetadataFromHtml(html, url) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const getMeta = (name, prop) => {
      const byName = doc.querySelector(`meta[name="${name}"]`);
      if (byName && byName.content) return byName.content;
      const byProp = doc.querySelector(`meta[property="${prop}"]`);
      if (byProp && byProp.content) return byProp.content;
      const byLink = doc.querySelector(`link[rel="canonical"]`);
      if (name === 'url' && byLink && byLink.href) return byLink.href;
      return null;
    };

    const title = getMeta('title','og:title') || doc.querySelector('title')?.textContent || getMeta('twitter:title','twitter:title');
    const site = getMeta('site_name','og:site_name') || (new URL(url)).hostname.replace(/^www\./,'');
    const author = getMeta('author','article:author') || getMeta('author','og:author') || getMeta('byline','byline');
    const published = getMeta('date','article:published_time') || getMeta('publication_date','publication_date') || getMeta('date','og:updated_time') || getMeta('pubdate','pubdate');

    return { title, site, author, published, url };
  }

  // Format published timestamps into user-friendly strings for each citation style.
  function formatPublishedDate(raw) {
    if (!raw) return null;
    // try parse ISO / common date strings
    const ms = Date.parse(raw);
    if (isNaN(ms)) {
      return { apa: raw, mla: raw, chicago: raw };
    }
    const d = new Date(ms);
    // use UTC parts to avoid timezone shifts from ISO Z strings
    const year = d.getUTCFullYear();
    const monthIdx = d.getUTCMonth();
    const day = d.getUTCDate();
    const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const monthName = months[monthIdx];
    return {
      apa: `${year}, ${monthName} ${day}`,      // e.g. "2025, December 4"
      mla: `${day} ${monthName} ${year}`,       // e.g. "4 December 2025"
      chicago: `${year}`                        // Chicago author-date often uses just year for in-text
    };
  }
  
  // try server-side metadata fetch (Flask) — returns { title, author, published, site, url } or throws
  async function fetchMetadataFromServer(targetUrl) {
    const base = (window.fetchProxyBase || '').replace(/\/$/, '');
    if (!base) {
      console.warn('No fetchProxyBase set; skipping server fetch');
      return null;
    }

    try {
      const endpoint = `${base}/fetch_meta?url=${encodeURIComponent(targetUrl)}`;
      console.info('Calling server metadata endpoint:', endpoint);
      const res = await fetch(endpoint, { method: 'GET' });

      // read response body safely (JSON preferred)
      const ct = res.headers.get('content-type') || '';
      const body = ct.includes('application/json') ? await res.json().catch(()=>null) : await res.text().catch(()=>null);

      if (!res.ok) {
        console.warn('Server fetch_meta returned non-OK', res.status, body);
        // show a helpful alert in dev so you know why client fell back
        const detail = body && body.detail ? body.detail : (typeof body === 'string' ? body : JSON.stringify(body));
        alert('Server metadata fetch failed: ' + (detail || res.status));
        return null;
      }

      console.info('Server metadata response', body);
      return body;
    } catch (err) {
      console.warn('Server metadata fetch failed (network)', err);
      alert('Server metadata fetch network error: ' + (err && err.message ? err.message : err));
      return null;
    }
  }

  // try server first, then fallback to client fetch + AllOrigins proxy
  async function fetchAndFill() {
    const url = (urlEl.value || '').trim();
    if (!url) { alert('Enter a URL first.'); return; }
    fetchBtn.textContent = 'Fetching…';
    fetchBtn.disabled = true;
    try {
      // server attempt
      let meta = await fetchMetadataFromServer(url);

      // client fallback
      if (!meta) {
        const html = await tryFetchHtml(url);
        if (!html) {
          alert('Failed to fetch page. CORS or proxy error. Consider enabling your Flask proxy.');
          return;
        }
        meta = parseMetadataFromHtml(html, url);
      }

      if (meta.author) authorEl.value = meta.author;
      if (meta.published) {
        const fmt = formatPublishedDate(meta.published);
        const style = (styleEl && styleEl.value) ? styleEl.value : 'apa';
        dateEl.value = (fmt && fmt[style]) ? fmt[style] : meta.published;
      }
      if (meta.title) titleEl.value = meta.title;
      if (meta.site) sourceEl.value = meta.site;
      urlEl.value = meta.url || url;
      generate();
    } catch (err) {
      console.warn(err);
      alert('Error fetching metadata.');
    } finally {
      fetchBtn.textContent = 'Fetch from URL';
      fetchBtn.disabled = false;
    }
  }

  fetchBtn.addEventListener('click', fetchAndFill);

  // show a default sample on load
  authorEl.value = 'Doe, J.';
  dateEl.value = '2025, May 10';
  titleEl.value = 'Harvard revokes tenure of Francesca Gino after misconduct findings.';
  sourceEl.value = 'The New York Times';
  urlEl.value = 'https://www.nytimes.com/article-link';
  generate();
})();
</script>


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thesis Generator</title>
    <style>
        .thesis-gen-card {
            background: linear-gradient(160deg, #3b3567ff, #33417aff);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 24px;
            margin: 30px 0;
            color: #eaf6ff;
            box-shadow: 0 12px 30px rgba(0,0,0,0.25);
        }

        .thesis-gen-card h3 {
            margin: 0 0 12px 0;
            color: #e4f1ff;
            font-size: 1.5rem;
        }

        .thesis-gen-card p {
            margin: 0 0 16px 0;
            color: #c8d7eb;
            font-size: 0.95rem;
        }

        .thesis-form-group {
            margin-bottom: 16px;
        }

        .thesis-label {
            display: block;
            font-weight: 600;
            margin-bottom: 6px;
            color: #d6e9ff;
            font-size: 0.9rem;
        }

        .thesis-input,
        .thesis-textarea,
        .thesis-select {
            width: 100%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.05);
            color: #eaf6ff;
            font-family: inherit;
            font-size: 0.95rem;
            box-sizing: border-box;
        }

        .thesis-textarea {
            min-height: 80px;
            resize: vertical;
        }

        .thesis-input::placeholder,
        .thesis-textarea::placeholder {
            color: rgba(234, 246, 255, 0.4);
        }

        .thesis-input:focus,
        .thesis-textarea:focus,
        .thesis-select:focus {
            outline: none;
            border-color: #7ad2f9;
            background: rgba(255,255,255,0.08);
        }

        .thesis-points-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .thesis-point-row {
            display: flex;
            gap: 8px;
            align-items: center;
        }

        .thesis-point-row input {
            flex: 1;
        }

        .thesis-btn-remove {
            padding: 8px 12px;
            background: rgba(248, 113, 113, 0.2);
            border: 1px solid rgba(248, 113, 113, 0.3);
            color: #fca5a5;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s;
        }

        .thesis-btn-remove:hover {
            background: rgba(248, 113, 113, 0.3);
        }

        .thesis-btn-add {
            margin-top: 8px;
            padding: 8px 14px;
            background: rgba(155, 231, 196, 0.15);
            border: 1px solid rgba(155, 231, 196, 0.3);
            color: #9be7c4;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s;
        }

        .thesis-btn-add:hover {
            background: rgba(155, 231, 196, 0.25);
        }

        .thesis-actions {
            display: flex;
            gap: 10px;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        .thesis-btn {
            flex: 1;
            min-width: 140px;
            padding: 12px 16px;
            border: none;
            border-radius: 10px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 0.95rem;
        }

        .thesis-btn-primary {
            background: #7ad2f9;
            color: #0e2038;
        }

        .thesis-btn-secondary {
            background: rgba(255,255,255,0.1);
            color: #d6e6ff;
            border: 1px solid rgba(255,255,255,0.15);
        }

        .thesis-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }

        .thesis-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        .thesis-status {
            margin-top: 12px;
            padding: 10px;
            border-radius: 8px;
            font-weight: 600;
            display: none;
        }

        .thesis-status.success {
            background: rgba(155, 231, 196, 0.15);
            border: 1px solid rgba(155, 231, 196, 0.3);
            color: #9be7c4;
        }

        .thesis-status.error {
            background: rgba(248, 113, 113, 0.15);
            border: 1px solid rgba(248, 113, 113, 0.3);
            color: #fca5a5;
        }

        .thesis-status.info {
            background: rgba(122, 210, 249, 0.15);
            border: 1px solid rgba(122, 210, 249, 0.3);
            color: #7ad2f9;
        }

        .thesis-output-section {
            margin-top: 24px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }

        .thesis-output-section h4 {
            color: #e4f1ff;
            margin-bottom: 16px;
            font-size: 1.2rem;
        }

        .thesis-card {
            background: rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 16px;
            margin-bottom: 16px;
        }

        .thesis-statement {
            font-size: 1.05rem;
            font-weight: 600;
            color: #e4f1ff;
            margin-bottom: 12px;
            line-height: 1.5;
        }

        .thesis-strength-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .thesis-strength-high {
            background: rgba(155, 231, 196, 0.3);
            color: #9be7c4;
            border: 1px solid rgba(155, 231, 196, 0.4);
        }

        .thesis-strength-medium {
            background: rgba(251, 191, 36, 0.3);
            color: #fbbf24;
            border: 1px solid rgba(251, 191, 36, 0.4);
        }

        .thesis-strength-low {
            background: rgba(248, 113, 113, 0.3);
            color: #fca5a5;
            border: 1px solid rgba(248, 113, 113, 0.4);
        }

        .thesis-details {
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid rgba(255,255,255,0.08);
        }

        .thesis-details h5 {
            color: #7ad2f9;
            margin-bottom: 8px;
            font-size: 0.9rem;
        }

        .thesis-details ul {
            list-style-position: inside;
            color: #c8d7eb;
            font-size: 0.9rem;
            margin: 0;
            padding-left: 8px;
        }

        .thesis-details li {
            margin-bottom: 6px;
        }

        .thesis-btn-use {
            margin-top: 12px;
            padding: 8px 14px;
            background: rgba(122, 210, 249, 0.2);
            border: 1px solid rgba(122, 210, 249, 0.3);
            color: #7ad2f9;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s;
        }

        .thesis-btn-use:hover {
            background: rgba(122, 210, 249, 0.3);
        }

        .thesis-loading {
            text-align: center;
            padding: 30px;
        }

        .thesis-spinner {
            border: 3px solid rgba(255,255,255,0.1);
            border-top: 3px solid #7ad2f9;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: thesis-spin 1s linear infinite;
            margin: 0 auto 16px;
        }

        @keyframes thesis-spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .thesis-recommendations {
            background: rgba(251, 191, 36, 0.15);
            border-left: 3px solid #fbbf24;
            padding: 14px;
            margin-top: 16px;
            border-radius: 8px;
        }

        .thesis-recommendations h5 {
            color: #fbbf24;
            margin: 0 0 8px 0;
            font-size: 0.95rem;
        }

        .thesis-recommendations p {
            color: #e6f0ff;
            margin: 0;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="thesis-gen-card">
        <h3>✍️ AI Thesis Generator</h3>
        <p>Transform your ideas into powerful thesis statements using AI</p>

        <div class="thesis-form-group">
            <label class="thesis-label" for="thesis-topic">Topic *</label>
            <input type="text" id="thesis-topic" class="thesis-input" placeholder="e.g., Social Media Impact on Society" required>
        </div>

        <div class="thesis-form-group">
            <label class="thesis-label" for="thesis-position">Your Position/Argument *</label>
            <textarea id="thesis-position" class="thesis-textarea" placeholder="e.g., Social media has negative effects on mental health" required></textarea>
        </div>

        <div class="thesis-form-group">
            <label class="thesis-label">Supporting Points (Optional)</label>
            <div class="thesis-points-container" id="thesis-points-container">
                <div class="thesis-point-row">
                    <input type="text" class="thesis-input thesis-supporting-point" placeholder="Supporting point 1">
                </div>
            </div>
            <button class="thesis-btn-add" id="thesis-add-point">+ Add Point</button>
        </div>

        <div class="thesis-form-group">
            <label class="thesis-label" for="thesis-type">Thesis Type</label>
            <select id="thesis-type" class="thesis-select">
                <option value="Argumentative">Argumentative</option>
                <option value="Analytical">Analytical</option>
                <option value="Expository">Expository</option>
                <option value="Compare/Contrast">Compare/Contrast</option>
                <option value="Cause/Effect">Cause/Effect</option>
            </select>
        </div>

        <div class="thesis-form-group">
            <label class="thesis-label" for="thesis-audience">Target Audience (Optional)</label>
            <input type="text" id="thesis-audience" class="thesis-input" placeholder="e.g., General academic">
        </div>

        <div class="thesis-actions">
            <button class="thesis-btn thesis-btn-primary" id="thesis-generate">✨ Generate Thesis</button>
            <button class="thesis-btn thesis-btn-secondary" id="thesis-clear">🔄 Clear Form</button>
        </div>

        <div id="thesis-status" class="thesis-status"></div>

        <div class="thesis-output-section" id="thesis-output-section" style="display: none;">
            <h4>Generated Thesis Statements</h4>
            <div id="thesis-output"></div>
            <div id="thesis-recommendations"></div>
        </div>
    </div>

    <script>
        const API_URL = 'https://api.anthropic.com/v1/messages';

        function addThesisPoint() {
            const container = document.getElementById('thesis-points-container');
            const pointDiv = document.createElement('div');
            pointDiv.className = 'thesis-point-row';
            pointDiv.innerHTML = `
                <input type="text" class="thesis-input thesis-supporting-point" placeholder="Supporting point ${container.children.length + 1}">
                <button class="thesis-btn-remove" onclick="removeThesisPoint(this)">×</button>
            `;
            container.appendChild(pointDiv);
        }

        window.removeThesisPoint = function(btn) {
            btn.parentElement.remove();
        };

        function showThesisStatus(message, type) {
            const statusDiv = document.getElementById('thesis-status');
            statusDiv.textContent = message;
            statusDiv.className = `thesis-status ${type}`;
            statusDiv.style.display = 'block';
            
            if (type !== 'info') {
                setTimeout(() => statusDiv.style.display = 'none', 5000);
            }
        }

        async function generateThesis() {
            const topic = document.getElementById('thesis-topic').value.trim();
            const position = document.getElementById('thesis-position').value.trim();
            
            if (!topic || !position) {
                showThesisStatus('Please fill in both Topic and Position fields', 'error');
                return;
            }

            const pointInputs = document.querySelectorAll('.thesis-supporting-point');
            const supportingPoints = Array.from(pointInputs)
                .map(input => input.value.trim())
                .filter(point => point.length > 0);

            const thesisType = document.getElementById('thesis-type').value;
            const audience = document.getElementById('thesis-audience').value.trim();

            const outputSection = document.getElementById('thesis-output-section');
            const thesisOutput = document.getElementById('thesis-output');
            outputSection.style.display = 'block';
            thesisOutput.innerHTML = '<div class="thesis-loading"><div class="thesis-spinner"></div><p>Generating your thesis statements...</p></div>';

            try {
                const prompt = `Generate 3 high-quality thesis statements for an essay with the following details:

Topic: ${topic}
Position/Argument: ${position}
${supportingPoints.length > 0 ? `Supporting Points: ${supportingPoints.join(', ')}` : ''}
Thesis Type: ${thesisType}
${audience ? `Target Audience: ${audience}` : ''}

For each thesis statement, provide:
1. The thesis statement itself
2. A strength rating (1-10)
3. A brief explanation of why it's strong or weak
4. 2-3 supporting arguments that could be used
5. 2-3 potential counterarguments to address

Also provide overall recommendations for improving the thesis.

Format your response as a JSON object with this structure:
{
  "theses": [
    {
      "statement": "...",
      "strength": 8,
      "strengthExplanation": "...",
      "supportingArguments": ["...", "...", "..."],
      "counterarguments": ["...", "...", "..."]
    }
  ],
  "recommendations": "..."
}`;

                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        model: 'claude-sonnet-4-20250514',
                        max_tokens: 1000,
                        messages: [
                            {
                                role: 'user',
                                content: prompt
                            }
                        ]
                    })
                });

                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }

                const data = await response.json();
                const content = data.content.find(item => item.type === 'text')?.text;
                
                if (!content) {
                    throw new Error('No response content received');
                }

                // Parse JSON from response
                const jsonMatch = content.match(/\{[\s\S]*\}/);
                if (!jsonMatch) {
                    throw new Error('Could not parse JSON response');
                }

                const result = JSON.parse(jsonMatch[0]);
                displayTheses(result);
                showThesisStatus('✅ Thesis statements generated successfully!', 'success');
            } catch (error) {
                console.error('Error:', error);
                thesisOutput.innerHTML = '';
                outputSection.style.display = 'none';
                showThesisStatus('❌ Error: ' + error.message, 'error');
            }
        }

        function displayTheses(data) {
            const thesisOutput = document.getElementById('thesis-output');
            const recommendationsOutput = document.getElementById('thesis-recommendations');
            
            thesisOutput.innerHTML = '';

            if (!data.theses || data.theses.length === 0) {
                thesisOutput.innerHTML = '<p>No theses generated. Please try again.</p>';
                return;
            }

            data.theses.forEach((thesis) => {
                const strengthClass = thesis.strength >= 8 ? 'thesis-strength-high' : 
                                     thesis.strength >= 6 ? 'thesis-strength-medium' : 'thesis-strength-low';
                
                const card = document.createElement('div');
                card.className = 'thesis-card';
                card.innerHTML = `
                    <div class="thesis-statement">${thesis.statement}</div>
                    <span class="thesis-strength-badge ${strengthClass}">Strength: ${thesis.strength}/10</span>
                    <p style="color: #c8d7eb; margin-top: 10px; font-size: 0.9rem;">${thesis.strengthExplanation}</p>
                    
                    ${thesis.supportingArguments && thesis.supportingArguments.length > 0 ? `
                        <div class="thesis-details">
                            <h5>📚 Supporting Arguments</h5>
                            <ul>
                                ${thesis.supportingArguments.map(arg => `<li>${arg}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                    
                    ${thesis.counterarguments && thesis.counterarguments.length > 0 ? `
                        <div class="thesis-details">
                            <h5>⚖️ Counterarguments to Address</h5>
                            <ul>
                                ${thesis.counterarguments.map(counter => `<li>${counter}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                    
                    <button class="thesis-btn-use" onclick="useThesis(\`${thesis.statement.replace(/`/g, '\\`')}\`)">
                        Use This Thesis
                    </button>
                `;
                
                thesisOutput.appendChild(card);
            });

            if (data.recommendations) {
                recommendationsOutput.innerHTML = `
                    <div class="thesis-recommendations">
                        <h5>💡 Recommendations</h5>
                        <p>${data.recommendations}</p>
                    </div>
                `;
            }
        }

        window.useThesis = function(statement) {
            navigator.clipboard.writeText(statement).then(() => {
                showThesisStatus('📋 Thesis copied to clipboard!', 'success');
            }).catch(() => {
                showThesisStatus('⚠️ Please manually copy the thesis', 'error');
            });
        };

        function clearThesisForm() {
            document.getElementById('thesis-topic').value = '';
            document.getElementById('thesis-position').value = '';
            document.getElementById('thesis-audience').value = '';
            document.getElementById('thesis-type').value = 'Argumentative';
            
            const pointsContainer = document.getElementById('thesis-points-container');
            pointsContainer.innerHTML = `
                <div class="thesis-point-row">
                    <input type="text" class="thesis-input thesis-supporting-point" placeholder="Supporting point 1">
                </div>
            `;
            
            document.getElementById('thesis-output-section').style.display = 'none';
            showThesisStatus('Form cleared', 'info');
        }

        // Event listeners
        document.getElementById('thesis-add-point').addEventListener('click', addThesisPoint);
        document.getElementById('thesis-generate').addEventListener('click', generateThesis);
        document.getElementById('thesis-clear').addEventListener('click', clearThesisForm);
    </script>
</body>
</html>