<style>
                .media-spectrum-intro {
                    margin-bottom: 30px;
                }
                
                .spectrum-bar {
                    height: 12px;
                    background: linear-gradient(to right, #3b82f6, #94a3b8, #ef4444);
                    border-radius: 10px;
                    margin: 20px 0;
                }
            </style>

        <div id="bias-info-box" style="background: rgba(15, 23, 42, 0.8); border: 2px solid #94a3b8; border-radius: 16px; padding: 30px; min-height: 200px; transition: all 0.3s;">

            <div class="media-spectrum-intro">
                <h3 style="color: #60a5fa; font-size: 1.8rem; margin-bottom: 20px; text-align: center;">The Media Spectrum Explorer</h3>
                <p style="color: #cbd5e1; margin-bottom: 20px; line-height: 1.6; text-align: center;">
                    Media bias is how stories get framed. Drag the slider to explore different perspectives!
                </p>

                <div style="position: relative; padding: 40px 20px;">
                    <div class="spectrum-bar"></div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                        <span style="color: #3b82f6; font-weight: 700; font-size: 0.9rem;">LEFT</span>
                        <span style="color: #94a3b8; font-weight: 700; font-size: 0.9rem;">CENTER</span>
                        <span style="color: #ef4444; font-weight: 700; font-size: 0.9rem;">RIGHT</span>
                    </div>
                    
                    <div style="position: relative; margin: 30px 0;">
                        <input type="range" min="0" max="100" value="50" 
                               id="bias-slider" 
                               style="width: 100%; height: 8px; border-radius: 5px; background: rgba(148, 163, 184, 0.3); outline: none; cursor: pointer;">
                    </div>
                        <div style="text-align: center;">
                            <div style="font-size: 4rem; margin-bottom: 15px;" id="bias-emoji">𓍝</div>
                            <h4 style="color: #94a3b8; font-size: 1.5rem; margin-bottom: 15px;" id="bias-title">Center/Neutral</h4>
                            <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.8;" id="bias-description">
                                Focuses on factual reporting with minimal editorial opinion, presenting multiple viewpoints.
                            </p>
                            <div style="margin-top: 20px; padding: 15px; background: rgba(148, 163, 184, 0.1); border-radius: 10px;">
                                <p style="color: #60a5fa; font-weight: 700; margin-bottom: 8px;" id="bias-key">Key Characteristics:</p>
                                <p style="color: #e2e8f0; font-size: 0.9rem;" id="bias-traits">
                                    ✓ Fact-based headlines<br>
                                    ✓ Multiple perspectives<br>
                                    ✓ Minimal opinion language
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="background: rgba(168, 85, 247, 0.1); border: 1px solid rgba(168, 85, 247, 0.3); padding: 20px; border-radius: 12px; margin-top: 25px;">
                    <h4 style="color: #a78bfa; margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 1.5rem;"></span> Pro Tip
                    </h4>
                    <p style="color: #e2e8f0; line-height: 1.6;">
                        <strong>No source is 100% unbiased.</strong> Don't strive for perfection. Just consider the value each source brings. Smart readers consume multiple viewpoints to have a well rounded opinon.
                    </p>
                </div>
            </div>

            <script>
                (function() {
                    const biasSlider = document.getElementById('bias-slider');
                    const biasData = {
                        0: {
                            emoji: '︎⚠︎',
                            title: 'Far Left',
                            color: '#1e40af',
                            description: 'Strong progressive advocacy. Often focuses on social justice, wealth inequality, and systemic change. May use passionate language to drive urgency.',
                            traits: '✓ Advocacy journalism<br>✓ Social justice focus<br>✓ Bold reform proposals'
                        },
                        25: {
                            emoji: '🗣',
                            title: 'Left-Leaning',
                            color: '#3b82f6',
                            description: 'Generally supports progressive policies like environmental regulation, social programs, and diversity initiatives. Frames stories with these values in mind.',
                            traits: '✓ Progressive values<br>✓ Government solutions<br>✓ Social equity emphasis'
                        },
                        50: {
                            emoji: '𓍝',
                            title: 'Center/Neutral',
                            color: '#94a3b8',
                            description: 'Focuses on factual reporting with minimal editorial opinion, presenting multiple viewpoints. Prioritizes verifiable information over interpretation.',
                            traits: '✓ Fact-based headlines<br>✓ Multiple perspectives<br>✓ Minimal opinion language'
                        },
                        75: {
                            emoji: '🎤︎',
                            title: 'Right-Leaning',
                            color: '#ef4444',
                            description: 'Generally supports conservative values like free markets, limited government, and traditional institutions. Stories emphasize these principles.',
                            traits: '✓ Conservative values<br>✓ Market solutions<br>✓ Traditional institutions'
                        },
                        100: {
                            emoji: '⚠︎',
                            title: 'Far Right',
                            color: '#a01414',
                            description: 'Strong conservative advocacy. Often focuses on individual liberty, national sovereignty, and traditional values. May use passionate language about cultural issues.',
                            traits: '✓ Advocacy journalism<br>✓ Nationalist focus<br>✓ Traditional values defense'
                        }
                    };

                    if (biasSlider) {
                        biasSlider.addEventListener('input', function() {
                            const value = parseInt(this.value, 10);
                            let closestKey = 50;
                            let minDiff = Math.abs(value - 50);
                            
                            Object.keys(biasData).forEach(key => {
                                const diff = Math.abs(value - parseInt(key, 10));
                                if (diff < minDiff) {
                                    minDiff = diff;
                                    closestKey = key;
                                }
                            });
                            
                            const data = biasData[closestKey];
                            const infoBox = document.getElementById('bias-info-box');
                            
                            document.getElementById('bias-emoji').textContent = data.emoji;
                            document.getElementById('bias-title').textContent = data.title;
                            document.getElementById('bias-title').style.color = data.color;
                            document.getElementById('bias-description').textContent = data.description;
                            document.getElementById('bias-traits').innerHTML = data.traits;
                            infoBox.style.borderColor = data.color;
                        });
                    }
                })();
            </script>

            <div class="content-placeholder">
                <p>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  min-height: 100vh;
  background-size: cover;
  background-color: #9393c7;
  padding: 20px;
}

