---
layout: post
title: "Bias Detector"
description: "Second line of defense from foregin invaders"
permalink: /digital-famine/media-lit/submodule_2/
footer:
  previous: /digital-famine/media-lit/submodule_1
  home: /digital-famine/media-lit
  next: /digital-famine/media-lit/submodule_3
parent: "Analytics/Admin"
team: "Scratchers"
submodule: 2
categories: [CSP, Submodule, Analytics/Admin]
tags: [analytics, submodule, curators]
breadcrumb: true
microblog: true
author: "Anwita Bandaru and Nick Diaz"
date: 2025-10-21
---
# Bias Detector

<div class="intro-text">
  <h3>Why is checking for bias Important?</h3>
  <p>
    The alien misinformation swarm doesn’t invade with lasers or ships — it attacks minds.<br>
    Every distorted headline, every emotional post, every half-true story is a signal designed to scramble human judgment. Once people can’t tell what’s real, they stop trusting reliable information. Biased language can make ordinary events sound urgent or frightening, pushing people to react before they think. When that happens, truth fades and manipulation spreads.
  </p>
  <hr>
  <p><strong>By identifying bias, you decode the signal. You learn to notice when words are chosen to provoke rather than inform.</strong></p>

  <h2>Media Bias Training</h2>
  <p>
    Before you receive your mission to protect Media Literacy Planet, you'll need to undergo training. Test your knowledge of media bias by sorting news outlets into their typical editorial positions. This training will help you understand the different biases present in major news sources to defeat the invaders.
  </p>
  <p><strong>Begin by pressing reset to load the images</strong></p>
</div>

