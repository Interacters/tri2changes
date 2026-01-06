---
permalink: /english_help/
author: Interactors
date: 2025-12-12
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English Essay Help - Media Literacy Module</title>
    <style>
  * {
    max-width: none !important;
  }
  
  .container {
    max-width: 900px !important;
    padding: 40px;
  }
</style>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            background: linear-gradient(135deg, #1e3a8a 0%, #312e81 50%, #1e293b 100%);
            font-family: 'Inter', system-ui, sans-serif;
            color: #e2e8f0;
            padding: 20px;
        }

        .container {
            max-width: 100%;
            margin: 0 auto;
            background: #31285cbc 
        }

        /* Progress Tracker */
        .progress-tracker {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 30px;
            border: 1px solid rgba(148, 163, 184, 0.1);
        }

        .progress-header {
            text-align: center;
            margin-bottom: 30px;
        }

        .progress-header h1 {
            font-size: 2rem;
            background: linear-gradient(90deg, #60a5fa, #a78bfa, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }

        .progress-subtitle {
            color: #94a3b8;
            font-size: 1rem;
        }

        .progress-steps {
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            margin-bottom: 20px;
        }

        .progress-line {
            position: absolute;
            top: 20px;
            left: 0;
            right: 0;
            height: 4px;
            background: rgba(148, 163, 184, 0.2);
            z-index: 0;
        }

        .progress-line-fill {
            height: 100%;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            transition: width 0.5s ease;
            border-radius: 2px;
        }

        .step {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            z-index: 1;
            flex: 1;
        }

        .step-circle {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: rgba(15, 23, 42, 0.9);
            border: 3px solid rgba(148, 163, 184, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1rem;
            transition: all 0.3s ease;
            margin-bottom: 12px;
        }

        .step.active .step-circle {
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            border-color: #60a5fa;
            box-shadow: 0 0 20px rgba(96, 165, 250, 0.5);
            transform: scale(1.1);
        }

        .step.completed .step-circle {
            background: linear-gradient(135deg, #10b981, #059669);
            border-color: #10b981;
        }

        .step.completed .step-circle::before {
            content: '✓';
            font-size: 1.2rem;
        }

        .step-label {
            font-size: 0.85rem;
            color: #94a3b8;
            text-align: center;
            font-weight: 500;
            max-width: 120px;
        }

        .step.active .step-label {
            color: #60a5fa;
            font-weight: 600;
        }

        .step.completed .step-label {
            color: #10b981;
        }

        /* Section Container */
        .section-container {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 40px;
            margin-bottom: 30px;
            border: 1px solid rgba(148, 163, 184, 0.1);
            display: none;
        }

        .section-container.active {
            display: block;
            animation: fadeIn 0.5s ease;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .section-header {
            margin-bottom: 30px;
        }

        .section-title {
            font-size: 2rem;
            margin-bottom: 12px;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .section-description {
            color: #cbd5e1;
            font-size: 1.05rem;
            line-height: 1.6;
        }

        /* Navigation Buttons */
        .navigation-buttons {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin-top: 40px;
        }

        .nav-btn {
            padding: 14px 32px;
            border: none;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .nav-btn-prev {
            background: rgba(148, 163, 184, 0.2);
            color: #e2e8f0;
        }

        .nav-btn-prev:hover:not(:disabled) {
            background: rgba(148, 163, 184, 0.3);
            transform: translateX(-4px);
        }

        .nav-btn-next {
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            color: white;
            margin-left: auto;
        }

        .nav-btn-next:hover:not(:disabled) {
            transform: translateX(4px);
            box-shadow: 0 8px 20px rgba(96, 165, 250, 0.4);
        }

        .nav-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        /* Placeholder for game content */

        /* Responsive */
        @media (max-width: 768px) {
            .progress-steps {
                flex-wrap: wrap;
                gap: 20px;
            }

            .step {
                min-width: 80px;
            }

            .progress-line {
                display: none;
            }

            .navigation-buttons {
                flex-direction: column;
            }

            .nav-btn-next {
                margin-left: 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Progress Tracker -->
        <div class="progress-tracker">
            <div class="progress-header">
                <h1>English Essay Skills Module</h1>
                <p class="progress-subtitle">Ideation help for an English Essay. Start by finding accurate sources and end with citing them.</p>
            </div>

            <div class="progress-steps">
                <div class="progress-line">
                    <div class="progress-line-fill" id="progress-fill"></div>
                </div>
                
                <div class="step active" data-step="1">
                    <div class="step-circle">1</div>
                    <div class="step-label">Media Bias Game</div>
                </div>
                
                <div class="step" data-step="2">
                    <div class="step-circle">2</div>
                    <div class="step-label">Thesis Generator</div>
                </div>
                
                <div class="step" data-step="3">
                    <div class="step-circle">3</div>
                    <div class="step-label">Citation Generator</div>
                </div>
                
                <div class="step" data-step="4">
                    <div class="step-circle">4</div>
                    <div class="step-label">Performance Review</div>
                </div>
            </div>
        </div>

        <!-- Section 1: Media Bias Game (with AI Chatbox) -->
        <div class="section-container active" id="section-1">
            <div class="section-header">
                <h2 class="section-title">Media Bias Sorting Game</h2>
                <p class="section-description">
                    When writing a paper, checking the bias of sources is very important. 
                    Drag the news sources to the correct bins. Use the AI chatbox below if you need help!
                </p>
            </div>

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
  background: url('{{ site.baseurl }}/MediaBiasChanges/media/assets/spacebackground.jpg') no-repeat center center fixed;
  background-size: cover;
  background-color: #061226;
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

<!-- REPLACE YOUR ENTIRE SCRIPT SECTION WITH THIS -->
<script type="module">
import {pythonURI,fetchOptions} from '{{site.baseurl}}/assets/js/api/config.js';
window.pythonURI = pythonURI;

// Authentication Manager Class
// Fixed Authentication Manager with proper CORS and GitHub validation

class AuthManager {
    constructor() {
        this.currentUser = null;
    }

    async login(uid, password) {
        const requestOptions = {
            method: 'POST',
            mode: 'cors',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-Origin': 'client'
            },
            body: JSON.stringify({ uid, password })
        };

        const response = await fetch(`${window.pythonURI}/api/authenticate`, requestOptions);
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || 'Login failed');
        }

        const data = await response.json();
        this.currentUser = data.user;
        sessionStorage.setItem('currentUser', JSON.stringify(data.user));
        return data.user;
    }

    async signup(name, uid, password) {
        // First verify GitHub ID exists
        const isValidGitHub = await this.verifyGitHubAccount(uid);
        if (!isValidGitHub) {
            throw new Error(`GitHub account "${uid}" not found. Please use your actual GitHub username.`);
        }

        const requestOptions = {
            method: 'POST',
            mode: 'cors',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-Origin': 'client',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                uid: uid,
                password: password,
                email: `${uid}@github.user`
            })
        };

        const response = await fetch(`${window.pythonURI}/api/user`, requestOptions);
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || 'Signup failed');
        }

        return await response.json();
    }

    async verifyGitHubAccount(username) {
        if (!username || username.length < 1) return false;
        
        try {
            const response = await fetch(`https://api.github.com/users/${username}`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/vnd.github.v3+json'
                }
            });
            
            if (response.status === 404) {
                return false;
            }
            
            if (response.ok) {
                const data = await response.json();
                return data.login.toLowerCase() === username.toLowerCase();
            }
            
            return false;
        } catch (error) {
            console.error('GitHub verification error:', error);
            return false;
        }
    }

    async logout() {
        const requestOptions = {
            method: 'DELETE',
            mode: 'cors',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-Origin': 'client'
            }
        };

        try {
            await fetch(`${window.pythonURI}/api/authenticate`, requestOptions);
        } catch (error) {
            console.warn('Logout request failed:', error);
        }

        this.currentUser = null;
        sessionStorage.removeItem('currentUser');
    }

    setGuestUser() {
        this.currentUser = {
            uid: 'guest',
            name: 'Guest Player',
            role: 'Guest'
        };
        sessionStorage.setItem('currentUser', JSON.stringify(this.currentUser));
    }

    checkExistingSession() {
        const savedUser = sessionStorage.getItem('currentUser');
        if (savedUser) {
            try {
                this.currentUser = JSON.parse(savedUser);
                return this.currentUser;
            } catch (error) {
                console.error('Failed to parse saved user:', error);
                sessionStorage.removeItem('currentUser');
            }
        }
        return null;
    }

    getCurrentUser() {
        return this.currentUser;
    }
}