/* Center everything */
.page-content {
  max-width: 1800px;
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
    background: #a7a0d4;
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
    background: rgb(255 255 255 / 29%);
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
  color: #b2c7deff
}

.leaderboard-table tr:nth-child(even) {
  background: rgba(29, 31, 75, 1);
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

<!-- REPLACE YOUR ENTIRE SCRIPT SECTION WITH THIS -->
<script type="module">
import {pythonURI,fetchOptions} from '{{site.baseurl}}/assets/js/api/config.js';
window.pythonURI = pythonURI;

// Authentication Manager Class
// Fixed Authentication Manager with proper CORS and GitHub validation

async function getCurrentUser() {
    try {
        const response = await fetch(`${pythonURI}/api/id`, {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (response.ok) {
            const userData = await response.json();
            return userData; // Returns {uid, name, role, etc.}
        }
    } catch (error) {
        console.log('No authenticated user:', error);
    }
    return null; // Guest user
}

// Update the auth button display
async function updateAuthButton() {
    const authBtn = document.getElementById('auth-btn');
    const playerDisplay = document.getElementById('player-name');
    
    if (!authBtn || !playerDisplay) return;
    
    const user = await getCurrentUser();
    
    if (user && user.uid) {
        // Logged in user
        authBtn.textContent = 'Sign Out';
        authBtn.onclick = () => {
            window.location.href = '{{site.baseurl}}/logout';
        };
        playerDisplay.textContent = `Player: ${user.uid}`;
        window.currentPlayerUid = user.uid;
        window.currentPlayerName = user.name;
    } else {
        // Guest user
        authBtn.textContent = 'Sign In';
        authBtn.onclick = () => {
            window.location.href = '{{site.baseurl}}/login';
        };
        playerDisplay.textContent = 'Player: Guest';
        window.currentPlayerUid = 'Guest';
        window.currentPlayerName = 'Guest';
    }
}

// Initialize on load
window.addEventListener('DOMContentLoaded', () => {
    updateAuthButton();
});

// Make updateAuthButton available globally
window.updateAuthButton = updateAuthButton;
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

    // Game state
    let currentPlayer = "Guest";
    let placedImages = new Set();
    let timerHandle = null;
    let gameStarted = false;

    const playerDisplay = document.getElementById('player-name');
    const timerDisplay = document.getElementById('timer');
    const bins = document.querySelectorAll('.bin');
    const imagesArea = document.getElementById('images');

    // TIMER UTILITIES
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
    // Use the globally set currentPlayerUid from updateAuthButton
    if (window.currentPlayerUid) {
        currentPlayer = window.currentPlayerUid;
    } else {
        currentPlayer = 'Guest';
    }
    
    updateDisplays();
}

async function postScore(username, finalTime) {
    try {
        const response = await fetch(`${pythonURI}/api/media/score/${encodeURIComponent(username)}/${finalTime}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            credentials: "include"
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
        const response = await fetch(pythonURI + '/api/media/leaderboard?limit=5');
        if (!response.ok) throw new Error('Failed to fetch leaderboard');
        const data = await response.json();
        
        tbody.innerHTML = '';
        data.forEach((entry, index) => {
            const row = tbody.insertRow();
            row.insertCell().textContent = entry.rank || (index + 1);
            row.insertCell().textContent = entry.username || 'Unknown';
            // Use 'time' instead of 'score' and format it
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
            headers: {'Content-Type': 'application/json'},
            credentials: "include"
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
        console.log("DOM fully loaded — initializing game & buttons");

        initGame();
        console.log("Game initialized automatically");

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

        const submitBtn = document.getElementById('submit-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                console.log("Submit clicked");

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
        console.log("Window fully loaded — starting game");
        fetchUser();
        initGame();
        fetchLeaderboard();
        setInterval(fetchLeaderboard, 30000);
    };
</script>

------------------------------------------------

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