<style>
body {
  min-height: 100vh;
  background: url('{{ site.baseurl }}/hacks/digital-famine/media-lit/media/assets/spacebackground.jpg') no-repeat center center fixed;
  background-size: cover;
  background-color: #061226; /* fallback */
}
 .intro-text {
  background: rgba(0,0,30,0.85);
  padding: 20px;
  border-radius: 12px;
  font-family: "Inter", system-ui, sans-serif;
  font-size: 1.05rem;
  margin-bottom: 20px;
  line-height: 1.5;
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
  background: linear-gradient(160deg, #1e2a38, #2f3f4f);
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

<!-- 🛰 Source Intel Chatbox -->
<div class="ai-card" id="source-intel-chat">
  <h3>AI Source Intel Chat</h3>
  <p>Ask about a news source to get neutral background info, or request a hint without revealing bias placement.</p>

  <label for="source-query">Type a source or question:</label>
  <textarea id="source-query" placeholder="e.g., Tell me about The Epoch Times, or 'Hint about Reuters'"></textarea>

  <div class="ai-controls">
    <button class="ai-btn primary" id="lookup-btn">🔍 Source Lookup</button>
    <button class="ai-btn secondary" id="hint-btn">💡 Smart Hint</button>
    <button class="ai-btn ghost" id="save-chat-btn">💾 Save Session</button>
    <button class="ai-btn ghost" id="load-chat-btn">📂 Load Saved</button>
    <button class="ai-btn ghost" id="clear-chat-btn">🧹 Clear Chat</button>
  </div>

  <div id="ai-chat-status" class="ai-status"></div>

  <div class="ai-chat-log" id="source-chat-log">
    <div class="chat-hint">Try: "What should I know about Reuters?" or "Give me a hint about Fox News."</div>
  </div>
</div>

<script>
(function() {
  const statusBox = document.getElementById('ai-chat-status');
  const queryInput = document.getElementById('source-query');
  const chatLog = document.getElementById('source-chat-log');
  let lastMatchedSource = null;

  const SOURCE_PROFILES = [
    {
      name: "The Epoch Times",
      aliases: ["epoch times", "the epoch"],
      ownership: "Epoch Media Group",
      founded: "2000 by John Tang",
      audience: "Global audience with focus on U.S. and China politics",
      description: "International newspaper with investigative coverage and roots in Falun Gong-affiliated ownership.",
      notes: "Often blends straight reporting with analysis pieces; check sourcing when stories go viral.",
      hints: [
        "Check ownership ties and how coverage of China is framed compared with other outlets.",
        "Scan whether opinion and hard news are clearly separated in the piece you saw."
      ]
    },
    {
      name: "Reuters",
      aliases: ["thomson reuters"],
      ownership: "Thomson Reuters (public company)",
      founded: "1851 by Paul Julius Reuter",
      audience: "Global wire service feeding newsrooms and financial terminals",
      description: "Wire service known for speed and fact-centered copy supplied to other outlets.",
      notes: "Focuses on straight news; opinion content is uncommon and usually labeled.",
      hints: [
        "Consider their revenue model (terminals and licensing) and how that affects incentives.",
        "Look at datelines and sourcing—they emphasize multiple independent confirmations."
      ]
    },
    {
      name: "Fox News",
      aliases: ["fox"],
      ownership: "Fox Corporation",
      founded: "1996 by Rupert Murdoch and Roger Ailes",
      audience: "Large U.S. cable audience; mix of news programming and opinion shows",
      description: "Cable channel combining straight news segments with high-profile opinion primetime shows.",
      notes: "Distinguish between newsroom reporting and commentary—tone shifts by program.",
      hints: [
        "Check whether the segment was from daytime news or primetime opinion.",
        "Notice guest selection and how panels frame contested topics."
      ]
    },
    {
      name: "NPR",
      aliases: ["national public radio"],
      ownership: "Nonprofit; member station network",
      founded: "1970",
      audience: "U.S. public radio listeners and digital readers",
      description: "Public media network producing radio, podcasts, and digital news with focus on explanatory reporting.",
      notes: "Member stations contribute reporting; funding combines donations, underwriting, and grants.",
      hints: [
        "Check whether the piece is straight news or an explanatory feature with analysis.",
        "Look at how sources are balanced between officials, experts, and affected communities."
      ]
    },
    {
      name: "The New York Times",
      aliases: ["ny times", "nyt", "the times"],
      ownership: "The New York Times Company (public, Sulzberger family control)",
      founded: "1851 by Henry Jarvis Raymond and George Jones",
      audience: "Global digital subscribers and U.S. print readers",
      description: "Legacy newspaper with extensive national and international bureaus and large opinion section.",
      notes: "News and opinion are separate desks; look for the Opinion label on columns.",
      hints: [
        "Check whether you’re reading News, Opinion, or Guest Essay—labels matter.",
        "Consider how sourcing spans officials, experts, and impacted individuals."
      ]
    }
  ];

  function setStatus(message, type = "info") {
    statusBox.textContent = message;
    statusBox.style.display = "block";
    const colors = {
      info: { bg: "rgba(122,210,249,0.14)", color: "#b4e4ff" },
      success: { bg: "rgba(155,231,196,0.14)", color: "#b6f3d8" },
      error: { bg: "rgba(255,204,204,0.18)", color: "#ffd6d6" }
    };
    const palette = colors[type] || colors.info;
    statusBox.style.backgroundColor = palette.bg;
    statusBox.style.color = palette.color;
    if (type !== "info") {
      setTimeout(() => { statusBox.style.display = "none"; }, 4000);
    }
  }

  function addMessage(role, text, allowHTML = false) {
    const bubble = document.createElement('div');
    bubble.className = `chat-bubble ${role}`;
    if (allowHTML) {
      bubble.innerHTML = text;
    } else {
      bubble.textContent = text;
    }
    chatLog.appendChild(bubble);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  function findSource(query) {
    const q = query.toLowerCase();
    return SOURCE_PROFILES.find(src =>
      [src.name, ...(src.aliases || [])].some(n => n.toLowerCase().includes(q))
    );
  }

  function formatSourceResponse(src) {
    return `
      <strong>${src.name}</strong><br>
      Ownership: ${src.ownership}<br>
      Founded: ${src.founded}<br>
      Audience: ${src.audience}<br>
      Summary: ${src.description}<br>
      Note: ${src.notes}
    `;
  }

  function handleLookup() {
    const query = queryInput.value.trim();
    if (!query) {
      setStatus("⚠️ Enter a source name first.", "error");
      return;
    }
    addMessage("user", `You: ${query}`);
    setStatus("Looking up source...", "info");
    const match = findSource(query);
    if (match) {
      lastMatchedSource = match;
      addMessage("ai", formatSourceResponse(match), true);
      setStatus("✅ Source info shared.", "success");
    } else {
      addMessage("ai", "I could not find that source in the quick reference. Try a different spelling or ask for a general hint.");
      setStatus("No direct match found.", "error");
    }
  }

  function handleHint() {
    const query = queryInput.value.trim();
    const match = query ? findSource(query) : lastMatchedSource;
    if (match) {
      lastMatchedSource = match;
      const hint = match.hints[Math.floor(Math.random() * match.hints.length)];
      addMessage("ai", `Hint about ${match.name}: ${hint}`);
      setStatus("🎯 Hint delivered.", "success");
    } else {
      addMessage("ai", "Think about ownership, funding, and how clearly news is separated from opinion. Try entering a source name for a tailored hint.");
      setStatus("Shared a general hint.", "info");
    }
  }

  function saveChat() {
    const payload = {
      html: chatLog.innerHTML,
      last: lastMatchedSource ? lastMatchedSource.name : null
    };
    localStorage.setItem("source-intel-chat", JSON.stringify(payload));
    setStatus("💾 Session saved locally.", "success");
  }

  function loadChat() {
    const saved = localStorage.getItem("source-intel-chat");
    if (!saved) {
      setStatus("⚠️ No saved session found.", "error");
      return;
    }
    const data = JSON.parse(saved);
    chatLog.innerHTML = data.html || "";
    lastMatchedSource = SOURCE_PROFILES.find(s => s.name === data.last) || null;
    setStatus("📂 Session loaded.", "success");
  }

  function clearChat() {
    chatLog.innerHTML = '<div class="chat-hint">Try: "What should I know about Reuters?" or "Give me a hint about Fox News."</div>';
    lastMatchedSource = null;
    setStatus("Chat cleared.", "info");
  }

  document.getElementById('lookup-btn').addEventListener('click', handleLookup);
  document.getElementById('hint-btn').addEventListener('click', handleHint);
  document.getElementById('save-chat-btn').addEventListener('click', saveChat);
  document.getElementById('load-chat-btn').addEventListener('click', loadChat);
  document.getElementById('clear-chat-btn').addEventListener('click', clearChat);
})();
</script>

<!-- REPLACE YOUR ENTIRE SCRIPT SECTION WITH THIS -->
<script type="module">
    console.log("✅ Game script loaded");
    import { javaURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';
    
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

    function createImageCard(file, index) {
        const img = document.createElement('img');
        img.src = IMAGE_BASE + file.src;
        img.alt = file.company;
        img.className = 'image';
        img.draggable = true;
        img.dataset.bin = file.bin;
        img.dataset.company = file.company;
        img.dataset.id = `img-${index}`;

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

        const selectedImages = [
            ...getRandomSubset(leftImages, 7),
            ...getRandomSubset(centerImages, 7),
            ...getRandomSubset(rightImages, 7)
        ].sort(() => 0.5 - Math.random());

        selectedImages.forEach((file, index) => {
            const card = createImageCard(file, index);
            imagesArea.appendChild(card);
        });
    }

    // Autofill helper
    function autofillImageGame(showAlert = false) {
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');
        const imgs = Array.from(document.querySelectorAll('img.image'));
        let correctCount = 0;
        imgs.forEach(img => {
            const target = img.dataset.bin;
            const id = img.dataset.id;
            const bin = Array.from(document.querySelectorAll('.bin')).find(b => b.dataset.bin === target);
            if (bin) {
                bin.querySelector('.bin-content').appendChild(img);
                img.style.opacity = '1';
                img.style.cursor = 'grab';
                placedImages.add(id);
                correctCount++;
            }
        });
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
            
            updateDisplays();
        });
    });

    async function fetchUser() {
        try {
            const response = await fetch(javaURI + '/api/person/get', fetchOptions);
            if (response.ok) {
                const data = await response.json();
                currentPlayer = data.name || data.username || 'Guest';
            }
        } catch (err) {
            console.warn('Failed to fetch user:', err);
        }
        updateDisplays();
    }

    // CHANGED: Now submits time instead of score
    async function submitFinalTime(username, seconds) {
        try {
            const response = await fetch(`${javaURI}/api/media/score/${encodeURIComponent(username)}/${seconds}`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'}
            });
            if (!response.ok) throw new Error('Failed to save time');
            console.log(`✅ Time submitted: ${seconds}s`);
            fetchLeaderboard();
        } catch (err) {
            console.error('Error saving time:', err);
        }
    }

    // CHANGED: Displays times in MM:SS format
    async function fetchLeaderboard() {
        const tbody = document.getElementById('leaderboard-body');
        try {
            const response = await fetch(javaURI + '/api/media/leaderboard');
            if (!response.ok) throw new Error('Failed to fetch leaderboard');
            const data = await response.json();
            
            tbody.innerHTML = '';
            data.forEach((entry, index) => {
                const row = tbody.insertRow();
                row.insertCell().textContent = entry.rank || (index + 1);
                row.insertCell().textContent = entry.username || 'Unknown';
                
                // Format time as MM:SS
                const time = entry.time || 0;
                const minutes = Math.floor(time / 60);
                const seconds = time % 60;
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

    window.addEventListener('DOMContentLoaded', () => {
        console.log("🚀 DOM fully loaded — initializing game & buttons");

        initGame();
        console.log("✅ Game initialized automatically");

        const resetBtn = document.getElementById('reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                console.log("🔁 Reset clicked");
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
