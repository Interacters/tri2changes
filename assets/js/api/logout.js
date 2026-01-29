import { pythonURI, fetchOptions } from './config.js';

export async function handleLogout() {
    console.log("🚪 Logging out...");
    
    try {
        const response = await fetch(pythonURI + '/api/authenticate', {
            ...fetchOptions,
            method: 'DELETE',
            credentials: 'include' // Important!
        });
        
        console.log("📊 Logout response status:", response.status);
        
        if (response.ok) {
            console.log("✅ Logout successful");
            
            // Clear any local storage/session storage
            localStorage.clear();
            sessionStorage.clear();
            
            // Force page reload to clear any cached state
            window.location.reload();
            return true;
        } else {
            console.error('❌ Logout failed:', response.status);
            const data = await response.json().catch(() => ({}));
            console.error('Error details:', data);
            
            // Still clear local storage and reload even if backend fails
            localStorage.clear();
            sessionStorage.clear();
            window.location.reload();
            return false;
        }
        
    } catch (e) {
        console.error('❌ Logout request failed:', e);
        
        // Clear storage and reload even on error
        localStorage.clear();
        sessionStorage.clear();
        window.location.reload();
        return false;
    }
}