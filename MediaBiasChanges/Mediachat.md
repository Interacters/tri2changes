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
        const response = await fetch(pythonURI + '/api/media/leaderboard?limit=5');
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
</script>