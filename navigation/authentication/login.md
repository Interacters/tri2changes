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
        /* Use flexbox for side-by-side layout */
        justify-content: space-between;
        /* Add space between the cards */
        align-items: flex-start;
        /* Align items to the top */
        gap: 20px;
        /* Add spacing between the cards */
        flex-wrap: nowrap;
        /* Prevent wrapping of the cards */
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
        <form id="pythonForm" onsubmit="loginBoth(); return false;">
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
    import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

    // Function to handle Python login
    window.pythonLogin = async function () {
        const uid = document.getElementById("uid").value;
        const password = document.getElementById("password").value;
        
        if (!uid || !password) {
            document.getElementById("message").textContent = "Please enter both username and password";
            return;
        }
        
        try {
            console.log("🔐 Attempting login...");
            const response = await fetch(`${pythonURI}/api/authenticate`, {
                method: 'POST',
                mode: 'cors',
                credentials: 'include',
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
            
            const data = await response.json();
            console.log("✅ Login successful:", data);
            
            // Wait for cookie to be set
            await new Promise(resolve => setTimeout(resolve, 500));
            
            // Verify session
            console.log("🔍 Verifying session...");
            const verifyResponse = await fetch(`${pythonURI}/api/id`, {
                method: 'GET',
                mode: 'cors',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Origin': 'client'
                }
            });
            
            console.log("📊 Verify status:", verifyResponse.status);
            
            if (verifyResponse.ok) {
                console.log("✅ Session verified, redirecting...");
                window.location.href = '{{site.baseurl}}/profile';
            } else {
                const errorData = await verifyResponse.json().catch(() => ({}));
                throw new Error(`Session verification failed: ${errorData.message || verifyResponse.status}`);
            }
            
        } catch (error) {
            console.error("❌ Login error:", error);
            document.getElementById("message").textContent = `Error: ${error.message}`;
        }
    }

    window.signup = async function () {
        const signupButton = document.querySelector(".signup-card button");
        signupButton.disabled = true;
        signupButton.classList.add("disabled");

        try {
            const response = await fetch(`${pythonURI}/api/user`, {
                method: "POST",
                mode: 'cors',
                credentials: "include",
                headers: {
                    "Content-Type": "application/json",
                    "X-Origin": "client"
                },
                body: JSON.stringify({
                    name: document.getElementById("name").value,
                    uid: document.getElementById("signupUid").value,
                    email: document.getElementById("signupEmail").value,
                    password: document.getElementById("signupPassword").value,
                    kasm_server_needed: document.getElementById("kasmNeeded").checked,
                })
            });
            
            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.message || `Signup failed: ${response.status}`);
            }
            
            document.getElementById("signupMessage").textContent = "Signup successful!";
            document.getElementById("signupMessage").style.color = "green";
            
            setTimeout(() => {
                window.location.href = '{{site.baseurl}}/login';
            }, 1500);
            
        } catch (error) {
            console.error("Signup Error:", error);
            document.getElementById("signupMessage").style.color = "red";
            document.getElementById("signupMessage").textContent = `Signup Error: ${error.message}`;
            signupButton.disabled = false;
            signupButton.classList.remove("disabled");
        }
    }
</script>