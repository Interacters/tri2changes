<style>
    /* Floats the help popover to the right of whatever card it is nested inside. Absolute positioning lets it escape normal flow without shifting other elements. */
    .help-popover {
        position: absolute;
        top: 0;
        left: 100%;           /* anchors to the right edge of the parent card */
        width: 280px;
        background: rgba(15, 23, 42, 0.95);
        color: #e2e8f0;
        border: 1px solid rgba(148, 163, 184, 0.35);
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.6);
        display: none;        /* hidden until the .show class is added via JS */
        z-index: 9999;        /* stays on top of all other page content */
        margin-left: 16px;    /* gap between the card edge and the popover */
    }

    /* Adding .show switches display back on and plays the entrance animation */
    .help-popover.show {
        display: block;
        animation: popIn 0.25s ease;
    }

    /* Fades the popover in while nudging it upward from a slightly lower start position */
    @keyframes popIn {
        from {
            opacity: 0;
            transform: translateY(8px) scale(0.98);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    /* Bright title text so it stands out against the dark panel background */
    .help-popover-title {
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 6px;
        font-size: 1rem;
    }

    /* Softer body copy that describes what the primary button will do */
    .help-popover-text {
        font-size: 0.9rem;
        color: #cbd5e1;
        margin: 0 0 12px;
    }

    /* Flex row that places the two action buttons side by side */
    .help-popover-actions {
        display: flex;
        gap: 8px;
    }

    /* Shared base for both action buttons inside the popover */
    .help-popover-btn {
        flex: 1;              /* both buttons share the row width equally */
        padding: 10px 12px;
        border-radius: 10px;
        border: 1px solid transparent;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    /* Filled blue button draws the eye to the primary action */
    .help-popover-btn.primary {
        background: #60a5fa;
        color: #0f172a;       /* dark text for contrast on the light blue fill */
        box-shadow: 0 8px 18px rgba(96, 165, 250, 0.35);
    }

    /* Transparent ghost button signals a secondary / dismissal option */
    .help-popover-btn.ghost {
        background: transparent;
        color: #e2e8f0;
        border-color: rgba(148, 163, 184, 0.4);
    }

    /* Both buttons lift slightly on hover to feel clickable */
    .help-popover-btn:hover {
        transform: translateY(-1px);
    }

    /* When the popover is used next to the chat panel it mirrors to the left */
    .help-popover.chat {
        left: auto;
        right: 100%;          /* now anchors to the left edge of the parent */
        margin-left: 0;
        margin-right: 16px;
    }

    /* Both card types need overflow:visible so the absolute popover is not clipped */
    .ai-card {
        position: relative;
        overflow: visible;
    }

    .source-selection {
        position: relative;
        overflow: visible;
    }

    /* Below 1100px there is no room for the popover to float beside the card, so it drops back into normal document flow and stacks underneath */
    @media (max-width: 1100px) {
        .help-popover {
            position: relative;
            left: auto;
            top: auto;
            width: 100%;
            margin: 12px 0 0;
        }
    }

    /* Spacing wrapper around the spectrum intro content */
    .media-spectrum-intro {
        margin-bottom: 30px;
    }

    /* Horizontal gradient bar that visualizes the left-to-right bias scale */
    .spectrum-bar {
        height: 12px;
        background: linear-gradient(to right, #3b82f6, #94a3b8, #ef4444); /* blue > grey > red */
        border-radius: 10px;
        margin: 20px 0;
    }

    /* Pill-shaped button that collapses or expands the bias info section */
    .spectrum-toggle-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        padding: 12px 20px;
        background: rgba(15, 23, 42, 0.8);
        border: 2px solid #94a3b8;
        border-radius: 16px;
        color: #afb3e8;
        font-size: 1.2rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-bottom: 20px;
        user-select: none;    /* stops the label being accidentally selected */
    }

    /* Blue border on hover signals the button is interactive */
    .spectrum-toggle-btn:hover {
        background: rgba(15, 23, 42, 0.95);
        border-color: #60a5fa;
    }

    /* Arrow icon that rotates smoothly when the section opens or closes */
    .spectrum-collapse-icon {
        font-size: 1.2rem;
        transition: transform 0.3s ease;
    }

    /* Pointing left shows the section is currently closed */
    .spectrum-collapse-icon.collapsed {
        transform: rotate(-90deg);
    }

    /* Animates height and opacity so the collapse feels smooth rather than instant */
    #bias-info-box {
        max-height: 2000px;   /* tall enough to always fit all content when open */
        overflow: hidden;
        transition: max-height 0.5s ease, opacity 0.4s ease, margin 0.3s ease;
        opacity: 1;
        margin-bottom: 30px;
    }

    /* Collapsing zeroes out height, opacity, and margin so no empty gap remains */
    #bias-info-box.collapsed {
        max-height: 0;
        opacity: 0;
        margin-bottom: 0;
        padding-top: 0;
        padding-bottom: 0;
    }
</style>

<!-- Toggle button lives outside the collapsible box so it stays visible even when the box is hidden, giving the user a way to reopen it -->
<div class="spectrum-toggle-btn" id="spectrum-toggle">
    <span>Click Here to See Spectrum of Bias</span>
    <span class="spectrum-collapse-icon" id="spectrum-icon">&#9660;</span>
</div>

<!-- Dark panel holding the bias spectrum explorer. Starts fully expanded; collapses when the toggle above is clicked. -->
<div id="bias-info-box" style="background: rgba(15, 23, 42, 0.8); border: 2px solid #94a3b8; border-radius: 16px; padding: 10px; transition: all 0.3s;">
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
            <!-- Slider starts at 50 so the page loads showing Center/Neutral -->
            <div style="position: relative; margin: 30px 0;">
                <input type="range" min="0" max="100" value="50"
                       id="bias-slider"
                       style="width: 100%; height: 8px; border-radius: 5px; background: rgba(148, 163, 184, 0.3); outline: none; cursor: pointer;">
            </div>
            <div style="text-align: center;">
                <div style="font-size: 4rem; margin-bottom: 15px;" id="bias-emoji">&#x1318D;</div>
                <h4 style="color: #94a3b8; font-size: 1.5rem; margin-bottom: 15px;" id="bias-title">Center/Neutral</h4>
                <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.8;" id="bias-description">
                    Focuses on factual reporting with minimal editorial opinion, presenting multiple viewpoints.
                </p>
                <div style="margin-top: 20px; padding: 15px; background: rgba(148, 163, 184, 0.1); border-radius: 10px;">
                    <p style="color: #60a5fa; font-weight: 700; margin-bottom: 8px;" id="bias-key">Key Characteristics:</p>
                    <p style="color: #e2e8f0; font-size: 0.9rem;" id="bias-traits">
                        Fact-based headlines<br>
                        Multiple perspectives<br>
                        Minimal opinion language
                    </p>
                </div>
            </div>
        </div>
    </div>

    <div style="background: rgba(168, 85, 247, 0.1); border: 1px solid rgba(168, 85, 247, 0.3); padding: 20px; border-radius: 12px; margin-top: 25px;">
        <h4 style="color: #a78bfa; margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
            Pro Tip
        </h4>
        <p style="color: #e2e8f0; line-height: 1.6;">
            <strong>No source is 100% unbiased.</strong> Do not strive for perfection. Just consider the value each source brings. Smart readers consume multiple viewpoints to have a well rounded opinion.
        </p>
    </div>
</div>

<script>
    // Wrap the slider and collapse logic in an IIFE so no variable names here bleed into the global scope and clash with the game scripts below
    (function() {

        // Cache the slider element once at startup so we are not querying the DOM on every event
        const biasSlider = document.getElementById('bias-slider');

        // Lookup table keyed by the five slider positions: 0, 25, 50, 75, 100.
        // Each entry holds all the content the info panel needs to show for that position.
        const biasData = {
            0: {
                emoji: 'warning',
                title: 'Far Left',
                color: '#1e40af',
                description: 'Strong progressive advocacy. Often focuses on social justice, wealth inequality, and systemic change. May use passionate language to drive urgency.',
                traits: 'Advocacy journalism<br>Social justice focus<br>Bold reform proposals'
            },
            25: {
                emoji: 'speaker',
                title: 'Left-Leaning',
                color: '#3b82f6',
                description: 'Generally supports progressive policies like environmental regulation, social programs, and diversity initiatives. Frames stories with these values in mind.',
                traits: 'Progressive values<br>Government solutions<br>Social equity emphasis'
            },
            50: {
                emoji: 'scale',
                title: 'Center/Neutral',
                color: '#94a3b8',
                description: 'Focuses on factual reporting with minimal editorial opinion, presenting multiple viewpoints. Prioritizes verifiable information over interpretation.',
                traits: 'Fact-based headlines<br>Multiple perspectives<br>Minimal opinion language'
            },
            75: {
                emoji: 'mic',
                title: 'Right-Leaning',
                color: '#ef4444',
                description: 'Generally supports conservative values like free markets, limited government, and traditional institutions. Stories emphasize these principles.',
                traits: 'Conservative values<br>Market solutions<br>Traditional institutions'
            },
            100: {
                emoji: 'warning',
                title: 'Far Right',
                color: '#a01414',
                description: 'Strong conservative advocacy. Often focuses on individual liberty, national sovereignty, and traditional values. May use passionate language about cultural issues.',
                traits: 'Advocacy journalism<br>Nationalist focus<br>Traditional values defense'
            }
        };

        // Only attach the listener if the slider element actually exists on the page
        if (biasSlider) {

            // Fire on every incremental movement so the panel updates while dragging, not only when the user releases the thumb
            biasSlider.addEventListener('input', function() {

                // Convert the raw string from the input to a real integer
                const value = parseInt(this.value, 10);

                // Start the nearest-key search from position 50 (Center) as a safe default
                let closestKey = 50;
                let minDiff = Math.abs(value - 50);

                // Walk every defined key and remember whichever sits closest to the slider value
                Object.keys(biasData).forEach(key => {
                    const diff = Math.abs(value - parseInt(key, 10));
                    if (diff < minDiff) {
                        minDiff = diff;
                        closestKey = key;
                    }
                });

                // Pull the content block for the winning position
                const data = biasData[closestKey];

                // Get a reference to the outer box so we can recolor its border below
                const infoBox = document.getElementById('bias-info-box');

                // Update every dynamic element in the panel to match the selected position
                document.getElementById('bias-emoji').textContent       = data.emoji;
                document.getElementById('bias-title').textContent       = data.title;
                document.getElementById('bias-title').style.color       = data.color;
                document.getElementById('bias-description').textContent = data.description;
                document.getElementById('bias-traits').innerHTML        = data.traits;

                // Tint the box border to reinforce which end of the spectrum is active
                infoBox.style.borderColor = data.color;
            });
        }

        // Grab all three elements involved in the collapse toggle before wiring any events
        const toggleBtn = document.getElementById('spectrum-toggle');
        const box       = document.getElementById('bias-info-box');
        const icon      = document.getElementById('spectrum-icon');

        // Guard against any element being absent from the DOM before attaching the listener
        if (toggleBtn && box && icon) {
            toggleBtn.addEventListener('click', function() {
                // Toggle the collapsed class on the box to animate it open or shut
                box.classList.toggle('collapsed');

                // Rotate the arrow icon in sync with the box open/close state
                icon.classList.toggle('collapsed');
            });
        }

    })();
</script>

<div class="content-placeholder">
    <p>

<style>
/* Zero out default browser margin and padding so layout measurements are exact */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Page-level background color and padding that surrounds all content */
body {
    min-height: 100vh;
    background-size: cover;
    background-color: #9393c7;
    padding: 20px;
}

/* Constrain the content width and center it horizontally on wide screens */
.page-content {
    max-width: 1800px;
    margin: 0 auto;
}

/* Semi-transparent dark card for blocks of introductory text */
.intro-text {
    background: rgba(0, 0, 30, 0.85);
    padding: 20px;
    border-radius: 12px;
    font-family: "Inter", system-ui, sans-serif;
    font-size: 1.05rem;
    margin-bottom: 20px;
    line-height: 1.5;
    color: #e2e8f0;
}

/* Outer card that wraps the game header, bins, image tray, controls, and leaderboard */
.game-container {
    background: #a7a0d4;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin: 20px 0;
    font-family: system-ui, -apple-system, sans-serif;
}

/* Top bar of the game holding the player info pills and the auth button */
.game-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid rgba(255, 255, 255, 0.5);
}