// Enhanced modal with better GitHub verification UI
function showSignInPrompt() {
    if (document.getElementById('auth-modal')) {
        document.getElementById('auth-modal').remove();
    }
    
    const modal = document.createElement('div');
    modal.id = 'auth-modal';
    modal.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(0,0,0,0.85);display:flex;align-items:center;justify-content:center;z-index:10000;';
    modal.innerHTML = `
        <div style="background:linear-gradient(135deg, #353e74ff, #9384d5ff);padding:40px;border-radius:20px;box-shadow:0 20px 60px rgba(0,0,0,0.4);max-width:420px;width:90%;">
            <!-- Login Form -->
            <div id="login-form-container">
                <h2 style="color:#ffffff;margin-bottom:10px;font-size:1.8rem;text-align:center;">User Login</h2>
                <p style="color:#c8d7eb;margin-bottom:25px;text-align:center;">Sign in to save your scores</p>
                <div style="margin-bottom:20px;">
                    <label style="display:block;color:#e2e8f0;font-weight:600;margin-bottom:8px;">GitHub Username:</label>
                    <input type="text" id="login-uid" placeholder="Your GitHub username" style="width:100%;padding:12px;border-radius:10px;border:2px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.1);color:#fff;font-size:1rem;" />
                </div>
                <div style="margin-bottom:20px;">
                    <label style="display:block;color:#e2e8f0;font-weight:600;margin-bottom:8px;">Password:</label>
                    <input type="password" id="login-password" placeholder="Enter password" style="width:100%;padding:12px;border-radius:10px;border:2px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.1);color:#fff;font-size:1rem;" />
                </div>
                <div style="display:flex;gap:12px;">
                    <button id="guest-btn" style="flex:1;padding:12px;border-radius:10px;background:rgba(255,255,255,0.2);color:white;font-weight:700;border:none;cursor:pointer;">Play as Guest</button>
                    <button id="login-btn" style="flex:1;padding:12px;border-radius:10px;background:#4299e1;color:white;font-weight:700;border:none;cursor:pointer;">Login</button>
                </div>
                <p id="login-error" style="color:#ff6b6b;margin-top:10px;display:none;font-size:0.9rem;text-align:center;"></p>
                <p id="login-success" style="color:#4ade80;margin-top:10px;display:none;font-size:0.9rem;text-align:center;"></p>
                <p style="text-align:center;margin-top:20px;color:#c8d7eb;font-size:0.9rem;">
                    Don't have an account? <a href="#" id="show-signup" style="color:#4299e1;text-decoration:none;font-weight:600;">Sign up</a>
                </p>
            </div>
            
            <!-- Signup Form -->
            <div id="signup-form-container" style="display:none;">
                <h2 style="color:#ffffff;margin-bottom:10px;font-size:1.8rem;text-align:center;">Create Account</h2>
                <p style="color:#c8d7eb;margin-bottom:25px;text-align:center;font-size:0.9rem;">⚠️ You must have a GitHub account</p>
                <div style="margin-bottom:20px;">
                    <label style="display:block;color:#e2e8f0;font-weight:600;margin-bottom:8px;">Full Name:</label>
                    <input type="text" id="signup-name" placeholder="Enter your name" style="width:100%;padding:12px;border-radius:10px;border:2px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.1);color:#fff;font-size:1rem;" />
                </div>
                <div style="margin-bottom:20px;">
                    <label style="display:block;color:#e2e8f0;font-weight:600;margin-bottom:8px;">GitHub Username:</label>
                    <div style="position:relative;">
                        <input type="text" id="signup-uid" placeholder="Your GitHub username" style="width:100%;padding:12px;padding-right:45px;border-radius:10px;border:2px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.1);color:#fff;font-size:1rem;" />
                        <div id="github-status" style="position:absolute;right:12px;top:50%;transform:translateY(-50%);font-size:1.2rem;display:none;"></div>
                    </div>
                    <p style="color:#9bb3d6;font-size:0.85rem;margin-top:6px;">We'll verify this is a real GitHub account</p>
                </div>
                <div style="margin-bottom:20px;">
                    <label style="display:block;color:#e2e8f0;font-weight:600;margin-bottom:8px;">Password:</label>
                    <input type="password" id="signup-password" placeholder="8+ characters" style="width:100%;padding:12px;border-radius:10px;border:2px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.1);color:#fff;font-size:1rem;" />
                </div>
                <div style="display:flex;gap:12px;">
                    <button id="back-to-login" style="flex:1;padding:12px;border-radius:10px;background:rgba(255,255,255,0.2);color:white;font-weight:700;border:none;cursor:pointer;">Back</button>
                    <button id="signup-btn" style="flex:1;padding:12px;border-radius:10px;background:#4299e1;color:white;font-weight:700;border:none;cursor:pointer;">Sign Up</button>
                </div>
                <p id="signup-error" style="color:#ff6b6b;margin-top:10px;display:none;font-size:0.9rem;text-align:center;"></p>
                <p id="signup-success" style="color:#4ade80;margin-top:10px;display:none;font-size:0.9rem;text-align:center;"></p>
            </div>
            
            <button id="close-modal" style="width:100%;margin-top:15px;padding:10px;border-radius:10px;background:rgba(255,255,255,0.1);color:#d6e6ff;border:1px solid rgba(255,255,255,0.15);cursor:pointer;font-weight:600;">Close</button>
        </div>
    `;
    document.body.appendChild(modal);

    // Initialize AuthManager if not already
    if (!window.authManager) {
        window.authManager = new AuthManager();
    }

    // Event handlers
    document.getElementById('close-modal').addEventListener('click', () => modal.remove());
    
    document.getElementById('guest-btn').addEventListener('click', () => {
        window.authManager.setGuestUser();
        modal.remove();
        if (window.updateAuthButton) window.updateAuthButton();
    });
    
    // Toggle between login and signup
    document.getElementById('show-signup').addEventListener('click', (e) => {
        e.preventDefault();
        document.getElementById('login-form-container').style.display = 'none';
        document.getElementById('signup-form-container').style.display = 'block';
    });
    
    document.getElementById('back-to-login').addEventListener('click', () => {
        document.getElementById('signup-form-container').style.display = 'none';
        document.getElementById('login-form-container').style.display = 'block';
    });

    // Real-time GitHub verification
    let verifyTimeout;
    document.getElementById('signup-uid').addEventListener('input', (e) => {
        const username = e.target.value.trim();
        const statusEl = document.getElementById('github-status');
        
        clearTimeout(verifyTimeout);
        
        if (username.length === 0) {
            statusEl.style.display = 'none';
            return;
        }
        
        statusEl.style.display = 'block';
        statusEl.textContent = '⏳';
        statusEl.style.color = '#fbbf24';
        
        verifyTimeout = setTimeout(async () => {
            const isValid = await window.authManager.verifyGitHubAccount(username);
            if (isValid) {
                statusEl.textContent = '✓';
                statusEl.style.color = '#4ade80';
            } else {
                statusEl.textContent = '✗';
                statusEl.style.color = '#ff6b6b';
            }
        }, 800);
    });

    // Login handler
    document.getElementById('login-btn').addEventListener('click', async () => {
        const uid = document.getElementById('login-uid').value.trim();
        const password = document.getElementById('login-password').value;
        const errorMsg = document.getElementById('login-error');
        const successMsg = document.getElementById('login-success');
        const loginBtn = document.getElementById('login-btn');
        
        errorMsg.style.display = 'none';
        successMsg.style.display = 'none';
        
        if (!uid || !password) {
            errorMsg.textContent = 'Please enter both username and password';
            errorMsg.style.display = 'block';
            return;
        }
        
        loginBtn.disabled = true;
        loginBtn.textContent = 'Logging in...';
        
        try {
            await window.authManager.login(uid, password);
            successMsg.textContent = 'Login successful!';
            successMsg.style.display = 'block';
            setTimeout(() => {
                modal.remove();
                if (window.updateAuthButton) window.updateAuthButton();
                window.location.reload();
            }, 1000);
        } catch (error) {
            errorMsg.textContent = error.message;
            errorMsg.style.display = 'block';
        } finally {
            loginBtn.disabled = false;
            loginBtn.textContent = 'Login';
        }
    });

    // Signup handler - FIXED auto-login
    document.getElementById('signup-btn').addEventListener('click', async () => {
        const name = document.getElementById('signup-name').value.trim();
        const uid = document.getElementById('signup-uid').value.trim();
        const password = document.getElementById('signup-password').value;
        const errorMsg = document.getElementById('signup-error');
        const successMsg = document.getElementById('signup-success');
        const signupBtn = document.getElementById('signup-btn');
        
        errorMsg.style.display = 'none';
        successMsg.style.display = 'none';
        
        if (!name || !uid || !password) {
            errorMsg.textContent = 'Please fill in all fields';
            errorMsg.style.display = 'block';
            return;
        }
        
        if (password.length < 8) {
            errorMsg.textContent = 'Password must be at least 8 characters';
            errorMsg.style.display = 'block';
            return;
        }
        
        signupBtn.disabled = true;
        signupBtn.textContent = 'Verifying GitHub...';
        
        try {
            await window.authManager.signup(name, uid, password);
            successMsg.textContent = 'Account created! Logging in...';
            successMsg.style.display = 'block';
            signupBtn.textContent = 'Logging in...';
            
            // Wait a moment for backend to process, then login
            await new Promise(resolve => setTimeout(resolve, 500));
            
            try {
                await window.authManager.login(uid, password);
                modal.remove();
                if (window.updateAuthButton) window.updateAuthButton();
                window.location.reload();
            } catch (loginError) {
                console.error('Auto-login failed:', loginError);
                successMsg.textContent = 'Account created! Please click "Back" and login.';
                signupBtn.disabled = false;
                signupBtn.textContent = 'Sign Up';
            }
        } catch (error) {
            errorMsg.textContent = error.message;
            errorMsg.style.display = 'block';
            signupBtn.disabled = false;
            signupBtn.textContent = 'Sign Up';
        }
    });
}

