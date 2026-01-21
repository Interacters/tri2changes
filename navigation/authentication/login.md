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