/* Groups the player name and timer badges into a flex row */
.player-info {
    display: flex;
    gap: 20px;
    align-items: center;
}

/* Rounded badge used for the player name and elapsed time displays */
.info-pill {
    background: rgba(255, 255, 255, 0.5);
    padding: 8px 15px;
    border-radius: 20px;
    font-weight: 600;
    color: #2c5282;
}

/* Side-by-side row of three drop targets, each taking equal width */
.bins-container {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin: 20px 0;
}

/* Individual drop bin; dashed border makes it obvious cards can land here */
.bin {
    flex: 1;
    min-height: 150px;
    background: rgba(255, 255, 255, 0.4);
    border: 2px dashed #4299e1;
    border-radius: 10px;
    padding: 15px;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Visual feedback applied while a dragged card hovers over the bin */
.bin.highlight {
    background: rgba(255, 255, 255, 0.6);
    border-color: #2b6cb0;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(66, 153, 225, 0.2);
}

/* Text label at the top of each bin */
.bin-label {
    font-weight: 600;
    color: #2c5282;
    margin-bottom: 10px;
}

/* Tray that holds the shuffled source logo cards before they are sorted */
.images-area {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
    min-height: 100px;
}

/* Individual draggable source logo card */
.image {
    width: 80px;
    height: 80px;
    padding: 8px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    cursor: grab;
    transition: transform 0.2s ease, opacity 0.2s ease;
}

/* Slight upward nudge on hover hints the card is draggable */
.image:hover {
    transform: translateY(-2px);
}

/* While dragging, the card turns semi-transparent so the bin beneath is visible */
.image.dragging {
    opacity: 0.5;
    transform: scale(0.95);
}

/* Footer row containing the Reset, Autofill, and Submit buttons */
.controls {
    display: flex;
    justify-content: flex-end;
    gap: 15px;
    margin-top: 20px;
}

/* Base styles shared by all game buttons */
.btn {
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    border: none;
}

/* Filled blue button used for the primary Submit action */
.btn-primary {
    background: #4299e1;
    color: white;
}

/* Lightly tinted button for secondary actions like Reset */
.btn-ghost {
    background: rgb(255 255 255 / 29%);
    color: #2c5282;
}

/* All buttons lift slightly on hover */
.btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(66, 153, 225, 0.2);
}

