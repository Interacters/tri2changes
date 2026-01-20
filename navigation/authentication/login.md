---
layout: page
title: Login
permalink: /login
search_exclude: true
show_reading_time: false
---
<style>
    .submit-button {
        width: 100%;
        transition: all 0.3s ease;
        position: relative;
    }
    .login-container {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 20px;
        flex-wrap: nowrap;
    }

    .login-card,
    .signup-card {
        flex: 1 1 calc(50% - 20px);
        max-width: 45%;
        box-sizing: border-box;
        background: #1e1e1e;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        padding: 20px;
        color: white;
        overflow: hidden;
    }

    .login-card h1 {
        margin-bottom: 20px;
    }

    .signup-card h1 {
        margin-bottom: 20px;
    }

    .form-group {
        position: relative;
        margin-bottom: 1.5rem;
    }

    input {
        width: 100%;
        box-sizing: border-box;
    }
</style>
<br>
<div class="login-container">
    <!-- Python Login Form -->
    <div class="login-card">
        <h1 id="pythonTitle">User Login</h1>
        <hr>
        <form id="pythonForm" onsubmit="pythonLogin(); return false;">
            <div class="form-group">
                <input type="text" id="uid" placeholder="GitHub ID" required>
            </div>
            <div class="form-group">
                <input type="password" id="password" placeholder="Password" required>
            </div>
            <p>
                <button type="submit" class="large primary submit-button">Login</button>
            </p>
            <p id="message" style="color: red;"></p>
        </form>
    </div>
    <div class="signup-card">
        <h1 id="signupTitle">Sign Up</h1>
        <hr>
        <form id="signupForm" onsubmit="signup(); return false;">
            <div class="form-group">
                <input type="text" id="name" placeholder="Name" required>
            </div>
            <div class="form-group">
                <input type="text" id="signupUid" placeholder="GitHub ID" required>
            </div>
            <div class="form-group">
                <input type="text" id="signupSid" placeholder="Student ID" required>
            </div>
            <div class="form-group">
                <input type="text" id="signupEmail" placeholder="Email" required>
            </div>
            <div class="form-group">
                <input type="password" id="signupPassword" placeholder="Password" required>
            </div>
            <p>
                <label class="switch">
                    <span class="toggle">
                        <input type="checkbox" name="kasmNeeded" id="kasmNeeded">
                        <span class="slider"></span>
                    </span>
                    <span class="label-text">Kasm Server Needed</span>
                </label>
            </p>
            <p>
                <button type="submit" class="large primary submit-button">Sign Up</button>
            </p>
            <p id="signupMessage" style="color: green;"></p>
        </form>
    </div>
</div>
<script type="module">
    import { login, pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

window.pythonLogin = async function () {
    const uid = document.getElementById("uid").value;
    const password = document.getElementById("password").value;
    
    if (!uid || !password) {
        document.getElementById("message").textContent = "Please enter both username and password";
        return;
    }
    
    try {
        const response = await fetch(`${pythonURI}/api/authenticate`, {
            method: 'POST',
            mode: 'cors',
            credentials: 'include',  // CRITICAL: This allows cookies to be set
            headers: {
                'Content-Type': 'application/json',
                'X-Origin': 'client'
            },
            body: JSON.stringify({ uid, password })
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            document.getElementById("message").textContent = errorData.message || `Login failed: ${response.status}`;
            return;
        }
        
        // Wait for the response to complete (cookie is set now)
        const data = await response.json();
        console.log("Login successful:", data);
        
        // Small delay to ensure cookie is fully set
        await new Promise(resolve => setTimeout(resolve, 100));
        
        // Now verify the session is active
        const verifyResponse = await fetch(`${pythonURI}/api/id`, {
            method: 'GET',
            mode: 'cors',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-Origin': 'client'
            }
        });
        
        if (verifyResponse.ok) {
            // Session verified, redirect to profile
            window.location.href = '{{site.baseurl}}/profile';
        } else {
            throw new Error('Session verification failed');
        }
        
    } catch (error) {
        console.error("Login error:", error);
        document.getElementById("message").textContent = `Error: ${error.message}`;
    }
}

    // Function to fetch and display Python data
    function pythonDatabase() {
        const URL = `${pythonURI}/api/id`;
        fetch(URL, fetchOptions)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Flask server response: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                window.location.href = '{{site.baseurl}}/profile';
            })
            .catch(error => {
                document.getElementById("message").textContent = `Error: ${error.message}`;
            });
    }

    window.signup = function () {
        const signupButton = document.querySelector(".signup-card button");
        // Disable the button and change its color
        signupButton.disabled = true;
        signupButton.classList.add("disabled");

        const signupOptions = {
            URL: `${pythonURI}/api/user`,
            method: "POST",
            cache: "no-cache",
            body: {
                name: document.getElementById("name").value,
                uid: document.getElementById("signupUid").value,
                email: document.getElementById("signupEmail").value,
                password: document.getElementById("signupPassword").value,
                kasm_server_needed: document.getElementById("kasmNeeded").checked,
            }
        };

        fetch(signupOptions.URL, {
            method: signupOptions.method,
            headers: {
                "Content-Type": "application/json"
            },
            credentials: "include",
            body: JSON.stringify(signupOptions.body)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Signup failed: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                document.getElementById("signupMessage").textContent = "Signup successful!";
                // Optionally auto-login or redirect
                setTimeout(() => {
                    window.location.href = '{{site.baseurl}}/login';
                }, 1500);
            })
            .catch(error => {
                console.error("Signup Error:", error);
                document.getElementById("signupMessage").style.color = "red";
                document.getElementById("signupMessage").textContent = `Signup Error: ${error.message}`;
                // Re-enable the button if there is an error
                signupButton.disabled = false;
                signupButton.classList.remove("disabled");
            });
    }
</script>