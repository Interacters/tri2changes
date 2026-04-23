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
    <!-- Image tray where unsorted logos appear-->
    <div class="source-selection">
        <div class="images-area" id="images"></div>
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
    // Importing the backend pythonURI which produces player UID info and Leaderboard info
    import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

    // ---------------------------------------------------------------------------
    // Constants & data
    // ---------------------------------------------------------------------------

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

    // ---------------------------------------------------------------------------
    // Session state
    // ---------------------------------------------------------------------------

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

    // ---------------------------------------------------------------------------
    // Timer helpers
    // ---------------------------------------------------------------------------

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

    // ---------------------------------------------------------------------------
    // UI helpers
    // ---------------------------------------------------------------------------

    // Pushes the current player name into the info pill in the game header. Player name is fetched from the backend when they login.
    function updateDisplays() {
        playerDisplay.textContent = `Player: ${currentPlayer}`;
    }

    // Converts a company display name into a safe DOM id by lowercasing by turning non-word characters into underscores and adding a prefix 'img-'.
    // For example: "NY Times" becomes "img-ny_times"
    function slugify(text) {
        return 'img-' + String(text)
            .toLowerCase()
            .replace(/[^
\w]+/g, '_')    // replace spaces, dots, dashes etc. with underscores
            .replace(/^_+|_+$/g, '');   // strip any leading or trailing underscores
    }

    // Builds and returns one draggable img element for the given source file so that game can add it to the image tray. This function also stores metadata on the element using "data." attributes.
    // ---------------------------------------------------------------------------
    // Card builder
    // ---------------------------------------------------------------------------

    function createImageCard(file) {
        // Create the img element and stamp all the data attributes the game relies on
        const img           = document.createElement('img');
        img.src             = IMAGE_BASE + file.src; // logo image path
        img.alt             = file.company; //sets the alt to the company name
        img.className       = 'image';
        img.draggable       = true;
        img.dataset.bin     = file.bin;        // correct answer used during validation
        img.dataset.company = file.company;   // This is used in the incorrect feedback modal to show the user what they got wrong
        img.dataset.id      = slugify(file.company); //ID is used during drag/drop to find the dragged card again

        img.addEventListener('dragstart', (e) => {
            
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

    // ---------------------------------------------------------------------------
    // Drag/drop bindings
    // ---------------------------------------------------------------------------

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
        });
    });

    // ---------------------------------------------------------------------------
    // Game flow
    // ---------------------------------------------------------------------------
    // Initializes a new game round or resets the current round.
    // The board state (bins + tray) is cleared
    // When the game is reset, the session flags (game started, timer, autofill) are also reset
    // Randomly selects 21 cards (balanced: 7 left, 7 center, 7 right)
    // Makes the cards draggable images
    function initGame() {
        // Wipe the selectedImages tray and every bin content area
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

        const selectedImages = [
            ...getRandomSubset(leftImages,   7),
            ...getRandomSubset(centerImages, 7),
            ...getRandomSubset(rightImages,  7)
        ].sort(() => 0.5 - Math.random());   // shuffle the combined 21 cards

        // Build a card element for each selected file and add it to the tray
        selectedImages.forEach((file) => {
            const card = createImageCard(file);
            imagesArea.appendChild(card);
        });

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

                // Save the placement in the session-only set
                placedImages.add(id);
                correctCount++;
            }
        });
    }

    // ---------------------------------------------------------------------------
    // Auth & leaderboard
    // ---------------------------------------------------------------------------
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

            // Show a error row so the player knows the leaderboard could not load
            tbody.innerHTML = '<tr><td colspan="3">Unable to load leaderboard</td></tr>';
        }
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
            fetchLeaderboard(5);
        } catch (err) {
            console.error('Error saving score:', err);
        }
    }


    // ---------------------------------------------------------------------------
    // Modals
    // ---------------------------------------------------------------------------

    // AUTOFILL USED ALERT: Shows a full-screen modal informing the player that autofill was detected and that their time will not appear on the leaderboard
    function showAutofillWarning() {
        // Create the dark semi-transparent sheer overlay that sits on top of the whole page
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

        // EXIT: Wire the "Got It" button to remove the overlay and hand control back to the game
        const btn = document.getElementById('return-to-game-autofill');
        if (btn) {
            btn.addEventListener('click', () => {
                msg.remove();
            });
        }
    }

    // CONGRATULATIONS ALERT: Shows a full-screen congratulations modal after a legitimate submission without only autofill.
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

        // EXIT: Clicking Return to Game dismisses the overlay;
        // initGame is called by the submit handler right after showCongrats returns
        const btn = document.getElementById('return-to-game');
        if (btn) {
            btn.addEventListener('click', () => {
                msg.remove();
            });
        }
    }

    // INCORRECT ALERT: Shows a modal listing every card that landed in the wrong bin.
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

        // EXIT: The "Try Again" button closes the modal so the player can fix their mistakes
        document.getElementById('close-feedback').addEventListener('click', () => {
            modal.remove();
        });

        // EXIT: Clicking anywhere on the dark backdrop also dismisses the modal
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.remove();
            }
        });
    }

    // ---------------------------------------------------------------------------
    // Validation & submit
    // ---------------------------------------------------------------------------

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
            fetchLeaderboard(5);
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

    // This function checks each card against its correct bin to validate the player's placements
    // It iterates through all bins, then through all images in each bin, and finds mismatches
    // The result is used to provide specific feedback on which cards are wrong and where they are so the player can fix them
    function getIncorrectPlacements(binsList) {
        const incorrect = []; // Array to hold details of incorrectly placed cards

        binsList.forEach(bin => { // Iterate through each bin element
            bin.querySelectorAll('.image').forEach(img => { // For each image card in this bin
                // Check if the card's correct bin (data-bin) matches the bin it's currently in
                if (img.dataset.bin !== bin.dataset.bin) {
                    // Card is misplaced, collect its details for feedback
                    incorrect.push({
                        name: img.dataset.company, // Company name to display in the feedback modal
                        currentBin: bin.dataset.bin, // The bin where the card is currently placed (wrong)
                        src: img.src // Image source to show the outlet logo
                    });
                }
            });
        });

        return incorrect; // Return the list of incorrect placements
    }

    // ---------------------------------------------------------------------------
    // Event wiring
    // ---------------------------------------------------------------------------

    // Wire up every button click handler as soon as the HTML is parsed. Also runs the first game initialization so cards appear without waiting for the full window load event, which may be delayed by slow-loading images.
    window.addEventListener('DOMContentLoaded', () => {

        // Build the first round immediately after the page HTML is parsed.
        initGame();

        // Reset Button: clears the current board and starts a brand new game round
        const resetBtn = document.getElementById('reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                // Reset does not keep any previous assignments or round state
                // It simply rebuilds the tray, bins, and timer from ground 0
                initGame();
            });
        }

        // Autofill Button: automatically places every card into its correct bin
        const autofillBtn = document.getElementById('autofill-images');
        if (autofillBtn) {
            autofillBtn.addEventListener('click', () => {
                autofillImageGame(true);   // passing true signals the button was deliberaely pressed
            });
        }

        // Submit Button: validates the current board and submits the score if correct
        const submitBtn = document.getElementById('submit-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {

                // Checkpoint 1: every card must be in a bin before anything else is checked

                if (!validateAllPlaced(placedImages)) return;

                // Checkpoint 2: all placed cards must be in their correct bins, if they aren't the feedback modal is displayed indicating what icons are in the wrong placements
                // Retrieve a list of incorrectly placed cards by checking each bin for mismatches by finding every element with class="bin" (e.g., the three drop zones for Left, Center, and Right bias categories)
                const incorrect = getIncorrectPlacements(document.querySelectorAll('.bin'));
                // If there are any mistakes, show the feedback modal and stop submission
                if (incorrect.length > 0) {
                    showIncorrectFeedback(incorrect); 
                    return; // Prevent further processing (score submission)
                }

                // Checkpoint 3: autofill disqualifies this run from appearing on the leaderboard and halts the timer
                if (autofillUsed) {
                    showAutofillWarning();
                    initGame();   // start a fresh round after the player dismisses the warning
                    return;
                }

                // Checkpoint 4: the timer must have been started by actual player interaction like dragging an icon to a bin
                if (!timerHandle) {
                    alert("Timer not started. Please play the game first!");
                    return;
                }

                // All four gates passed: stop the clock and capture the final time
                const elapsed  = timerHandle.stop();
                const username = window.currentPlayerUid || 'Guest';

                // Submit the score to the backend and refresh the leaderboard
                submitFinalTime(username, elapsed);

                // Show the congratulations screen and immediately reset for a new round
                showCongrats(elapsed);
                initGame();
            });
        }
    });

    // ---------------------------------------------------------------------------
    // Page Setup
    // ---------------------------------------------------------------------------

    // Secondary initialization that runs once the entire page including external resources has finished loading. Syncs the player identity, ensures the game board is drawn, fetches initial leaderboard standings, and starts a 30-second polling interval so scores from other players appear without a manual reload.
    window.onload = () => {

        // Pull the authenticated username from the auth module into currentPlayer
        fetchUser();

        // initGame may have already run from DOMContentLoaded; calling it again here is safe because it always starts from a fully clean state
        initGame();

        // Show current top 5 standings as soon as the page is fully ready
        fetchLeaderboard(5);

        // Poll for updated standings every 30 seconds so new scores appear automatically
        setInterval(fetchLeaderboard(5), 30000);
    };
</script>