/* Leaderboard panel that sits below the game and shows top completion times */
.leaderboard {
    background: linear-gradient(180deg, rgba(95, 73, 174, 0.18), rgba(60, 97, 156, 0.4));
    border-radius: 10px;
    padding: 20px;
    margin-top: 20px;
    color: #ffffffff;
    border: 1px solid rgba(255, 255, 255, 0.04);
}

/* Header row inside the leaderboard */
.leaderboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

/* Table that fills the leaderboard panel */
.leaderboard-table {
    width: 100%;
    border-collapse: collapse;
}

/* Shared padding and text color for header and data cells */
.leaderboard-table th,
.leaderboard-table td {
    padding: 10px;
    text-align: left;
    color: #b2c7deff;
}

/* Alternating row tint makes it easier to scan across entries */
.leaderboard-table tr:nth-child(even) {
    background: rgba(29, 31, 75, 1);
}
</style>

<!-- Main game card containing the header, bins, image tray, controls, and leaderboard -->
<div class="game-container" id="media-bias-game">
    <div class="game-header">
        <div class="player-info">
            <div class="info-pill" id="player-name">Player: Guest</div>
            <div class="info-pill" id="timer">Time: 0:00</div>
        </div>
        <button class="btn btn-primary" id="auth-btn">Sign In</button>
    </div>
    <!-- Three drop targets, one per bias category -->
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
    <!-- Image tray where unsorted logos appear, plus the optional help popover -->
    <div class="source-selection">
        <div class="images-area" id="images"></div>
        <div class="help-popover" id="help-popover" role="dialog" aria-live="polite" aria-label="Need help with media bias?">
            <div class="help-popover-title">Need help?</div>
            <p class="help-popover-text">Jump to Source Intel Chat for quick tips on bias and sources.</p>
            <div class="help-popover-actions">
                <button type="button" class="help-popover-btn primary" id="help-popover-go">Go to Chat</button>
                <button type="button" class="help-popover-btn ghost" id="help-popover-dismiss">Not now</button>
            </div>
        </div>
    </div>
    <!-- Action buttons: reset the board, autofill answers, or submit a score -->
    <div class="controls">
        <button class="btn btn-ghost" id="reset-btn">Reset</button>
        <button class="btn btn-ghost" id="autofill-images" title="Autofill images">Autofill</button>
        <button class="btn btn-primary" id="submit-btn">Submit Score</button>
    </div>
    <!-- Leaderboard showing the top five fastest completion times -->
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
            </tbody>
        </table>
    </div>
</div>

