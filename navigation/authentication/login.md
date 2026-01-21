---
layout: page
title: Login
permalink: /login
search_exclude: true
show_reading_time: false
---
<style>
    :root {
        --primary: #2563eb;
        --primary-dark: #1e40af;
        --primary-light: #3b82f6;
        --secondary: #0891b2;
        --success: #059669;
        --danger: #dc2626;
        --warning: #d97706;
        --dark: #111827;
        --gray-50: #f9fafb;
        --gray-100: #f3f4f6;
        --gray-200: #e5e7eb;
        --gray-300: #d1d5db;
        --gray-600: #4b5563;
        --gray-700: #374151;
        --gray-800: #1f2937;
        --gray-900: #111827;
    }

    body {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
        min-height: 100vh;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }

    .login-container {
        display: flex;
        gap: 2rem;
        max-width: 1200px;
        width: 100%;
    }

    .login-card,
    .signup-card {
        flex: 1;
        background: #c9c9f5;
        border-radius: 12px;
        padding: 2.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .login-card:hover,
    .signup-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .login-card h1,
    .signup-card h1 {
        font-size: 2rem;
        font-weight: 700;
        color: var(--gray-900);
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.025em;
    }

    hr {
        border: none;
        height: 2px;
        background: var(--primary);
        margin: 0 0 2rem 0;
        border-radius: 2px;
    }

    .form-group {
        margin-bottom: 1.5rem;
    }

    input[type="text"],
    input[type="password"],
    input[type="email"] {
        width: 100%;
        padding: 0.75rem 1rem;
        border: 2px solid var(--gray-200);
        border-radius: 8px;
        font-size: 0.95rem;
        transition: all 0.2s ease;
        background: white;
        color: var(--gray-900);
        box-sizing: border-box;
    }

    input[type="text"]:focus,
    input[type="password"]:focus,
    input[type="email"]:focus {
        outline: none;
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }

    input::placeholder {
        color: var(--gray-600);
    }

    .switch {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 1.5rem;
    }

    .toggle {
        position: relative;
        display: inline-block;
        width: 50px;
        height: 26px;
    }

    .toggle input {
        opacity: 0;
        width: 0;
        height: 0;
    }

    .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: var(--gray-300);
        transition: 0.3s;
        border-radius: 34px;
    }

    .slider:before {
        position: absolute;
        content: "";
        height: 20px;
        width: 20px;
        left: 3px;
        bottom: 3px;
        background-color: white;
        transition: 0.3s;
        border-radius: 50%;
    }

    input:checked + .slider {
        background-color: var(--primary);
    }

    input:checked + .slider:before {
        transform: translateX(24px);
    }

    .label-text {
        color: var(--gray-700);
        font-weight: 500;
        font-size: 0.9rem;
    }

    button[type="submit"] {
        width: 100%;
        padding: 0.875rem 1.5rem;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
        background: var(--primary);
        color: white;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }

    button[type="submit"]:hover {
        background: var(--primary-dark);
        transform: translateY(-1px);
        box-shadow: 0 6px 8px rgba(37, 99, 235, 0.3);
    }

    button[type="submit"]:active {
        transform: translateY(0);
    }

    button[type="submit"]:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        transform: none;
    }

    #message,
    #signupMessage {
        margin-top: 1rem;
        padding: 0.75rem 1rem;
        border-radius: 6px;
        font-weight: 500;
        text-align: center;
        font-size: 0.9rem;
    }

    #message {
        background: #fee2e2;
        color: var(--danger);
        border: 1px solid #fecaca;
    }

    #signupMessage {
        background: #dcfce7;
        color: var(--success);
        border: 1px solid #bbf7d0;
    }

    #signupMessage.error {
        background: #fee2e2;
        color: var(--danger);
        border: 1px solid #fecaca;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .login-container {
            flex-direction: column;
        }

        .login-card,
        .signup-card {
            max-width: 100%;
        }
    }
</style>

<div class="login-container">
    <!-- Login Form -->
    <div class="login-card">
        <h1>User Login</h1>
        <hr>
        <form id="pythonForm" onsubmit="pythonLogin(); return false;">
            <div class="form-group">
                <input type="text" id="uid" placeholder="GitHub ID" required>
            </div>
            <div class="form-group">
                <input type="password" id="password" placeholder="Password" required>
            </div>
            <button type="submit" class="large primary submit-button">Login</button>
            <p id="message" style="display: none;"></p>
        </form>
    </div>

    <!-- Signup Form -->
    <div class="signup-card">
        <h1>Sign Up</h1>
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
                <input type="email" id="signupEmail" placeholder="Email" required>
            </div>
            <div class="form-group">
                <input type="password" id="signupPassword" placeholder="Password" required>
            </div>
            <label class="switch">
                <span class="toggle">
                    <input type="checkbox" name="kasmNeeded" id="kasmNeeded">
                    <span class="slider"></span>
                </span>
                <span class="label-text">Kasm Server Needed</span>
            </label>
            <button type="submit" class="large primary submit-button">Sign Up</button>
            <p id="signupMessage" style="display: none;"></p>
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
        console.log("🔐 Attempting login for user:", uid);
        
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
        console.log("✅ Server response:", data);
        
        // ✅ ADDED: Check if cookie was set
        const cookieName = 'jwt_python_flask'; // Should match JWT_TOKEN_NAME
        const cookies = document.cookie.split(';').map(c => c.trim());
        const jwtCookie = cookies.find(c => c.startsWith(cookieName + '='));
        
        if (jwtCookie) {
            console.log("✅ Cookie found:", cookieName);
        } else {
            console.warn("⚠️ Cookie not found in document.cookie (may be HttpOnly)");
        }
        
        // Wait for cookie to be fully set
        await new Promise(resolve => setTimeout(resolve, 1000));
        
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
        
        console.log("📊 Verify response status:", verifyResponse.status);
        
        if (verifyResponse.ok) {
            const userData = await verifyResponse.json();
            console.log("✅ Session verified for:", userData.name);
            console.log("🎉 Redirecting to profile...");
            window.location.href = '{{site.baseurl}}/profile';
        } else {
            const errorText = await verifyResponse.text();
            console.error("❌ Session verification failed:", errorText);
            document.getElementById("message").textContent = "Login succeeded but session verification failed. Please try again.";
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