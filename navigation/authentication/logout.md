---
layout: opencs
title: Logout
permalink: /logout
search_exclude: True
---

<style>
    body {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        background: linear-gradient(to bottom, #0f172a, #1e293b);
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    .logout-message {
        text-align: center;
        padding: 2rem;
    }
</style>

<div class="logout-message">
    <h2>Logging out...</h2>
    <p>Please wait...</p>
</div>

<script type="module">
    import { handleLogout } from '{{site.baseurl}}/assets/js/api/logout.js';
    
    (async () => {
        console.log("🚪 Logout page loaded");
        
        // Perform logout
        await handleLogout();
        
        // Wait a moment to ensure cookies are cleared
        await new Promise(resolve => setTimeout(resolve, 500));
        
        console.log("🔄 Redirecting to login...");
        
        // Redirect to login page
        window.location.href = "{{site.baseurl}}/login";
    })();
</script>