// Make functions available globally
window.AuthManager = AuthManager;
window.showSignInPrompt = showSignInPrompt;

// Update auth button text/handler
window.updateAuthButton = function() {
    const authBtn = document.getElementById('auth-btn');
    if (!authBtn) return;
    
    const currentUser = window.authManager ? window.authManager.getCurrentUser() : null;
    
    if (currentUser && currentUser.uid !== 'guest') {
        authBtn.textContent = 'Sign Out';
        authBtn.onclick = () => window.signOut();
    } else {
        authBtn.textContent = 'Sign In';
        authBtn.onclick = () => window.showSignInPrompt();
    }
};

// Sign out function
window.signOut = async function() {
    await window.authManager.logout();
    window.authManager.setGuestUser();
    window.location.reload();
};

// Initialize on load
window.addEventListener('DOMContentLoaded', () => {
    if (!window.authManager) {
        window.authManager = new AuthManager();
    }
    const existingUser = window.authManager.checkExistingSession();
    if (!existingUser || existingUser.uid === 'guest') {
        window.authManager.setGuestUser();
    }
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
    // Get current user from authManager
    const user = window.authManager ? window.authManager.getCurrentUser() : null;
    
    if (user && user.uid !== 'guest') {
        currentPlayer = user.uid;
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

        // CHANGED: Submit validates and shows incorrect placements
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
</script></p>
                <p style="margin-top: 20px; font-size: 0.9rem;">
                </p>
            </div>

            <div style="margin-top: 40px;">
                <div class="content-placeholder">
                    <p>
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

<script>
// Smart Prompts Feature
const PROMPT_TEMPLATES = [
    { id: 1, text: "What is the political bias of {source}?" },
    { id: 2, text: "Show me recent top stories from {source}" },
    { id: 3, text: "How does {source} compare to other news outlets?" },
    { id: 4, text: "What are the most controversial topics covered by {source}?" },
    { id: 5, text: "Is {source} a reliable news source?" }
];

const PROMPTS_API_BASE = 'http://localhost:8001';
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

// Send message
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
        const response = await fetch('http://localhost:8001/api/chat', {
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
</script></p>
                    <p style="margin-top: 20px; font-size: 0.9rem;">
                    </p>
                </div>
            </div>

            <div class="navigation-buttons">
                <button class="nav-btn nav-btn-prev" disabled>
                    ← Previous
                </button>
                <button class="nav-btn nav-btn-next" onclick="nextSection()">
                    Next Section →
                </button>
            </div>
        </div>

        <!-- Section 2: Thesis Generator -->
        <div class="section-container" id="section-2">
            <div class="section-header">
                <h2 class="section-title">Thesis Generator</h2>
                <p class="section-description">
                Starting your essay can be challenging. Use this AI-powered tool to 
                generate strong thesis statements that outline your argument effectively.
                </p>
            </div>

            <div class="content-placeholder">
                <p>
                <style>
        .thesis-gen-card {
            background: linear-gradient(160deg, #856ccadd, #5b6ebce1);
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
<body>
    <div class="thesis-gen-card">

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
            <button class="thesis-btn thesis-btn-primary" id="thesis-generate">Generate Thesis</button>
            <button class="thesis-btn thesis-btn-secondary" id="thesis-clear">🔄 Clear Form</button>
        </div>

        <div id="thesis-status" class="thesis-status"></div>

        <div class="thesis-output-section" id="thesis-output-section" style="display: none;">
            <h4>Generated Thesis Statements</h4>
            <div id="thesis-output"></div>
            <div id="thesis-recommendations"></div>
        </div>
    </div>

<script type="module">
    import {pythonURI} from '{{site.baseurl}}/assets/js/api/config.js';

    const API_BASE = pythonURI || 'http://localhost:8001';

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
            const response = await fetch(`${API_BASE}/api/thesis/generate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    topic: topic,
                    position: position,
                    supportingPoints: supportingPoints,
                    thesisType: thesisType,
                    audience: audience
                })
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.error || `HTTP ${response.status}: ${response.statusText}`);
            }

            const result = await response.json();
            
            if (!result.success || !result.data) {
                throw new Error('Invalid response from server');
            }

            displayTheses(result.data);
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
                        <h5>Supporting Arguments</h5>
                        <ul>
                            ${thesis.supportingArguments.map(arg => `<li>${arg}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}
                
                ${thesis.counterarguments && thesis.counterarguments.length > 0 ? `
                    <div class="thesis-details">
                        <h5>Counterarguments to Address</h5>
                        <ul>
                            ${thesis.counterarguments.map(counter => `<li>${counter}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}
                
                <button class="thesis-btn-use" data-statement="${thesis.statement.replace(/"/g, '&quot;')}">
                    Use This Thesis
                </button>
            `;
            
            thesisOutput.appendChild(card);
        });

        // Add event listeners to "Use This Thesis" buttons
        document.querySelectorAll('.thesis-btn-use').forEach(btn => {
            btn.addEventListener('click', function() {
                const statement = this.getAttribute('data-statement');
                useThesis(statement);
            });
        });

        if (data.recommendations) {
            recommendationsOutput.innerHTML = `
                <div class="thesis-recommendations">
                    <h5>Recommendations</h5>
                    <p>${data.recommendations}</p>
                </div>
            `;
        }
    }

    function useThesis(statement) {
        navigator.clipboard.writeText(statement).then(() => {
            showThesisStatus('Thesis copied to clipboard!', 'success');
        }).catch(() => {
            showThesisStatus('Please manually copy the thesis', 'error');
        });
    }

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
</p>
                <p style="margin-top: 20px; font-size: 0.9rem;">
                </p>
            </div>

            <div class="navigation-buttons">
                <button class="nav-btn nav-btn-prev" onclick="prevSection()">
                    ← Previous
                </button>
                <button class="nav-btn nav-btn-next" onclick="nextSection()">
                    Next Section →
                </button>
            </div>
        </div>

        <!-- Section 3: Citation Generator -->
        <div class="section-container" id="section-3">
            <div class="section-header">
                <h2 class="section-title">Citation Generator</h2>
                <p class="section-description">
                    It's important to include correct citations for your work. 
                    There are many formats including MLA, APA, and Chicago. 
                    This tool helps you create proper citations for your sources.
                </p>
            </div>
            <div class="content-placeholder">
                <p>
<style>
  /* Import modern, readable font matching thesis generator */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

  .cite-card { 
    background: linear-gradient(160deg,  #555dc2d2, #564ea0ff); 
    color:#ffffff; 
    padding:18px; 
    border-radius:12px; 
    margin:20px 0;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  }
  
  .cite-row { 
    display: flex; 
    gap: 10px;
    flex-wrap: wrap;
    align-items: center;
    margin-top: 8px;
  }
  
  .cite-label { 
    min-width: 110px;
    font-weight:700; 
    color:#ffffff;
    font-size: 0.9rem;
  }
  
  .cite-input, .cite-select { 
    flex: 1;
    padding:8px; 
    border-radius:6px; 
    border:1px solid rgba(255,255,255,0.2); 
    background:rgba(255,255,255,0.15); 
    color:#ffffff;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
  }
  
  .cite-input::placeholder {
    color: rgba(255, 255, 255, 0.6);
  }
  
  .cite-select option {
    background: #564ea0ff;
    color: #ffffff;
  }
  
  .cite-actions { 
    display:flex; 
    gap:10px; 
    margin-top:12px; 
    justify-content:flex-end;
    flex-wrap: wrap;
  }
  
  .cite-btn { 
    padding:8px 12px; 
    border-radius:8px; 
    border:none; 
    cursor:pointer; 
    font-weight:700;
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  
  .cite-btn.primary { 
    background:#7ad2f9; 
    color:#082033; 
  }
  
  .cite-btn.ghost { 
    background:rgba(255,255,255,0.15); 
    color:#ffffff; 
    border:1px solid rgba(255,255,255,0.2); 
  }
  
  .cite-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
  
  .btn-hint {
    font-size: 0.7rem;
    color: rgba(255, 255, 255, 0.8);
    font-weight: 400;
  }
  
  .cite-output { 
    margin-top:12px; 
    background:rgba(0,0,0,0.25); 
    padding:12px; 
    border-radius:8px; 
    font-family: 'Inter', sans-serif;
    color:#ffffff;
    font-size: 0.9rem;
  }
  
  .cite-output:empty::before {
    content: 'Your citation will appear here...';
    color: rgba(255, 255, 255, 0.6);
    font-style: italic;
  }
  
  .cite-small { 
    font-size:0.9rem; 
    color:rgba(255, 255, 255, 0.75); 
    margin-top:6px;
  }
  
  .works-cited-section {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid rgba(255,255,255,0.2);
  }
  
  .works-cited-section h3 {
    font-size: 1.2rem;
    color: #ffffff;
    margin-bottom: 12px;
    font-family: 'Inter', sans-serif;
  }
  
  .works-cited-list {
    background: rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 10px;
    padding: 12px;
    max-height: 320px;
    overflow-y: auto;
  }
  
  .works-cited-list:empty::before {
    content: 'No saved citations yet. Click "Save" to add citations to your Works Cited list.';
    color: rgba(255, 255, 255, 0.7);
    font-style: italic;
    display: block;
    text-align: center;
    padding: 20px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
  }
  
  .citation-item {
    padding: 10px;
    margin-bottom: 10px;
    background: rgba(255,255,255,0.1);
    border-left: 4px solid #7ad2f9;
    border-radius: 6px;
    position: relative;
    padding-right: 40px;
  }
  
  .citation-item:last-child {
    margin-bottom: 0;
  }
  
  .citation-text {
    color: #ffffff;
    font-size: 0.85rem;
    line-height: 1.45;
    font-family: 'Inter', sans-serif;
  }
  
  .citation-delete {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(248, 113, 113, 0.8);
    color: white;
    border: none;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    cursor: pointer;
    font-weight: bold;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    font-family: 'Inter', sans-serif;
  }
  
  .citation-delete:hover {
    background: rgba(248, 113, 113, 1);
    transform: translateY(-50%) scale(1.1);
  }

  .cite-input.missing {
  border: 2px solid #f87171 !important;
  background: rgba(248, 113, 113, 0.2) !important;
}

.cite-warning {
  margin-top: 10px;
  padding: 10px;
  border-radius: 8px;
  background: rgba(248, 113, 113, 0.15);
  color: #fff;
  font-size: 0.85rem;
  font-family: 'Inter', sans-serif;
}
</style>

<div class="cite-card" id="citation-tool">
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
    <input id="cite-title" class="cite-input" placeholder="Article title" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Source</div>
    <input id="cite-source" class="cite-input" placeholder="e.g., The New York Times" />
  </div>

  <div class="cite-row">
    <div class="cite-label">URL</div>
    <input id="cite-url" class="cite-input" placeholder="https://..." />
    <button id="cite-fetch-metadata" class="cite-btn ghost" title="Generate citation from URL" style="margin-left:8px;min-width:160px;">
      Generate from URL
    </button>
  </div>

  <div class="cite-actions">
    <button id="cite-generate" class="cite-btn primary">Generate</button>
    <button id="cite-reset" class="cite-btn ghost"> Reset <span class="btn-hint">(clear fields)</span> </button>
    <button id="cite-copy" class="cite-btn ghost">
      Copy <span class="btn-hint">(to clipboard)</span>
    </button>
    <button id="cite-save" class="cite-btn ghost" title="Save locally">
      Save <span class="btn-hint">(add to Works Cited)</span>
    </button>
    <button id="cite-load" class="cite-btn ghost" title="Load last">
      Load <span class="btn-hint">(view Works Cited)</span>
    </button>
  </div>

  <div id="cite-output" class="cite-output" aria-live="polite"></div>
  <div id="cite-parenthetical" class="cite-output" style="margin-top:8px;"></div>
  <div id="cite-warning" class="cite-warning" style="display:none;"></div>
  <div class="cite-small">Formats: APA, MLA (9th ed.), Chicago (author-date). Saved citations are stored locally in your browser.</div>

  <div class="works-cited-section" id="works-cited-section" style="display: none;">
    <h3>Works Cited</h3>
    <div id="works-cited-list" class="works-cited-list"></div>
  </div>
</div>

<script>
(function(){
  // ===== COLLEGE BOARD REQUIREMENTS DOCUMENTATION =====
  
  /* 
   * STUDENT-DEVELOPED PROCEDURE: processCitationList
   * Purpose: Process and filter a list of saved citations based on style and date range
   * Parameters:
   *   - citationList (array): List of citation objects to process
   *   - filterStyle (string): Citation style to filter by (e.g., "apa", "mla", "chicago", or "all")
   *   - maxItems (number): Maximum number of items to return
   * Return type: Object containing filtered citations and statistics
   * 
   * This procedure demonstrates:
   * - LISTS/COLLECTION: Works with array of citation objects
   * - ITERATION: Loops through citation list
   * - SEQUENCING: Steps execute in specific order
   * - SELECTION: Conditional logic for filtering
   * - ALGORITHM: Complete process for filtering and counting
   * - ABSTRACTION: Encapsulates complex filtering logic
   */
  
  function processCitationList(citationList, filterStyle, maxItems) {
    // SEQUENCING: Initialize variables in order
    let filtered = [];
    let styleCount = { apa: 0, mla: 0, chicago: 0 };
    
    // ITERATION: Loop through each citation in the list
    for (let i = 0; i < citationList.length; i++) {
      let citation = citationList[i];
      
      // SELECTION: Conditional logic to filter by style
      if (filterStyle === 'all' || citation.style === filterStyle) {
        filtered.push(citation);
      }
      
      // Count citations by style
      if (citation.style && styleCount.hasOwnProperty(citation.style)) {
        styleCount[citation.style]++;
      }
      
      // SELECTION: Stop if we've reached max items
      if (filtered.length >= maxItems) {
        break;
      }
    }
    
    // Return processed data
    return {
      citations: filtered,
      totalCount: citationList.length,
      styleCounts: styleCount
    };
  }
  
  // ===== END REQUIREMENTS DOCUMENTATION =====
  
  // DOM Elements - INPUT from user interface
  const styleEl = document.getElementById('cite-style');
  const authorEl = document.getElementById('cite-author');
  const dateEl = document.getElementById('cite-date');
  const titleEl = document.getElementById('cite-title');
  const sourceEl = document.getElementById('cite-source');
  const urlEl = document.getElementById('cite-url');
  const outEl = document.getElementById('cite-output');
  const fetchBtn = document.getElementById('cite-fetch-metadata');
  const generateBtn = document.getElementById('cite-generate');
  const copyBtn = document.getElementById('cite-copy');
  const saveBtn = document.getElementById('cite-save');
  const loadBtn = document.getElementById('cite-load');
  const worksCitedSection = document.getElementById('works-cited-section');
  const worksCitedList = document.getElementById('works-cited-list');

  // Backend configuration
  if (!window.fetchProxyBase) {
      window.fetchProxyBase = 'http://localhost:8001/api/media';
      console.info('fetchProxyBase defaulted to', window.fetchProxyBase);
  }

  // ===== CROSS-CHECK FORMATTING =====
function validateCitationFields() {
  const style = styleEl.value;
  const warnings = [];

  // Basic checks for missing required fields
  if (!authorEl.value.trim()) warnings.push('Author is missing');
  if (!titleEl.value.trim()) warnings.push('Title is missing');
  if (!sourceEl.value.trim()) warnings.push('Source is missing');
  if (!dateEl.value.trim()) warnings.push('Date is missing');

  // Style-specific checks
  if (style === 'apa' && dateEl.value && !/\d{4}/.test(dateEl.value)) {
    warnings.push('APA date should include a year (YYYY)');
  }
  if (style === 'mla' && dateEl.value && !/\d{4}/.test(dateEl.value)) {
    warnings.push('MLA date should include a year (YYYY)');
  }
  if (style === 'chicago' && dateEl.value && !/\d{4}/.test(dateEl.value)) {
    warnings.push('Chicago date should include a year (YYYY)');
  }

  // Display warnings
  const warningEl = document.getElementById('cite-warning');
  if (warnings.length) {
    warningEl.innerHTML = `⚠️ Formatting issues:<br><b>${warnings.join('<br>')}</b>`;
    warningEl.style.display = 'block';
  } else {
    warningEl.style.display = 'none';
  }
}

// Run validation whenever an input or style changes
[authorEl, titleEl, sourceEl, dateEl, urlEl, styleEl].forEach(el => {
  el.addEventListener('input', validateCitationFields);
});
styleEl.addEventListener('change', validateCitationFields);

// Save session whenever inputs change
[authorEl, titleEl, sourceEl, dateEl, urlEl, styleEl].forEach(el => {
  el.addEventListener('input', () => {
    localStorage.setItem(SESSION_KEY, JSON.stringify({
      author: authorEl.value,
      title: titleEl.value,
      source: sourceEl.value,
      date: dateEl.value,
      url: urlEl.value,
      style: styleEl.value
    }));
  });
});

  // LIST: Storage key for citation collection
  const KEY = 'biasGame_citations_v1';

  function safe(val, fallback='') { return (val || '').trim(); }

  // FIXED APA FORMAT
  function fmtAPA({ author, date, title, source, url }) {
    // APA Format: Author. (Date). Title. Source. URL
    // If no author, start with Title. (Date). then rest
    let parts = [];

    if (author) {
      parts.push(author + '.');
      if (date) {
        parts.push(`(${date}).`);
      }
      if (title) {
        parts.push(title + '.');
      }
    } else {
      // No author: Title. (Date). Source. URL
      if (title) {
        parts.push(title + '.');
      }
      if (date) {
        parts.push(`(${date}).`);
      }
    }
    
    if (source) {
      parts.push(`<i>${source}</i>.`);
    }
    
    if (url) {
      parts.push(url);
    }

    return parts.join(' ').trim();
  }

  // CORRECT MLA 9TH EDITION FORMAT
function fmtMLA9({ author, date, title, source, url }) {
  // MLA format:
  // Author. "Title." Source, Day Mon. Year, URL.

  let parts = [];

  // Author
  if (author) {
    parts.push(author.trim() + '.');
  }

  // Title (required if no author)
  if (title) {
    parts.push(`"${title.trim()}."`);
  }

  // Source (italicized)
  if (source) {
    parts.push(`<i>${source.trim()}</i>,`);
  }

  // Date → MLA format (Day Mon. Year)
  if (date) {
    let mlaDate = date;

    const parsed = Date.parse(date);
    if (!isNaN(parsed)) {
      const d = new Date(parsed);
      const day = d.getUTCDate();
      const year = d.getUTCFullYear();
      const months = [
        'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June',
        'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.'
      ];
      const month = months[d.getUTCMonth()];
      mlaDate = `${day} ${month} ${year}`;
    }

    parts.push(mlaDate + ',');
  }

  // URL (no https:// removal in MLA 9 unless teacher says so)
  if (url) {
    parts.push(url.trim() + '.');
  }

  return parts.join(' ').replace(/\s+/g, ' ').trim();
}

  // CORRECT CHICAGO (AUTHOR–DATE) FORMAT
function fmtChicago({ author, date, title, source, url }) {
  // Chicago author-date:
  // Author. (Date). "Title." Source. URL.
  // No author → "Title." (Date). Source. URL.

  let parts = [];

  // Author (if present)
  if (author) {
    parts.push(author.trim() + '.');
  }

  // Title (always quoted)
  if (title) {
    parts.push(`"${title.trim()}."`);
  }

  // Date in parentheses (after title if no author)
  if (date) {
    parts.push(`(${date.trim()}).`);
  }

  // Source (italicized)
  if (source) {
    parts.push(`<i>${source.trim()}</i>.`);
  }

  // URL (no trailing period in Chicago author-date)
  if (url) {
    parts.push(url.trim());
  }

  return parts.join(' ').replace(/\s+/g, ' ').trim();
}

function buildParenthetical({ author, title, date, style = 'apa' }) {
  // Extract year if possible
  let year = '';
  if (date) {
    const match = date.match(/\d{4}/);
    if (match) year = match[0];
  }

  // Short title for no-author cases
  const shortTitle = title
    ? title.split(' ').slice(0, 3).join(' ')
    : '';

  // ---- MLA parenthetical
  if (style === 'mla') {
    if (author) {
      // MLA: only author last name
      const last = author.split(',')[0].trim();
      return `(${last})`;
    }
    if (shortTitle) {
      // MLA: shortened title in quotes (no year)
      return `("${shortTitle}…")`;
    }
    return '';
  }

  // ---- APA parenthetical
  if (style === 'apa') {
    if (author) {
      const last = author.split(',')[0].trim();
      // APA: (Author, Year)
      return year ? `(${last}, ${year})` : `(${last})`;
    }
    if (shortTitle) {
      // APA: (Short Title, Year) if no author
      return year
        ? `(${shortTitle}, ${year})`
        : `(${shortTitle})`;
    }
    return '';
  }

  // ---- Chicago (author-date) parenthetical
  if (style === 'chicago') {
    if (author) {
      const last = author.split(',')[0].trim();
      // Chicago: (Author Year) — **no comma**
      return year ? `(${last} ${year})` : `(${last})`;
    }
    if (shortTitle) {
      // Chicago: (Short Title Year) — no comma
      return year
        ? `(${shortTitle} ${year})`
        : `(${shortTitle})`;
    }
    return '';
  }

  // Default fallback
  return '';
}

  // OUTPUT: Generate and display citation
  function generate() {
  const payload = {
    author: safe(authorEl.value),
    date: safe(dateEl.value),
    title: safe(titleEl.value),
    source: safe(sourceEl.value),
    url: safe(urlEl.value)
  };

  const missing = [];
  const fields = [
    { el: authorEl, key: 'author', label: 'Author' },
    { el: titleEl, key: 'title', label: 'Title' },
    { el: sourceEl, key: 'source', label: 'Source / Website' },
    { el: dateEl, key: 'date', label: 'Publication Date' }
  ];

  // Reset previous highlights
  fields.forEach(f => f.el.classList.remove('missing'));

  // Detect missing fields
  fields.forEach(f => {
    if (!payload[f.key]) {
      missing.push(f.label);
      f.el.classList.add('missing');
    }
  });

const style = styleEl.value; // 'apa', 'mla', or 'chicago'

let citation = '';
if (style === 'mla') citation = fmtMLA9(payload);
else if (style === 'chicago') citation = fmtChicago(payload);
else citation = fmtAPA(payload);

outEl.innerHTML = citation;

// Pass style to buildParenthetical!
const parentheticalEl = document.getElementById('cite-parenthetical');
const parenthetical = buildParenthetical({ ...payload, style });

if (parentheticalEl) {
  parentheticalEl.innerHTML = parenthetical
    ? `<b>Parenthetical citation:</b> ${parenthetical}`
    : '';
}

  // Warning message
  const warningEl = document.getElementById('cite-warning');
  if (missing.length > 0) {
    warningEl.innerHTML =
      `⚠️ Missing citation info: <b>${missing.join(', ')}</b><br>
       Please manually enter these fields for a complete citation.`;
    warningEl.style.display = 'block';
  } else {
    warningEl.style.display = 'none';
  }

  return citation;
}

  // OUTPUT: Copy to clipboard (tactile/visual feedback)
  function copyToClipboard(text) {
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = text;
    const plainText = tempDiv.textContent || tempDiv.innerText || '';

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(plainText).then(() => {
        alert('✓ Citation copied to clipboard!');
      }).catch(() => { 
        fallbackCopy(plainText);
      });
    } else {
      fallbackCopy(plainText);
    }
  }

  function fallbackCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { 
      document.execCommand('copy');
      alert('✓ Citation copied to clipboard!');
    } catch (e) {
      alert('Copy failed. Please manually copy the citation.');
    }
    ta.remove();
  }

  // LIST: Save citation to collection
  function saveToWorksCited() {
    const citation = generate();
    if (!citation || citation.length < 5) {
      alert('Please generate a citation first.');
      return;
    }
    
    // Get existing list from storage
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    saved.push({ 
      citation, 
      style: styleEl.value,
      at: Date.now() 
    });
    localStorage.setItem(KEY, JSON.stringify(saved));
    alert('✓ Citation saved to Works Cited!');
    
    loadWorksCited();
  }

  // PROCEDURE CALL: Use student-developed procedure to process citations
  // OUTPUT: Display filtered and processed citations
  function loadWorksCited() {
    // Get list from storage
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    
    if (saved.length === 0) {
      worksCitedSection.style.display = 'none';
      alert('No saved citations yet. Click "Save" to add citations to your Works Cited list.');
      return;
    }

    // PROCEDURE CALL: Process citation list
    const result = processCitationList(saved, 'all', 100);
    
    // Display results
    worksCitedSection.style.display = 'block';
    worksCitedList.innerHTML = '';

    // ITERATION: Display each citation
    result.citations.forEach((item, index) => {
      const citationDiv = document.createElement('div');
      citationDiv.className = 'citation-item';
      
      const textDiv = document.createElement('div');
      textDiv.className = 'citation-text';
      textDiv.innerHTML = item.citation;
      
      const deleteBtn = document.createElement('button');
      deleteBtn.className = 'citation-delete';
      deleteBtn.innerHTML = '×';
      deleteBtn.title = 'Delete this citation';
      deleteBtn.onclick = () => deleteCitation(index);
      
      citationDiv.appendChild(textDiv);
      citationDiv.appendChild(deleteBtn);
      worksCitedList.appendChild(citationDiv);
    });

    worksCitedSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function deleteCitation(index) {
    if (!confirm('Delete this citation from Works Cited?')) return;
    
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    saved.splice(index, 1);
    localStorage.setItem(KEY, JSON.stringify(saved));
    loadWorksCited();
  }

  // INPUT: Fetch data from online source (URL)
  async function tryFetchHtml(url) {
    try {
      const r = await fetch(url, { method: 'GET', mode: 'cors' });
      if (r.ok) return await r.text();
    } catch (err) {
      console.warn('Direct fetch failed (CORS?), will try proxy', err);
    }
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

  function formatPublishedDate(raw) {
    if (!raw) return null;
    const ms = Date.parse(raw);
    if (isNaN(ms)) {
      return { apa: raw, mla: raw, chicago: raw };
    }
    const d = new Date(ms);
    const year = d.getUTCFullYear();
    const monthIdx = d.getUTCMonth();
    const day = d.getUTCDate();
    const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const monthName = months[monthIdx];
    return {
      apa: `${year}, ${monthName} ${day}`,
      mla: `${day} ${monthName} ${year}`,
      chicago: `${year}`
    };
  }

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

      const ct = res.headers.get('content-type') || '';
      const body = ct.includes('application/json') ? await res.json().catch(()=>null) : await res.text().catch(()=>null);

      if (!res.ok) {
        console.warn('Server fetch_meta returned non-OK', res.status, body);
        return null;
      }

      console.info('Server metadata response', body);
      return body;
    } catch (err) {
      console.warn('Server metadata fetch failed (network)', err);
      return null;
    }
  }

  // INPUT: Process URL and fetch metadata
  async function fetchAndFill() {
    const url = (urlEl.value || '').trim();
    if (!url) { alert('Enter a URL first.'); return; }
    fetchBtn.textContent = 'Fetching…';
    fetchBtn.disabled = true;
    try {
      let meta = await fetchMetadataFromServer(url);

      if (!meta) {
        const html = await tryFetchHtml(url);
        if (!html) {
          alert('Failed to fetch page. CORS or proxy error. Consider enabling your Flask proxy.');
          return;
        }
        meta = parseMetadataFromHtml(html, url);
      }

      // Fill form inputs with fetched data
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
      fetchBtn.textContent = 'Generate from URL';
      fetchBtn.disabled = false;
    }
  }

  // INPUT: Event listeners for user actions
  fetchBtn.addEventListener('click', fetchAndFill);
  generateBtn.addEventListener('click', generate);
  const resetBtn = document.getElementById('cite-reset');

resetBtn.addEventListener('click', () => {
  // Clear all input fields
  [authorEl, dateEl, titleEl, sourceEl, urlEl].forEach(el => el.value = '');
  
  // Clear outputs
  outEl.innerHTML = '';
  document.getElementById('cite-parenthetical').innerHTML = '';
  document.getElementById('cite-warning').style.display = 'none';
  
  // Remove missing highlights
  [authorEl, dateEl, titleEl, sourceEl].forEach(el => el.classList.remove('missing'));
});
  copyBtn.addEventListener('click', () => {
    const citation = outEl.innerHTML;
    if (!citation || citation === 'Your citation will appear here...') {
      alert('Generate a citation first.');
      return;
    }
    copyToClipboard(citation);
  });
  saveBtn.addEventListener('click', saveToWorksCited);
  loadBtn.addEventListener('click', loadWorksCited);
})();
</script>
</p>
                <p style="margin-top: 20px; font-size: 0.9rem;">
                </p>
            </div>

            <div class="navigation-buttons">
                <button class="nav-btn nav-btn-prev" onclick="prevSection()">
                    ← Previous
                </button>
                <button class="nav-btn nav-btn-next" onclick="nextSection()">
                    Next Section →
                </button>
            </div>
        </div>

        <!-- Section 4: Performance Survey -->
        <div class="section-container" id="section-4">
            <div class="section-header">
                <h2 class="section-title">Performance Reflection</h2>
                <p class="section-description">
                    Rate your understanding and performance on these English skill-building activities. 
                    See how your peers felt and discover resources to help you improve!
                </p>
            </div>

            <div class="content-placeholder">
                <p>
<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .survey-container {
            background: rgba(113, 117, 193, 0.82);
            backdrop-filter: blur(20px);
            padding: 60px 50px;
            border-radius: 30px;
            max-width: 800px;
            width: 100%;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.4);
            position: relative;
            overflow: hidden;
            margin: 0 auto 40px;
        }

        .survey-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 8px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #4facfe);
            background-size: 300% 300%;
            animation: gradientShift 4s ease infinite;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .survey-header {
            text-align: center;
            margin-bottom: 45px;
        }

        .survey-header h2 {
            font-size: 2.5rem;
            background: #fff;
            background-clip: text;
            margin-bottom: 15px;
            font-weight: 800;
        }

        .survey-header p {
            color: #4a5568;
            font-size: 1.1rem;
            line-height: 1.7;
            animation: fadeIn 1s ease-out 0.3s backwards;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .rating-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(10px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }

        .rating-option {
            position: relative;
            cursor: pointer;
            animation: fadeInUp 0.6s ease-out backwards;
        }

        .rating-option:nth-child(1) { animation-delay: 0.1s; }
        .rating-option:nth-child(2) { animation-delay: 0.2s; }
        .rating-option:nth-child(3) { animation-delay: 0.3s; }
        .rating-option:nth-child(4) { animation-delay: 0.4s; }
        .rating-option:nth-child(5) { animation-delay: 0.5s; }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .rating-option input {
            display: none;
        }

        .rating-label {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px 15px;
            border: 3px solid #e2e8f0;
            border-radius: 20px;
            background: white;
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
            overflow: hidden;
        }

        .rating-label::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, #667eea, #764ba2);
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 0;
        }

        .rating-label > * {
            position: relative;
            z-index: 1;
        }

        .rating-number {
            font-size: 3rem;
            font-weight: 800;
            color: #667eea;
            transition: all 0.3s;
            margin-bottom: 10px;
        }

        .rating-text {
            font-size: 0.9rem;
            color: #718096;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s;
        }

        .rating-option:hover .rating-label {
            border-color: #667eea;
            transform: translateY(-8px) scale(1.05);
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        }

        .rating-option input:checked + .rating-label {
            border-color: #667eea;
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
            transform: scale(1.05);
        }

        .rating-option input:checked + .rating-label::before {
            opacity: 1;
        }

        .rating-option input:checked + .rating-label .rating-number,
        .rating-option input:checked + .rating-label .rating-text {
            color: white;
        }

        .submit-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 15px;
            font-size: 1.2rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            position: relative;
            overflow: hidden;
        }

        .submit-btn::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .submit-btn span {
            position: relative;
            z-index: 1;
        }

        .submit-btn:hover::before {
            opacity: 1;
        }

        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
        }

        .submit-btn:active {
            transform: translateY(-1px);
        }

        .submit-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            border-top-color: white;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Modal Styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 10000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: #31285cbc;
            backdrop-filter: blur(8px);
            animation: fadeIn 0.3s ease-out;
            overflow-y: auto;
        }

        .modal-content {
            background: #9281b3ff;
            margin: 3% auto;
            padding: 50px;
            border-radius: 30px;
            width: 90%;
            max-width: 700px;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.5);
            animation: slideInScale 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
        }

        @keyframes slideInScale {
            from {
                transform: translateY(-100px) scale(0.8);
                opacity: 0;
            }
            to {
                transform: translateY(0) scale(1);
                opacity: 1;
            }
        }

        .modal-close {
            position: absolute;
            right: 25px;
            top: 25px;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #f3f4f6;
            border: none;
            font-size: 24px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
            color: #4a5568;
        }

        .modal-close:hover {
            background: #e2e8f0;
            transform: rotate(90deg);
        }

        .result-badge {
            display: inline-block;
            padding: 12px 30px;
            border-radius: 50px;
            font-weight: 700;
            font-size: 1rem;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .badge-underprepared {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }

        .badge-average {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
        }

        .badge-overprepared {
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            color: white;
        }

        .result-title {
            font-size: 2.2rem;
            color: #1a202c;
            margin-bottom: 20px;
            font-weight: 800;
        }

        .result-message {
            font-size: 1.2rem;
            color: #4a5568;
            line-height: 1.8;
            margin-bottom: 35px;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 35px;
        }

        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
        }

        .stat-value {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .resources-section {
            background: #7973a8ff;
            padding: 30px;
            border-radius: 20px;
            margin-top: 30px;
            border: 2px solid #e2e8f0;
        }

        .resources-title {
            font-size: 1.5rem;
            color: #667eea;
            margin-bottom: 15px;
            font-weight: 700;
        }

        .resources-intro {
            color: #4a5568;
            margin-bottom: 20px;
            font-style: italic;
        }

        .resource-item {
            padding: 15px 20px;
            margin-bottom: 10px;
            background: #6768a3ff;
            border-radius: 10px;
            border-left: 4px solid #667eea;
            transition: all 0.3s;
        }

        .resource-item:hover {
            transform: translateX(8px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .resource-item a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            display: block;
        }

        .resource-item a:hover {
            color: #764ba2;
        }

        .modal-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 15px;
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 25px;
        }

        .modal-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }

        /* Admin View Styles */
        .admin-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 40px;
            border-radius: 30px;
            max-width: 1200px;
            width: 100%;
            margin: 40px auto;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.4);
        }

        .admin-header {
            margin-bottom: 30px;
            text-align: center;
        }

        .admin-header h2 {
            font-size: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        .ratings-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }

        .ratings-table th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.9rem;
            letter-spacing: 1px;
        }

        .ratings-table td {
            padding: 15px;
            border-bottom: 1px solid #e2e8f0;
            color: #4a5568;
        }

        .ratings-table tr:hover {
            background: #f7fafc;
        }

        .rating-badge {
            display: inline-block;
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 1.1rem;
        }

        .rating-1 { background: #fee; color: #c53030; }
        .rating-2 { background: #fef5e7; color: #d97706; }
        .rating-3 { background: #fef3c7; color: #b45309; }
        .rating-4 { background: #e0f2fe; color: #0369a1; }
        .rating-5 { background: #d1fae5; color: #047857; }

        .timestamp {
            font-size: 0.85rem;
            color: #718096;
        }

        .username-link {
            color: #667eea;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
            cursor: pointer;
        }

        .username-link:hover {
            color: #764ba2;
            text-decoration: underline;
        }

        .admin-stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        @media (max-width: 768px) {
            .survey-container {
                padding: 40px 30px;
            }

            .survey-header h2 {
                font-size: 2rem;
            }

            .rating-grid {
                grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
                gap: 15px;
            }

            .rating-number {
                font-size: 2.5rem;
            }

            .modal-content {
                padding: 35px 25px;
                width: 95%;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }

            .admin-container {
                padding: 20px;
            }

            .ratings-table {
                font-size: 0.85rem;
            }

            .ratings-table th,
            .ratings-table td {
                padding: 10px;
            }
        }
    </style>
<body>
    <div class="survey-container">
        <div class="survey-header">
            <h2>Performance Reflection</h2>
            <p>Rate your understanding and performance on the English skill building activities of media bias, thesis writing, and understanding citations. Let's see how your peers felt, and how you can improve next time.</p>
        </div>

        <form id="survey-form">
            <div class="rating-grid">
                <div class="rating-option">
                    <input type="radio" id="rating-1" name="rating" value="1">
                    <label for="rating-1" class="rating-label">
                        <span class="rating-number">1</span>
                        <span class="rating-text">Poor</span>
                    </label>
                </div>
                <div class="rating-option">
                    <input type="radio" id="rating-2" name="rating" value="2">
                    <label for="rating-2" class="rating-label">
                        <span class="rating-number">2</span>
                        <span class="rating-text">Fair</span>
                    </label>
                </div>
                <div class="rating-option">
                    <input type="radio" id="rating-3" name="rating" value="3">
                    <label for="rating-3" class="rating-label">
                        <span class="rating-number">3</span>
                        <span class="rating-text">Good</span>
                    </label>
                </div>
                <div class="rating-option">
                    <input type="radio" id="rating-4" name="rating" value="4">
                    <label for="rating-4" class="rating-label">
                        <span class="rating-number">4</span>
                        <span class="rating-text">Excellent</span>
                    </label>
                </div>
                <div class="rating-option">
                    <input type="radio" id="rating-5" name="rating" value="5">
                    <label for="rating-5" class="rating-label">
                        <span class="rating-number">5</span>
                        <span class="rating-text">Superior</span>
                    </label>
                </div>
            </div>

            <button type="submit" class="submit-btn" id="submit-btn">
                <span>Submit Rating</span>
            </button>
        </form>
    </div>

    <div id="results-modal" class="modal">
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            
            <div id="result-badge"></div>
            <h2 class="result-title" id="result-title"></h2>
            <p class="result-message" id="result-message"></p>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value" id="your-rating">-</div>
                    <div class="stat-label">Your Rating</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="class-avg">-</div>
                    <div class="stat-label">Class Average</div>
                </div>
            </div>

            <div class="resources-section">
                <h3 class="resources-title" id="resources-title"></h3>
                <p class="resources-intro" id="resources-intro"></p>
                <div id="resources-list"></div>
            </div>

            <button class="modal-btn" onclick="closeModal()">Got it, thanks!</button>
        </div>
    </div>

    <!-- Admin View (visible to admins only) -->
    <div class="admin-container" id="admin-section" style="display: none;">
        <div class="admin-header">
            <h2>📊 All Performance Ratings</h2>
        </div>

        <div class="admin-stats-grid" id="admin-stats-grid"></div>

        <table class="ratings-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Username</th>
                    <th>Rating</th>
                    <th>Timestamp</th>
                </tr>
            </thead>
            <tbody id="ratings-tbody"></tbody>
        </table>
    </div>

    <script>
        const API_BASE = 'http://localhost:8001/api';

        const resourcesByTier = {
            1: {
                title: 'Building Foundations',
                intro: 'Start with these fundamentals to strengthen your English skills:',
                items: [
                    { text: 'Grammarly Handbook - Grammar Basics', url: 'https://www.grammarly.com/blog/category/handbook/' },
                    { text: 'Khan Academy Grammar Course (Free)', url: 'https://www.khanacademy.org/humanities/grammar' },
                    { text: 'Basic Essay Structure (YouTube)', url: 'https://www.youtube.com/watch?v=sQEr5D1sSrU' },
                    { text: 'Purdue OWL - Writing Process Guide', url: 'https://owl.purdue.edu/owl/general_writing/the_writing_process/index.html' },
                    { text: 'Quizlet - Vocabulary Building', url: 'https://quizlet.com/subject/english-vocabulary/' }
                ]
            },
            2: {
                title: 'Developing Skills',
                intro: "You're on the right track! These resources will help you improve:",
                items: [
                    { text: 'MLA Citation Guide - Purdue OWL', url: 'https://owl.purdue.edu/owl/research_and_citation/mla_style/mla_formatting_and_style_guide/mla_formatting_and_style_guide.html' },
                    { text: 'Hemingway Editor - Improve Clarity', url: 'https://www.hemingwayapp.com/' },
                    { text: 'How to Write a Thesis Statement', url: 'https://www.youtube.com/watch?v=AzcJP7WS_5A' },
                    { text: 'UNC Writing Center - Essay Tips', url: 'https://writingcenter.unc.edu/tips-and-tools/' },
                    { text: 'Coursera - Academic English Writing (Free)', url: 'https://www.coursera.org/learn/writing-skills' }
                ]
            },
            3: {
                title: 'Solidifying Skills',
                intro: "You're right on track! Strengthen your skills with these:",
                items: [
                    { text: 'APA Format Guide - Research Papers', url: 'https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/general_format.html' },
                    { text: 'Thesaurus.com - Vocabulary Enhancement', url: 'https://www.thesaurus.com/' },
                    { text: 'Literary Analysis Techniques', url: 'https://www.youtube.com/watch?v=mhHfnhh-pB4' },
                    { text: 'Harvard Writing Center - Essay Strategies', url: 'https://writingcenter.fas.harvard.edu/pages/strategies-essay-writing' },
                    { text: 'edX - Advanced Grammar Course', url: 'https://www.edx.org/learn/english-grammar' }
                ]
            },
            4: {
                title: 'Advancing Excellence',
                intro: 'Great work! Take your skills to the next level:',
                items: [
                    { text: 'The New Yorker - Literary Journalism', url: 'https://www.newyorker.com/culture/culture-desk' },
                    { text: 'Literary Devices Guide - Advanced Analysis', url: 'https://literarydevices.net/' },
                    { text: 'Advanced Rhetorical Analysis', url: 'https://www.youtube.com/watch?v=QUF-5UDtRJs' },
                    { text: 'MLA Style Center - Advanced Citations', url: 'https://style.mla.org/' },
                    { text: 'MasterClass - Creative Writing (Paid)', url: 'https://www.masterclass.com/classes/margaret-atwood-teaches-creative-writing' }
                ]
            },
            5: {
                title: '🚀 Mastery Level',
                intro: 'Exceptional! Challenge yourself with these advanced resources:',
                items: [
                    { text: 'London Review of Books - Critical Essays', url: 'https://www.lrb.co.uk/' },
                    { text: 'JSTOR - Academic Research Database', url: 'https://www.jstor.org/' },
                    { text: 'Yale Lecture Series - Literary Theory', url: 'https://www.youtube.com/watch?v=8y8BXcjUNVU' },
                    { text: 'Chicago Manual of Style - Professional Writing', url: 'https://www.chicagomanualofstyle.org/home.html' },
                    { text: 'Poetry Foundation - Advanced Literary Forms', url: 'https://www.poets.org/poetsorg/text/learning-guide-poetry-terms' },
                    { text: 'Stanford Philosophy - Critical Thinking', url: 'https://philosophy.stanford.edu/teaching-guide' }
                ]
            }
        };

        // Check if user is authenticated and get their role
        async function checkAuth() {
            try {
                const response = await fetch(`${API_BASE}/id`, {
                    credentials: 'include'
                });
                
                if (response.ok) {
                    const userData = await response.json();
                    return userData;
                }
            } catch (error) {
                console.error('Auth check failed:', error);
            }
            return null;
        }

        // Load all performances (admin only)
        async function loadAllPerformances() {
            try {
                const response = await fetch(`${API_BASE}/performance`, {
                    credentials: 'include'
                });
                
                if (response.ok) {
                    const performances = await response.json();
                    displayAllPerformances(performances);
                    displayAdminStats(performances);
                }
            } catch (error) {
                console.error('Failed to load performances:', error);
            }
        }

        // Display all performances in table
        function displayAllPerformances(performances) {
            const tbody = document.getElementById('ratings-tbody');
            tbody.innerHTML = '';

            performances.reverse().forEach(perf => {
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${perf.id}</td>
                    <td><span class="username-link" onclick="showUserInfo(${perf.user_id}, '${perf.username}')">${perf.username || 'Guest'}</span></td>
                    <td><span class="rating-badge rating-${perf.rating}">${perf.rating}/5</span></td>
                    <td class="timestamp">${new Date(perf.timestamp).toLocaleString()}</td>
                `;
            });
        }

        // Display admin statistics
        function displayAdminStats(performances) {
            const statsGrid = document.getElementById('admin-stats-grid');
            
            const total = performances.length;
            const average = total > 0 
                ? (performances.reduce((sum, p) => sum + p.rating, 0) / total).toFixed(1)
                : 0;
            
            const distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0};
            performances.forEach(p => distribution[p.rating]++);
            const mostCommon = Object.entries(distribution)
                .sort((a, b) => b[1] - a[1])[0][0];

            statsGrid.innerHTML = `
                <div class="stat-card">
                    <div class="stat-value">${total}</div>
                    <div class="stat-label">Total Ratings</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">${average}</div>
                    <div class="stat-label">Average Rating</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">${mostCommon}</div>
                    <div class="stat-label">Most Common</div>
                </div>
            `;
        }

        // Show user info when clicking username
        window.showUserInfo = async function(userId, username) {
            try {
                const response = await fetch(`${API_BASE}/performance/user/${userId}`, {
                    credentials: 'include'
                });
                
                if (response.ok) {
                    const userPerfs = await response.json();
                    const totalRatings = userPerfs.length;
                    const avgRating = totalRatings > 0 
                        ? (userPerfs.reduce((sum, p) => sum + p.rating, 0) / totalRatings).toFixed(1)
                        : 0;
                    
                    const ratings = userPerfs.map(p => p.rating).join(', ');
                    
                    alert(`User: ${username}\nUser ID: ${userId}\n\nTotal Ratings: ${totalRatings}\nAverage Rating: ${avgRating}\nAll Ratings: ${ratings || 'None'}`);
                } else {
                    alert(`User: ${username}\nUser ID: ${userId}\n\nCould not load rating history.`);
                }
            } catch (error) {
                console.error('Error loading user info:', error);
                alert(`User: ${username}\nUser ID: ${userId}\n\nError loading rating history.`);
            }
        }

        document.getElementById('survey-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const rating = document.querySelector('input[name="rating"]:checked');
            if (!rating) {
                alert('Please select a rating before submitting.');
                return;
            }

            const submitBtn = document.getElementById('submit-btn');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<div class="loading"></div>';

            try {
                const response = await fetch(`${API_BASE}/performance/submit`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    body: JSON.stringify({ rating: parseInt(rating.value) })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    showResults(data);
                    
                    // Reload admin view if visible
                    if (document.getElementById('admin-section').style.display !== 'none') {
                        loadAllPerformances();
                    }
                } else {
                    alert('Error: ' + (data.error || 'Unknown error occurred'));
                }
            } catch (error) {
                alert('Failed to submit. Please ensure you are logged in and your Flask server is running on port 8001.');
                console.error(error);
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<span>Submit Rating</span>';
            }
        });

        function showResults(data) {
            const badgeColors = {
                'underprepared': 'badge-underprepared',
                'average': 'badge-average',
                'overprepared': 'badge-overprepared'
            };

            const titles = {
                'underprepared': "Let's Build Your Skills!",
                'overprepared': 'Excellent Work!',
                'average': "You're On Track!"
            };

            document.getElementById('result-badge').innerHTML = 
                `<span class="result-badge ${badgeColors[data.status]}">${data.status.toUpperCase()}</span>`;
            document.getElementById('result-title').textContent = titles[data.status] || 'Your Results';
            document.getElementById('result-message').textContent = data.message;
            document.getElementById('your-rating').textContent = data.your_rating;
            document.getElementById('class-avg').textContent = data.average_rating;

            const resources = resourcesByTier[data.your_rating];
            document.getElementById('resources-title').textContent = resources.title;
            document.getElementById('resources-intro').textContent = resources.intro;
            
            const resourcesList = document.getElementById('resources-list');
            resourcesList.innerHTML = resources.items.map(item => 
                `<div class="resource-item">
                    <a href="${item.url}" target="_blank">${item.text}</a>
                </div>`
            ).join('');

            document.getElementById('results-modal').style.display = 'block';
        }

        function closeModal() {
            document.getElementById('results-modal').style.display = 'none';
        }

        window.onclick = function(event) {
            const modal = document.getElementById('results-modal');
            if (event.target === modal) {
                closeModal();
            }
        }

        // Initialize page
        window.addEventListener('DOMContentLoaded', async () => {
            const user = await checkAuth();
            
            if (user) {
                console.log('User logged in:', user.uid, 'Role:', user.role);
                
                // Show admin section if user is admin
                if (user.role === 'Admin') {
                    document.getElementById('admin-section').style.display = 'block';
                    loadAllPerformances();
                }
            } else {
                console.log('No user logged in');
            }
        });
    </script>