<script type="module">
    // Import the backend base URL from the site config and attach it to window so the second module script below can read it without re-importing
    import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';
    window.pythonURI = pythonURI;

    // Find the session endpoint to find out if the user is currently logged in.
    // Returns the user object on success or null if there is no active session.
    async function getCurrentUser() {
        try {
            const response = await fetch(`${pythonURI}/api/id`, {
                method: 'GET',
                credentials: 'include',   // send the session cookie so the backend can verify it
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            // Only try to read the body when the server returned a success status
            if (response.ok) {
                const userData = await response.json();
                return userData;   // object contains uid, name, role, etc.
            }
        } catch (error) {
            // Network failures and CORS errors land here; treat the user as a guest
            console.log('No authenticated user:', error);
        }

        // Returning null signals guest state to every caller
        return null;
    }

    // Refreshes the sign-in/sign-out button and the player name pill to match whether a real session currently exists
    async function updateAuthButton() {
        const authBtn       = document.getElementById('auth-btn');
        const playerDisplay = document.getElementById('player-name');

        // If either element is missing from the DOM there is nothing to update
        if (!authBtn || !playerDisplay) return;

        // Ask the backend for the current session state before making any changes
        const user = await getCurrentUser();

        if (user && user.uid) {
            // Authenticated: rename the button to Sign Out and wire it to the logout URL
            authBtn.textContent = 'Sign Out';
            authBtn.onclick = () => {
                window.location.href = '{{site.baseurl}}/logout';
            };

            // Show the real username in the pill and store it globally for the game module
            playerDisplay.textContent = `Player: ${user.uid}`;
            window.currentPlayerUid   = user.uid;
            window.currentPlayerName  = user.name;
        } else {
            // Guest: rename the button to Sign In and wire it to the login page
            authBtn.textContent = 'Sign In';
            authBtn.onclick = () => {
                window.location.href = '{{site.baseurl}}/login';
            };

            // Show a generic placeholder and mark the player as Guest globally
            playerDisplay.textContent = 'Player: Guest';
            window.currentPlayerUid   = 'Guest';
            window.currentPlayerName  = 'Guest';
        }
    }

    // Run the auth check as soon as the HTML is parsed so the button state is correct before the user has any chance to interact with it
    window.addEventListener('DOMContentLoaded', () => {
        updateAuthButton();
    });

    // Expose the function on window so other scripts or a post-login redirect can trigger a button refresh without needing to re-import this module
    window.updateAuthButton = updateAuthButton;
</script>


<script type="module">
    import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

    // Root folder where all media outlet logo images are stored
    const IMAGE_BASE = '{{site.baseurl}}/media/assets/';

    // Complete list of every outlet the game knows about.
    // Each object holds the image filename, the display name used in modals, and the correct bin so placements can be validated at submit time.The game randomly draws 7 from each category (Left, Center, Right) each round.
    const imageFiles = [
        { src: "atlanticL.png",    company: "Atlantic",             bin: "Left"   },
        { src: "buzzfeedL.png",    company: "Buzzfeed",             bin: "Left"   },
        { src: "cnnL.png",         company: "CNN",                  bin: "Left"   },
        { src: "epochR.png",       company: "Epoch Times",          bin: "Right"  },
        { src: "forbesC.png",      company: "Forbes",               bin: "Center" },
        { src: "hillC.png",        company: "The Hill",             bin: "Center" },
        { src: "nbcL.png",         company: "NBC",                  bin: "Left"   },
        { src: "newsweekC.png",    company: "Newsweek",             bin: "Center" },
        { src: "nytL.png",         company: "NY Times",             bin: "Left"   },
        { src: "voxL.png",         company: "Vox",                  bin: "Left"   },
        { src: "wtR.png",          company: "Washington Times",     bin: "Right"  },
        { src: "bbcC.png",         company: "BBC",                  bin: "Center" },
        { src: "callerR.png",      company: "The Daily Caller",     bin: "Right"  },
        { src: "dailywireR.png",   company: "Daily Wire",           bin: "Right"  },
        { src: "federalistR.png",  company: "Federalist",           bin: "Right"  },
        { src: "foxR.png",         company: "Fox News",             bin: "Right"  },
        { src: "marketwatchC.png", company: "MarketWatch",          bin: "Center" },
        { src: "newsmaxR.png",     company: "Newsmax",              bin: "Right"  },
        { src: "nprL.png",         company: "NPR",                  bin: "Left"   },
        { src: "reutersC.png",     company: "Reuters",              bin: "Center" },
        { src: "wsjC.png",         company: "Wall Street Journal",  bin: "Center" },
        { src: "abcL.png",         company: "ABC",                  bin: "Left"   },
        { src: "timeL.png",        company: "Time",                 bin: "Left"   },
        { src: "yahooL.png",       company: "Yahoo News",           bin: "Left"   },
        { src: "newsnationC.png",  company: "News Nation",          bin: "Center" },
        { src: "reasonC.png",      company: "Reason News",          bin: "Center" },
        { src: "sanC.png",         company: "SAN News",             bin: "Center" },
        { src: "nypR.png",         company: "New York Post",        bin: "Right"  },
        { src: "upwardR.png",      company: "Upward News",          bin: "Right"  },
        { src: "cbnR.png",         company: "CBN",                  bin: "Right"  }
    ];

    // localStorage helpers
    // All game data lives under one versioned key so reads and writes go through a single path and future schema changes are easy to handle in one place.

    const STORAGE_KEY = 'biasGameData_v1';

    // Shape that every freshly loaded data object must conform to.
    // Used both as the initial value and as the merge template inside loadData.
    const DEFAULT_DATA = {
        profiles:  {},
        gameState: {},
        meta:      { lastModule: null, showInstructions: true },
        _version:  1
    };

    // Wraps localStorage.getItem in a try/catch so private-browsing mode and storage quota errors fail silently instead of crashing the game
    function _safeGet(key) {
        try {
            return localStorage.getItem(key);
        } catch (err) {
            console.warn('localStorage read error', err);
            return null;
        }
    }

    // Same silent-fail wrapper for localStorage.setItem
    function _safeSet(key, value) {
        try {
            localStorage.setItem(key, value);
        } catch (err) {
            console.warn('localStorage write error', err);
        }
    }

    // Reads and returns the full game data object, merging in any missing keys from DEFAULT_DATA so downstream code never has to guard for undefined
    function loadData() {
        const raw = _safeGet(STORAGE_KEY);

        // Nothing stored yet so hand back a clean deep copy of the defaults
        if (!raw) return JSON.parse(JSON.stringify(DEFAULT_DATA));

        try {
            const parsed = JSON.parse(raw);

            // Shallow-merge the saved object onto the defaults so new keys added to DEFAULT_DATA in future code versions are automatically present
            const merged     = Object.assign({}, DEFAULT_DATA, parsed);
            merged.profiles  = Object.assign({}, DEFAULT_DATA.profiles,  parsed.profiles  || {});
            merged.gameState = Object.assign({}, DEFAULT_DATA.gameState, parsed.gameState || {});
            merged.meta      = Object.assign({}, DEFAULT_DATA.meta,      parsed.meta      || {});

            return merged;
        } catch (err) {
            // Corrupt JSON in storage: log and fall back to a clean default object
            console.warn('Failed to parse storage; returning defaults', err);
            return JSON.parse(JSON.stringify(DEFAULT_DATA));
        }
    }

    // Writes the data object back to localStorage and stamps the current schema version so data from older builds can be detected on a future load
    function saveData(data) {
        try {
            data._version = DEFAULT_DATA._version;
            _safeSet(STORAGE_KEY, JSON.stringify(data));
        } catch (err) {
            console.warn('Failed to save storage', err);
        }
    }

    // Removes the stored bin assignment for each of the provided image IDs.
    // Called by the reset button so those cards return to the unsorted tray above.
    function clearGameStateForIds(ids = []) {
        const data = loadData();

        // Make sure gameState exists before trying to delete keys from it
        if (!data.gameState) data.gameState = {};

        ids.forEach(id => {
            // hasOwnProperty guard avoids accidentally touching prototype properties
            if (Object.prototype.hasOwnProperty.call(data.gameState, id)) {
                delete data.gameState[id];
            }
        });

        saveData(data);
    }

    // Session-level game state
    // These variables reset every time initGame runs and are read by event handlers.
    let currentPlayer = "Guest";     // If logged in, the username will appear instead of Guest
    let placedImages  = new Set();   // IDs of every card that has been dropped into a bin
    let timerHandle   = null;        // object returned by startTimer or null when idle
    let gameStarted   = false;       // true after the player's first manual drag
    let autofillUsed  = false;       // true if the Autofill button was clicked this round

    // Cache DOM references once at module load so querySelector is not called repeatedly
    const playerDisplay = document.getElementById('player-name');
    const timerDisplay  = document.getElementById('timer');
    const bins          = document.querySelectorAll('.bin');
    const imagesArea    = document.getElementById('images');

    // Starts a 1-second interval and returns a handle with two methods.
        // stop() halts the interval and returns total elapsed wall-clock seconds.
        // getSeconds() reads the running count without stopping the timer.
    function startTimer() {
        // Record the wall-clock start time so the final total is accurate even
        // if the browser throttles the interval slightly
        const startedAt = Date.now();
        let seconds = 0;

        // Tick the counter once per second and push the new value to the display
        const interval = setInterval(() => {
            seconds++;
            updateTimerDisplay(seconds);
        }, 1000);

        return {
            // Clear the interval and calculate elapsed time from the wall clock
            // rather than relying on the interval counter to be perfectly precise
            stop: () => {
                clearInterval(interval);
                const total = Math.round((Date.now() - startedAt) / 1000);
                return total;
            },
            // Read the running counter without stopping it
            getSeconds: () => seconds
        };
    }

    // Converts a raw second count to MM:SS format and writes it to the timer pill
    function updateTimerDisplay(seconds) {
        // Integer division gives whole minutes; modulo gives the leftover seconds
        const minutes = Math.floor(seconds / 60);
        const secs    = seconds % 60;

        if (timerDisplay) {
            // padStart ensures single-digit seconds always show two characters e.g. 0:07
            timerDisplay.textContent = `Time: ${minutes}:${secs.toString().padStart(2, '0')}`;
        }
    }

    // Visually freezes the timer display after autofill so it is clear to the player that the clock has stopped and the time will not be submitted to the leaderboard
    function lockTimerDisplay() {
        if (timerDisplay) {
            // Capture the readable time string before overwriting innerHTML
            const currentTime = timerDisplay.textContent;

            // Layer a lock icon using unicode "&#x1F512" over the existing time text using absolute positioning
            timerDisplay.innerHTML = `
                <span style="position: relative; display: inline-block;">
                    ${currentTime}
                    <span style="
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 1.2em;
                        color: #ef4444;
                        text-shadow: 0 0 3px white;
                    ">&#x1F512;</span>  
                </span>
            `;

            // Dim the whole pill to reinforce that it is no longer counting
            timerDisplay.style.opacity = '0.6';
        }
    }

    // Pushes the current player name into the info pill in the game header
    function updateDisplays() {
        playerDisplay.textContent = `Player: ${currentPlayer}`;
    }

    // Converts a company display name into a safe DOM id by lowercasing by collapsing non-word characters into underscores and adding a prefix.
    // For example: "NY Times" becomes "img-ny_times"
    function slugify(text) {
        return 'img-' + String(text)
            .toLowerCase()
            .replace(/[^\w]+/g, '_')    // replace spaces, dots, dashes etc. with underscores
            .replace(/^_+|_+$/g, '');   // strip any leading or trailing underscores
    }

    // Builds and returns one draggable img element for the given source file. Clicking or dragging the card pre-fills the news-source input in the chat panel so the player can look up that outlet without typing.
    function createImageCard(file) {
        // Create the img element and stamp all the data attributes the game relies on
        const img           = document.createElement('img');
        img.src             = IMAGE_BASE + file.src;
        img.alt             = file.company;
        img.className       = 'image';
        img.draggable       = true;
        img.dataset.bin     = file.bin;        // correct answer used during validation
        img.dataset.company = file.company;
        img.dataset.id      = slugify(file.company);
    
        // Call autofillNewsSource() to pre-populate the news source input in the chat panel (implemented by another team member's module). This lets players quickly look up bias info about the outlet they're dragging.
        const autofillNewsSource = () => {
            const newsSourceInput = document.getElementById('news-source');
            if (!newsSourceInput) return;    // field may not exist on every page variant
            newsSourceInput.value = file.company;
            newsSourceInput.dispatchEvent(new Event('input', { bubbles: true }));
        };

        img.addEventListener('click', () => {
            autofillNewsSource();
        });

        img.addEventListener('dragstart', (e) => {
            
            autofillNewsSource();
            
            //This section that starts the timer with a drag is part of my project
            // Start the round timer on the very first manual drag.
            // The autofillUsed guard prevents the timer from starting if the player already clicked Autofill and is now dragging one of the placed cards.
            if (!gameStarted && !autofillUsed) {
                gameStarted = true;
                timerHandle = startTimer();
                console.log("Timer started!");
            }

            // Apply the dragging CSS class so the card dims while in flight with the cursor
            e.target.classList.add('dragging');

            // Store the card ID in the drag payload so the drop handler can look up the element without relying on any shared mutable state
            e.dataTransfer.setData('text/plain', e.target.dataset.id);
        });

        img.addEventListener('dragend', (e) => {
            // Remove the dragging class whether the card landed on a bin or not
            e.target.classList.remove('dragging');
        });

        return img;
    }

    // Initializes a new game round or resets the current round.
    // The board state (bins + tray) is cleared
    // When the game is reset, the session flags (game started, timer, autofill) are also reset
    // Randomly selects 21 cards (balanced: 7 left, 7 center, 7 right)
    // The selection is saved to local storage
    // Makes the cards draggable images
    // Any placements from previous session that are in-progress are restored
    function initGame() {
        // Wipe the image tray and every bin content area
        imagesArea.innerHTML = '';
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');

        // Clear the placement tracker and reset all session flags: autofill and a previous game
        placedImages.clear();
        gameStarted  = false;
        autofillUsed = false;

        // Stop any running timer and null the handle to avoid holding a time no longer in the DOM
        if (timerHandle) {
            timerHandle.stop();
            timerHandle = null;
        }

        // Reset the timer display to 0:00 and restore full opacity in case it was locked
        if (timerDisplay) {
            timerDisplay.textContent   = 'Time: 0:00';
            timerDisplay.style.opacity = '1';
        }

        // Returns a randomly ordered slice of arr containing count items.
        // Spread into a new array first to avoid changing the original imageFiles list.
        const getRandomSubset = (arr, count) => {
            return [...arr]
                .sort(() => 0.5 - Math.random())
                .slice(0, count);
        };

        // Split the master list into the three bias bin categories so we can sample evenly
        const leftImages   = imageFiles.filter(img => img.bin === "Left");
        const centerImages = imageFiles.filter(img => img.bin === "Center");
        const rightImages  = imageFiles.filter(img => img.bin === "Right");

        const data = loadData();
        data.meta  = data.meta || {};

        // Try to restore a previously saved round selection from localStorage. Only trust it if it contains exactly 21 entries that all resolve to known files, otherwise fall through and generate a fresh set.
        let selectedImages = null;

        if (Array.isArray(data.meta.roundImages) && data.meta.roundImages.length === 21) {
            // Build a quick lookup map from slug ID to file object
            const idMap = new Map(imageFiles.map(f => [slugify(f.company), f]));
            const files = data.meta.roundImages
                .map(id => idMap.get(id))
                .filter(Boolean);   // drop any IDs that no longer exist in imageFiles

            // Only use the restored set when every single entry resolved correctly
            if (files.length === 21) {
                selectedImages = files;
            }
        }

        // No usable saved set found, so draw a fresh balanced selection and persist it immediately so a reload within the same round is consistent. Each bin,Left, Center, and Right, wil have an equal 7 news icons randomly selected from the list.
        if (!selectedImages) {
            selectedImages = [
                ...getRandomSubset(leftImages,   7),
                ...getRandomSubset(centerImages, 7),
                ...getRandomSubset(rightImages,  7)
            ].sort(() => 0.5 - Math.random());   // shuffle the combined 21 cards

            // Save slugified IDs (removing special characters to become a URL slug form of text) so the same set can be restored on the next page load
            data.meta.roundImages = selectedImages.map(f => slugify(f.company));
            saveData(data);
        }

        // Build a card element for each selected file and add it to the tray
        selectedImages.forEach((file) => {
            const card = createImageCard(file);
            imagesArea.appendChild(card);
        });

        // Re-apply any bin placements the player had already made before the page was loaded.
        // This restores their progress from localStorage so a refresh does not wipe their hard work.
        document.querySelectorAll('img.image').forEach(img => {
            const id   = img.dataset.id;
            const zone = data.gameState && data.gameState[id];

            if (zone) {
                // Find the bin whose data-bin attribute matches the saved zone name
                const bin = document.querySelector(`.bin[data-bin="${zone}"]`);
                if (bin) {
                    bin.querySelector('.bin-content').appendChild(img);
                    placedImages.add(id);   // keep the set in sync with what is in the DOM
                    img.style.opacity = '1';
                    img.style.cursor  = 'grab';
                }
            }
        });

        // Record which module was last active so other parts of the page can read it
        // "data.meta.lastModule = 'sortingGame';" is for my other group member's section of the project. Not relevent to the Media Bias game
        data.meta.lastModule = 'sortingGame';
        saveData(data);
    }

    // Places every card into its correct bin automatically without any player input.
    // Stops and locks the timer so the completed state cannot be added via post method to the leaderboard.
    function autofillImageGame(showAlert = false) {
        // Kill the timer if it was already running from a partial manual attempt
        if (timerHandle) {
            timerHandle.stop();
            timerHandle = null;
        }

        // Set the flag before doing anything else so the submit handler sees it immediately
        autofillUsed = true;

        // Stop the display so the player can see the clock is no longer running with a lock symbol
        lockTimerDisplay();

        // Clear all bin contents first so previously placed cards do not duplicate revealing answers incase they want to attempt again
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');

        // Work from every card currently on the page regardless of where it sits
        const imgs = Array.from(document.querySelectorAll('img.image'));
        let correctCount = 0;
        // Make sure the data is initialized to avoid "Typrerror: Cannot set property..." errors
        const data     = loadData();
        data.gameState = data.gameState || {};

        imgs.forEach(img => {
            // Each card already knows its correct bin via the data-bin attribute set when it's created
            const target = img.dataset.bin;
            const id     = img.dataset.id;

            // Find the bin element whose data-bin attribute matches the card's correct category
            const bin = Array.from(document.querySelectorAll('.bin'))
                .find(b => b.dataset.bin === target);

            if (bin) {
                // Move the card element into the correct bin content area
                bin.querySelector('.bin-content').appendChild(img);
                img.style.opacity = '1';
                img.style.cursor  = 'grab';

                // Save the placement in both the in-memory set and localStorage
                placedImages.add(id);
                data.gameState[id] = target;
                correctCount++;
            }
        });

        // Keep every auto-placed position so state remains consistent across modules
        saveData(data);
    }

    // Attaches drag-and-drop event handlers to every bin element so they can receive cards that are dragged over and dropped onto them.
    bins.forEach(bin => {

        // dragover must call preventDefault to tell the browser this element accepts drops because without it the drop event will never fire on this element
        bin.addEventListener('dragover', e => {
            e.preventDefault();
            bin.classList.add('highlight');   // light up the bin to confirm it is a valid target
        });

        // Remove the highlight as soon as the dragged card exits the bin boundary
        bin.addEventListener('dragleave', () => {
            bin.classList.remove('highlight');
        });

        bin.addEventListener('drop', e => {
            e.preventDefault();
            bin.classList.remove('highlight');   // clear the visual indicator once the card lands in desired bin

            // Retrieve the card ID that was stored in the drag payload at dragstart time
            const id  = e.dataTransfer.getData('text/plain');
            const img = document.querySelector(`[data-id="${id}"]`);

            // The element could theoretically have been removed from the DOM so this is a saftey measure
            if (!img) return;

            // Remove (delete) the card from the placed set before re-adding it under the new bin
            placedImages.delete(id);

            // Move the card element into this bin's content area
            bin.querySelector('.bin-content').appendChild(img);
            placedImages.add(id);

            // Restore full opacity and grab cursor in case earlier code had altered them
            img.style.opacity = '1';
            img.style.cursor  = 'grab';

            // Keep the placement right away so a page refresh does not lose this drop of the icon into the bin
            const data     = loadData();
            data.gameState = data.gameState || {};
            data.gameState[id] = bin.dataset.bin;
            saveData(data);
        });
    });

    // Reads the player identity that was stored globally by the auth module and pushes it so it displays as the player name pill in the game header
    async function fetchUser() {
        // currentPlayerUid is set by updateAuthButton in the first script module
        if (window.currentPlayerUid) {
            currentPlayer = window.currentPlayerUid;
        } else {
            currentPlayer = 'Guest';
        }

        updateDisplays();
    }

    // Posts a completed score to the backend endpoint and then refreshes the leaderboard. This function is the legacy path; submitFinalTime is the one called by the submit button.
    async function postScore(username, finalTime) {
        try {
            const response = await fetch(
                `${pythonURI}/api/media/score/${encodeURIComponent(username)}/${finalTime}`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include'   // include the session cookie for server-side auth to save the userid in the leaderboard next to score
                }
            );

            if (!response.ok) throw new Error('Failed to save score');

            // Pull fresh standings immediately after a successful save
            fetchLeaderboard();
        } catch (err) {
            console.error('Error saving score:', err);
        }
    }

    // The limit parameter controls how many rows are fetched and requested from the backend when displaying top entreis for the leaderboard table
    // A smaller limit keeps the panel compact in a way where scrolling is minimized
    async function fetchLeaderboard(limit = 5) {
        const tbody = document.getElementById('leaderboard-body');

        try {
            // Pass the limit value directly into the URL so the backend only returns that many rows
            const response = await fetch(pythonURI + `/api/media/leaderboard?limit=${limit}`);

            // If the server returned an error status, throw so the catch block handles it
            if (!response.ok) throw new Error('Failed to fetch leaderboard');

            const data = await response.json();

            // Clear any previous rows before inserting fresh data so old entries do not stack up
            tbody.innerHTML = '';

            // Iterate over every entry the server returned and insert one table row each
            data.forEach((entry, index) => {
                const row = tbody.insertRow();

                // Use the backend rank field if available, otherwise fall back to loop position
                row.insertCell().textContent = entry.rank || (index + 1);
                row.insertCell().textContent = entry.username || 'Unknown';

                // Convert raw seconds into a readable MM:SS string for the time column
                const timeInSeconds = entry.time || 0;
                const minutes       = Math.floor(timeInSeconds / 60);
                const seconds       = timeInSeconds % 60;
                row.insertCell().textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
            });
        } catch (err) {
            console.error('Error fetching leaderboard:', err);

            // Show a friendly error row so the player knows the leaderboard could not load
            tbody.innerHTML = '<tr><td colspan="3">Unable to load leaderboard</td></tr>';
        }
    }

    // Shows a full-screen modal informing the player that autofill was detected and that their time will not appear on the leaderboard
    function showAutofillWarning() {
        // Create the dark semi-transparent overlay that sits on top of the whole page
        const msg = document.createElement('div');
        msg.style.position       = 'fixed';
        msg.style.top            = '0';
        msg.style.left           = '0';
        msg.style.width          = '100vw';
        msg.style.height         = '100vh';
        msg.style.background     = 'rgba(0,0,0,0.55)';
        msg.style.display        = 'flex';
        msg.style.alignItems     = 'center';
        msg.style.justifyContent = 'center';
        msg.style.zIndex         = '9999';

        // Inject the card content HTML into the overlay div
        msg.innerHTML = `
          <div style="background: #6a75c8ff;padding:28px;border-radius:14px;box-shadow:0 8px 32px rgba(0,0,0,0.2);text-align:center;max-width:420px;">
            <h2 style="color: #ff6b6b;margin-bottom:12px;">!!Autofill Used!!</h2>
            <p style="color: #e6f0ff;margin:0 0 18px;font-size:1.05rem;">
              You used autofill! While you have completed the puzzle, your time will not be added to the leaderboard.
            </p>
            <p style="color: #e6f0ff;margin:0 0 18px;font-size:1rem;">
              Please try to attempt the bias game yourself when you can to compete for the top scores!
            </p>
            <button id="return-to-game-autofill" style="padding:10px 18px;border-radius:8px;background:#4299e1;color:white;border:none;cursor:pointer;font-weight:700;">
              Got It!
            </button>
          </div>
        `;

        // Add the overlay to the body so it renders above everything else
        document.body.appendChild(msg);

        // Wire the "Got It" button to remove the overlay and hand control back to the game
        const btn = document.getElementById('return-to-game-autofill');
        if (btn) {
            btn.addEventListener('click', () => {
                msg.remove();
            });
        }
    }

    // Shows a full-screen congratulations modal after a legitimate submission without only autofill.
    // Formats the elapsed seconds into MM:SS and displays the completion time prominently.
    function showCongrats(elapsedSeconds) {
        // Build the time string before touching the DOM
        const minutes    = Math.floor(elapsedSeconds / 60);
        const seconds    = elapsedSeconds % 60;
        const timeString = `${minutes}:${seconds.toString().padStart(2, '0')}`;

        // Build the same style of full-page overlay used by the other game modals
        const msg = document.createElement('div');
        msg.style.position       = 'fixed';
        msg.style.top            = '0';
        msg.style.left           = '0';
        msg.style.width          = '100vw';
        msg.style.height         = '100vh';
        msg.style.background     = 'rgba(0,0,0,0.55)';
        msg.style.display        = 'flex';
        msg.style.alignItems     = 'center';
        msg.style.justifyContent = 'center';
        msg.style.zIndex         = '9999';

        // Embed the formatted completion time so it is the first thing the player sees when they finish the game
        msg.innerHTML = `
          <div style="background: #6a75c8ff;padding:28px;border-radius:14px;box-shadow:0 8px 32px rgba(0,0,0,0.2);text-align:center;max-width:420px;">
            <h2 style="color: #546dbeff;margin-bottom:8px;">Congratulations!</h2>
            <p style="color: #e6f0ff;margin:0 0 12px;font-size:1.05rem;">
              Congratulations on mastering media bias.
            </p>
            <p style="color: #4ade80;margin:0 0 18px;font-size:1.3rem;font-weight:700;font-family:'Courier New',monospace;">
              Completed in ${timeString}
            </p>
            <button id="return-to-game" style="padding:10px 18px;border-radius:8px;background:#4299e1;color:white;border:none;cursor:pointer;font-weight:700;">
              Return to Game
            </button>
          </div>
        `;

        document.body.appendChild(msg);

        // Clicking Return to Game dismisses the overlay;
        // initGame is called by the submit handler right after showCongrats returns
        const btn = document.getElementById('return-to-game');
        if (btn) {
            btn.addEventListener('click', () => {
                msg.remove();
            });
        }
    }

    // Shows a modal listing every card that landed in the wrong bin.
    // Each entry displays the outlet logo, the outlet name, and which bin it was placed in so the player gets specific feedback rather than a generic wrong-answer message.
    function showIncorrectFeedback(incorrectImages) {
        // Full-page overlay consistent with the other game modals
        const modal = document.createElement('div');
        modal.style.position       = 'fixed';
        modal.style.top            = '0';
        modal.style.left           = '0';
        modal.style.width          = '100vw';
        modal.style.height         = '100vh';
        modal.style.background     = 'rgba(0,0,0,0.7)';   // slightly darker for error context
        modal.style.display        = 'flex';
        modal.style.alignItems     = 'center';
        modal.style.justifyContent = 'center';
        modal.style.zIndex         = '9999';

        // Map each incorrectly placed card to a row showing its logo, name, and wrong bin
        const imageGrid = incorrectImages.map(img =>
            `<div style="display:flex;align-items:center;gap:12px;margin:10px 0;padding:10px;background:rgba(255,100,100,0.15);border-radius:8px;">
                <img src="${img.src}" alt="${img.name}" style="width:50px;height:50px;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.2);">
                <div style="text-align:left;">
                    <div style="font-weight:700;color:#ff6b6b;font-size:1.05rem;">${img.name}</div>
                    <div style="font-size:0.9rem;color:#ffb3b3;">Currently in: ${img.currentBin}</div>
                </div>
            </div>`
        ).join('');

        // Use singular or plural phrasing depending on the number of mistakes
        modal.innerHTML = `
            <div style="background:linear-gradient(135deg, #2d3561, #4a5080);padding:30px;border-radius:18px;box-shadow:0 12px 40px rgba(0,0,0,0.4);max-width:500px;max-height:80vh;overflow-y:auto;">
                <h2 style='color:#ffd6d6;margin-bottom:8px;text-align:center;'>Incorrect Placements</h2>
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

        // The "Try Again" button closes the modal so the player can fix their mistakes
        document.getElementById('close-feedback').addEventListener('click', () => {
            modal.remove();
        });

        // Clicking anywhere on the dark backdrop also dismisses the modal
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.remove();
            }
        });
    }

    // Sends the player's elapsed seconds to the backend score endpoint with their registered username and time and then refreshes the leaderboard so the new entry appears straight away
    async function submitFinalTime(username, elapsed) {
        try {
            // Both the username and elapsed time travel in the URL path rather than the body to the backend which feeds the leaderboard
            const response = await fetch(
                `${pythonURI}/api/media/score/${encodeURIComponent(username)}/${elapsed}`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include'
                }
            );

            if (!response.ok) throw new Error('Failed to save score');

            // Pull fresh leaderboard data now that the new score is in the database
            fetchLeaderboard();
        } catch (err) {
            // Alert the player so they know the save failed and can try again
            alert('Failed to save your score. Please try again.');
        }
    }

    // Checks that every card in the current round has been placed in a bin.
    // Returns false and shows an alert if any cards are still sitting in the image tray.
    function validateAllPlaced(placedImages) {
        // Count all card elements currently in the DOM
        const total = document.querySelectorAll('.image').length;

        if (placedImages.size < total) {
            // Tell the player exactly how many cards remain so they know what to look for
            alert(`Place all images first! (${placedImages.size}/${total})`);
            return false;
        }

        return true;
    }

    // Displays every bin and collects cards whose data-bin attribute does not match the bin they currently sit inside. Returns an array of plain objects that the feedback modal can show directly.
    function getIncorrectPlacements() {
        const incorrect = [];

        document.querySelectorAll('.bin').forEach(bin => {
            bin.querySelectorAll('.image').forEach(img => {
                // data-bin is the correct answer stamped at card creation time
                // bin.dataset.bin is where the card was actually dropped so the user can see incorrect placements
                if (img.dataset.bin !== bin.dataset.bin) {
                    incorrect.push({
                        name:       img.dataset.company,
                        currentBin: bin.dataset.bin,
                        src:        img.src
                    });
                }
            });
        });

        return incorrect;
    }

    // Wire up every button click handler as soon as the HTML is parsed. Also runs the first game initialization so cards appear without waiting for the full window load event, which may be delayed by slow-loading images.
    window.addEventListener('DOMContentLoaded', () => {

        initGame();
        // Reset Button
        const resetBtn = document.getElementById('reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {

                // Collect the ID of every card on the page before wiping anything
                const ids = Array.from(document.querySelectorAll('img.image'))
                    .map(i => i.dataset.id);

                // Delete each card's bin assignment from storage so the slate is clean
                clearGameStateForIds(ids);

                // Also remove the saved round image set so a brand new 21 are chosen
                const data = loadData();
                if (data.meta && data.meta.roundImages) {
                    delete data.meta.roundImages;
                    saveData(data);
                }

                // Run the full init to draw a fresh shuffled set of cards
                initGame();
            });
        }
        // Autofill Button:
        const autofillBtn = document.getElementById('autofill-images');
        if (autofillBtn) {
            autofillBtn.addEventListener('click', () => {
                autofillImageGame(true);   // passing true signals the button was explicitly pressed
            });
        }
        // Submit Button:
        const submitBtn = document.getElementById('submit-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {

                // Gate 1: every card must be in a bin before anything else is checked
                if (!validateAllPlaced(placedImages)) return;

                // Gate 2: all placed cards must be in their correct bins, if they aren't the feedback modal is displayed indicating what icons are in the wrong placements
                const incorrect = getIncorrectPlacements();
                if (incorrect.length > 0) {
                    showIncorrectFeedback(incorrect); 
                    return;
                }

                // Gate 3: autofill disqualifies this run from appearing on the leaderboard and halts the timer
                if (autofillUsed) {
                    showAutofillWarning();
                    initGame();   // start a fresh round after the player dismisses the warning
                    return;
                }

                // Gate 4: the timer must have been started by actual player interaction like dragging an icon to a bin
                if (!timerHandle) {
                    alert("Timer not started. Please play the game first!");
                    return;
                }

                // All four gates passed: stop the clock and capture the final time
                const elapsed  = timerHandle.stop();
                const username = window.currentPlayerUid || 'Guest';

                // Save locally first so the attempt is not lost if the network call fails
                saveAttemptLocally(username, elapsed);

                // Submit the score to the backend and refresh the leaderboard
                submitFinalTime(username, elapsed);

                // Show the congratulations screen and immediately reset for a new round
                showCongrats(elapsed);
                initGame();
            });
        }
    });

    // Secondary initialization that runs once the entire page including external resources has finished loading. Syncs the player identity, ensures the game board is drawn, fetches initial leaderboard standings, and starts a 30-second polling interval so scores from other players appear without a manual reload.
    window.onload = () => {

        // Pull the authenticated username from the auth module into currentPlayer
        fetchUser();

        // initGame may have already run from DOMContentLoaded; calling it again here is safe because it always starts from a fully clean state
        initGame();

        // Show current top 5 standings as soon as the page is fully ready
        fetchLeaderboard(5);

        // Poll for updated standings every 30 seconds so new scores appear automatically
        setInterval(fetchLeaderboard, 30000);
    };
</script>