</body>
</p>
                <p style="margin-top: 20px; font-size: 0.9rem;">
                </p>
            </div>

            <div class="navigation-buttons">
                <button class="nav-btn nav-btn-prev" onclick="prevSection()">
                    ← Previous
                </button>
                <button class="nav-btn nav-btn-next" disabled>
                    Complete ✓
                </button>
            </div>
        </div>
    </div>

    <script>
        let currentSection = 1;
        const totalSections = 4;

        function updateProgress() {
            // Update step indicators
            document.querySelectorAll('.step').forEach((step, index) => {
                const stepNum = index + 1;
                step.classList.remove('active', 'completed');
                
                if (stepNum < currentSection) {
                    step.classList.add('completed');
                } else if (stepNum === currentSection) {
                    step.classList.add('active');
                }
            });

            // Update progress line
            const progressPercent = ((currentSection - 1) / (totalSections - 1)) * 100;
            document.getElementById('progress-fill').style.width = progressPercent + '%';

            // Show/hide sections
            document.querySelectorAll('.section-container').forEach((section, index) => {
                section.classList.remove('active');
                if (index + 1 === currentSection) {
                    section.classList.add('active');
                }
            });

            // Scroll to top smoothly
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function nextSection() {
            if (currentSection < totalSections) {
                currentSection++;
                updateProgress();
            }
        }

        function prevSection() {
            if (currentSection > 1) {
                currentSection--;
                updateProgress();
            }
        }

        // Allow direct navigation by clicking steps
        document.querySelectorAll('.step').forEach((step) => {
            step.addEventListener('click', function() {
                const targetStep = parseInt(this.dataset.step);
                // Only allow going to completed or current step
                if (targetStep <= currentSection) {
                    currentSection = targetStep;
                    updateProgress();
                }
            });
        });

        // Initialize
        updateProgress();
    </script>
</body>
</html>