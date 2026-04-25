<!-- This is the main game card that holds all the key parts: the header, the bins, the image tray, the controls, and the leaderboard -->
<div class="game-container" id="media-bias-game">
  <div class="game-header">
    <div class="player-info">
      <div class="info-pill" id="player">Player: Guest</div>
      <div class="info-pill" id="time">Time: 0:00</div>
    </div>
    <button class="btn btn-primary" id="auth-btn">Sign In</button>
  </div>
  <!-- Here are the three drop targets, one for each bias category -->
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
  <!-- This is the image tray where the unsorted logos appear -->
  <div class="source-selection">
    <div class="images-area" id="imgs"></div>
  </div>
  <!-- These are the action buttons: reset the board, autofill answers, or submit a score -->
  <div class="controls">
    <button class="btn btn-ghost" id="reset-btn">Reset</button>
    <button class="btn btn-ghost" id="autofill-images" title="Autofill images">Autofill</button>
    <button class="btn btn-primary" id="submit-btn">Submit Score</button>
  </div>
  <!-- This leaderboard shows the top five fastest completion times -->
  <div class="leaderboard">
    <div class="leaderboard-header">
      <h3>Top Players</h3>
    </div>
    <table class="leaderboard-table">
      <thead>
        <tr> <!-- This shows Rank, Player, and Time on the leaderboard table -->
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
    // Importing the backend pythonURI that gives us player UID info and leaderboard info
    import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

    // CONSTANTS AND DATA

    // This is the root folder where all the media outlet logo images are stored
    const imgBase = '{{site.baseurl}}/media/assets/';

    // This is the complete list of every outlet the game knows about in my repository.
    // Each object has the image filename, the display name used in modals, and the correct bin so we can validate placements at submit time.
    const files = [
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
        { src: "abcL.png", company: "ABC", bin: "Left" },
        { src: "timeL.png", company: "Time", bin: "Left" },
        { src: "yahooL.png", company: "Yahoo News", bin: "Left" },
        { src: "newsnationC.png", company: "News Nation", bin: "Center" },
        { src: "reasonC.png", company: "Reason News", bin: "Center" },
        { src: "sanC.png", company: "SAN News", bin: "Center" },
        { src: "nypR.png", company: "New York Post", bin: "Right" },
        { src: "upwardR.png", company: "Upward News", bin: "Right" },
        { src: "cbnR.png", company: "CBN", bin: "Right" }
    ];


    // This is the session-level game state
    // These variables reset every time initGame runs and are read by the event handlers.
    let user = "Guest"; // If you're logged in, the username will appear instead of Guest
    let placed = new Set(); // IDs of every card that has been dropped into a bin
    let timer = null; // This is the object returned by timerStart or null when idle
    let started = false; // This is true after the player's first manual drag
    let autofilled = false; // This is true if the Autofill button was clicked this round

    // We cache DOM references once at module load so we don't have to call querySelector repeatedly
    const playerDiv = document.getElementById('player');
    const timerDiv = document.getElementById('time');
    const bins = document.querySelectorAll('.bin');
    const imagesDiv = document.getElementById('imgs');


    // TIMER HELPERS

    // We start timer that increments once per second.
    // This returns an object so we can either stop the timer or read the current time.
    function timerStart() {

        // This stores the exact start time for more accurate final calculations
        const startTimestamp = Date.now();
        let elapsedSeconds = 0;

        // This updates the visible timer every second
        const interval = setInterval(() => {
            elapsedSeconds++;
            timeShow(elapsedSeconds);
        }, 1000);

        return {
            // This stops the timer and calculates total elapsed time using real clock time
            stop: () => {
                clearInterval(interval);
                const totalSeconds = Math.round((Date.now() - startTimestamp) / 1000);
                return totalSeconds;
            },

            // This returns the current running time without stopping the timer
            getSeconds: () => elapsedSeconds
        };
    }


    // This converts raw seconds into MM:SS format and updates the UI
    function timeShow(seconds) {

        const minutes = Math.floor(seconds / 60); // Minutes are calulated with division
        const remainingSeconds = seconds % 60; // Seconds are calculated with multiplication

        if (timerDiv) {
            timerDiv.textContent =
                `Time: ${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
        }
    }


    // Visually locks the timer after autofill is used using a lock emoji in unicode
    // This makes it clear the time will not count toward the leaderboard
    function lockTime() {

        if (!timerDiv) return;

        const currentText = timerDiv.textContent;

        timerDiv.innerHTML = `
            <span style="position: relative; display: inline-block;">
                ${currentText}
                <span style="
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-size: 1.2em;
                    color: #ef4444;
                    text-shadow: 0 0 3px white;
                ">
                    &#x1F512; 
                </span>
            </span>
        `;
    }


    // UI HELPERS


    // This pushes the current player name into the info pill in the game header. The player name is fetched from the backend when they login.
    function updateUI() {
        playerDiv.textContent = `Player: ${user}`;
    }


    // CARD CATEGORIES
   

    function createIMG(file) {
        // We create the img element and stamp all the data attributes the game relies on
        const img = document.createElement('img');
        img.src  = imgBase + file.src; // This is the logo image path
        img.alt = file.company; // This sets the alt to the company name
        img.className = 'image';
        img.draggable = true;
        img.dataset.bin = file.bin;        // This is the correct answer used during validation
        img.dataset.company = file.company;   // This is used in the incorrect feedback modal to show the user what they got wrong
        img.dataset.id = slugify(file.company); // This ID is used during drag/drop to find the dragged card again

        img.addEventListener('dragstart',(e) => {
           
            // This section starts the timer with a drag
            // The autofilled guard prevents the timer from starting if the player already clicked Autofill and is now dragging one of the placed cards.
            if (!started && !autofilled) {
                started = true;
                timer = timerStart();
                console.log("Timer started!!!!");
            }

            // We apply the dragging CSS class so the card dims while in flight with the cursor
            e.target.classList.add('dragging');

            // We store the card ID in the drag payload so the drop handler can look up the element without relying on any shared mutable state
            e.dataTransfer.setData('text/plain', e.target.dataset.id);
        });

        img.addEventListener('dragend', (e) => {
            // We remove the dragging class whether the card landed on a bin or not
            e.target.classList.remove('dragging');
        });

        return img;
    }


    // DRAG AND DROP 


    // This attaches drag-and-drop event handlers to every bin element so they can receive cards that are dragged over and dropped onto them.
    bins.forEach(bin => {

        // dragover has to call preventDefault to tell the browser this element accepts drops because without it the drop event will not work on the card
        bin.addEventListener('dragover', e => {
            e.preventDefault();
            bin.classList.add('highlight');   // We light up the bin to confirm it is a valid target
        });

        // We remove the highlight as soon as the dragged card exits the bin boundary
        bin.addEventListener('dragleave', () => {
            bin.classList.remove('highlight');
        });

        bin.addEventListener('drop', e => {
            e.preventDefault();
            bin.classList.remove('highlight');   // We clear the visual indicator once the card lands in the desired bin

            // We retrieve the card ID that was stored in the drag payload at dragstart time
            const id = e.dataTransfer.getData('text/plain');
            const img = document.querySelector(`[data-id="${id}"]`);

            // The element could theoretically have been removed from the DOM so this is a safety measure
            if (!img) return;

            // We remove (delete) the card from the placed set before re-adding it under the new bin
            placed.delete(id);

            // We move the card element into this bin's content area
            bin.querySelector('.bin-content').appendChild(img);
            placed.add(id);

            // We restore full opacity and grab cursor in case earlier code had altered them
            img.style.opacity = '1';
            img.style.cursor  = 'grab';
        });
    });

    // GAME FLOW

    // This initializes a new game round or resets the current round. When the game is reset, the session flags (game started, timer, autofill) are also reset
    function startGame() {
        // We wipe the selectedImages tray and every bin content area
        imagesDiv.innerHTML = '';
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');

        // We clear the placement tracker and reset all session flags: autofill and a previous game
        placed.clear();
        started = false;
        autofilled = false;

        // We stop any running timer and null the handle to avoid holding a time no longer in the DOM
        if (timer) {
            timer.stop();
            timer = null;
        }

        // We reset the timer display to 0:00 and restore full opacity in case it was locked
        if (timerDiv) {
            timerDiv.textContent = 'Time: 0:00';
            timerDiv.style.opacity = '1';
        }

        // This returns a randomly ordered slice of arr containing count items.
        // We spread into a new array first to avoid changing the original files list.
        const getRandomSubset = (arr, count) => {
            return [...arr]
                .sort(() => 0.5 - Math.random())
                .slice(0, count);
        };

        // We split the master list into the three bias bin categories so we can get a balanced, even sample
        const leftImages = files.filter(img => img.bin === "Left");
        const centerImages = files.filter(img => img.bin === "Center");
        const rightImages = files.filter(img => img.bin === "Right");

        const selectedImages = [ // We randomly select 21 cards (7 from left, 7 from center, 7 from right)
            ...getRandomSubset(leftImages, 7),
            ...getRandomSubset(centerImages, 7),
            ...getRandomSubset(rightImages, 7) 
        ].sort(() => 0.5 - Math.random());   // We shuffle the combined 21 cards

        // We build a card element for each selected file and add it to the tray
        selectedImages.forEach((file) => {
            const card = createIMG(file);
            imagesDiv.appendChild(card);
        });

    }

    // This places every card into its correct bin automatically without any player input.
    // We stop and lock the timer so the completed state cannot be added via post method to the leaderboard.
    function autofill() {
        // We kill the timer if it was already running from a partial manual attempt
        if (timerHandle) {
            timerHandle.stop();
            timerHandle = null;
        }

        // We set the flag before doing anything else so the submit handler sees it immediately
        autofilled = true;

        // We stop the display so the player can see the clock is no longer running with a lock symbol
        lockTime();

        // We clear all bin contents first so previously placed cards do not duplicate revealing answers in case they want to attempt again
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');

        // We work from every card currently on the page regardless of where it sits
        const imgs = Array.from(document.querySelectorAll('img.image'));
        let correctCount = 0;

        imgs.forEach(img => {
            // Each card already knows its correct bin via the data-bin attribute set when it's created
            const target = img.dataset.bin;
            const id     = img.dataset.id;

            // We find the bin element whose data-bin attribute matches the card's correct category
            const bin = Array.from(document.querySelectorAll('.bin'))
                .find(b => b.dataset.bin === target);

            if (bin) {
                // We move the card element into the correct bin content area
                bin.querySelector('.bin-content').appendChild(img);
                img.style.opacity = '1';
                img.style.cursor  = 'grab';

                // We save the placement in the session-only set
                placed.add(id);
                correctCount++;
            }
        });
    }


    // AUTH AND LEADERBOARD
   
    // This reads the player identity that was stored globally by the auth module and pushes it so it displays as the player name pill in the game header
    async function getUser() {
        // currentPlayerUid is set from the login system
        if (window.currentPlayerUid) {
            user = window.currentPlayerUid;
        } else {
            user = 'Guest';
        }

        updateUI();
    }

    // The limit parameter controls how many rows are fetched and requested from the backend when displaying top entries for the leaderboard table
    // A smaller limit keeps the panel compact in a way where scrolling is minimized
    async function fetchLeaderboard(limit = 5) {
        const tbody = document.getElementById('leaderboard-body');

        try {
            // We pass the limit value directly into the URL so the backend only returns that many rows
            const response = await fetch(pythonURI + `/api/media/leaderboard?limit=${limit}`);

            // If the server returned an error status, we throw so the catch block handles it
            if (!response.ok) throw new Error('Failed to fetch leaderboard');

            const data = await response.json();

            // We clear any previous rows before inserting fresh data so old entries do not stack up
            tbody.innerHTML = '';

            // We iterate over every entry the server returned and insert one table row each
            data.forEach((entry, index) => {
                const row = tbody.insertRow();

                // We use the backend rank field if available, otherwise we fall back to loop position
                row.insertCell().textContent = entry.rank || (index + 1);
                row.insertCell().textContent = entry.username || 'Unknown';

                // We convert raw seconds into a readable MM:SS string for the time column again similar to before in the time pill
                const timeInSeconds = entry.time || 0;
                const minutes = Math.floor(timeInSeconds / 60);
                const seconds = timeInSeconds % 60;
                row.insertCell().textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
            });
        } catch (err) {
            console.error('Error fetching leaderboard:', err);

            // We show an error row so the player knows the leaderboard could not load
            tbody.innerHTML = '<tr><td colspan="3">Unable to load leaderboard</td></tr>';
        }
    }


    // MODAL

    // AUTOFILL USED ALERT: This shows a full-screen modal informing the player that autofill was detected and that their time will not appear on the leaderboard
    function autofillWarn() {
        // We create the dark semi-transparent sheer overlay that sits on top of the whole page
        const msg = document.createElement('div');
        msg.style.position = 'fixed';
        msg.style.top = '0';
        msg.style.left  = '0';
        msg.style.width = '100vw';
        msg.style.height = '100vh';
        msg.style.background = 'rgba(0,0,0,0.55)';
        msg.style.display = 'flex';
        msg.style.alignItems = 'center';
        msg.style.justifyContent = 'center';
        msg.style.zIndex  = '9999';

        // We inject the card content HTML into the overlay div
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

        // We add the overlay to the body so it renders above everything else
        document.body.appendChild(msg);

        // EXIT: We wire the "Got It" button to remove the overlay and hand control back to the game
        const btn = document.getElementById('return-to-game-autofill');
        if (btn) {
            btn.addEventListener('click', () => {
                msg.remove();
            });
        }
    }

    // CONGRATULATIONS ALERT: This shows a full-screen congratulations modal after a legitimate submission without autofill.
    // We format the elapsed seconds into MM:SS and display the completion time prominently.
    function showCongrats(elapsedSeconds) {
        // We build the time string before touching the DOM
        const minutes    = Math.floor(elapsedSeconds / 60);
        const seconds    = elapsedSeconds % 60;
        const timeString = `${minutes}:${seconds.toString().padStart(2, '0')}`;

        // We build the same style of full-page overlay used by the other game modals
        const msg = document.createElement('div');
        msg.style.position = 'fixed';
        msg.style.top = '0';
        msg.style.left  = '0';
        msg.style.width = '100vw';
        msg.style.height = '100vh';
        msg.style.background = 'rgba(0,0,0,0.55)';
        msg.style.display = 'flex';
        msg.style.alignItems = 'center';
        msg.style.justifyContent = 'center';
        msg.style.zIndex  = '9999';

        // We embed the formatted completion time so it is the first thing the player sees when they finish the game
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

    // INCORRECT ALERT: This shows a modal listing every card that landed in the wrong bin.
    // Each entry displays the outlet logo, the outlet name, and which bin it was placed in so the player gets specific feedback 
    function showWrong(incorrectImages) {
        // This is a full-page overlay consistent with the other game modals
        const modal = document.createElement('div');
        modal.style.position = 'fixed';
        modal.style.top = '0';
        modal.style.left = '0';
        modal.style.width = '100vw';
        modal.style.height  = '100vh';
        modal.style.background = 'rgba(0,0,0,0.7)';   // slightly darker for error context
        modal.style.display  = 'flex';
        modal.style.alignItems = 'center';
        modal.style.justifyContent = 'center';
        modal.style.zIndex = '9999';
        

        // We map each incorrectly placed card to a row showing its logo, name, and wrong bin
        const imageGrid = incorrectImages.map(img =>
            `<div style="display:flex;align-items:center;gap:12px;margin:10px 0;padding:10px;background:rgba(255,100,100,0.15);border-radius:8px;">
                <img src="${img.src}" alt="${img.name}" style="width:50px;height:50px;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.2);">
                <div style="text-align:left;">
                    <div style="font-weight:700;color:#ff6b6b;font-size:1.05rem;">${img.name}</div>
                    <div style="font-size:0.9rem;color:#ffb3b3;">Currently in: ${img.currentBin}</div>
                </div>
            </div>`
        ).join('');

        // We use singular or plural phrasing depending on the number of mistakes
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


    // VALIDATION & SUBMIT

    // This sends the player's time to the server and refreshes the leaderboard to show the new score immediately. 
    async function submitTime(username, elapsed) {
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

            // We pull fresh leaderboard data now that the new score is in the database
            fetchLeaderboard(5);
        } catch (err) {
            // We alert the player so they know the save failed and can try again
            alert('Failed to save your score. Please try again.');
        }
    }

    // This checks that every source in the current round has been placed in a bin.
    // We return false and show an alert if any sources are still sitting in the image tray.
    function checkPlaced(placed) {
        // We count all source elements currently in the DOM
        const total = document.querySelectorAll('.image').length;

        if (placed.size < total) {
            // We tell the player exactly how many sources remain so they know what to look for
            alert(`Place all images first! (${placed.size}/${total})`);
            return false;
        }

        return true;
    }

    // This function checks each source against its correct bin to validate the player's placements
    // It iterates through all bins, then through all images in each bin, and finds mismatches
    // The result is used to provide specific feedback on which sources are wrong and where they are so the player can fix them
    function getWrong(binsList) {
        const incorrect = []; // This is an array to hold details of incorrectly placed sources

        binsList.forEach(bin => { // We iterate through each bin element
            bin.querySelectorAll('.image').forEach(img => { // For each image card in this bin
                // We check if the source's correct bin (data-bin) matches the bin it's currently in
                if (img.dataset.bin !== bin.dataset.bin) {
                    // The source is misplaced, so we collect its details for feedback
                    incorrect.push({
                        name: img.dataset.company, // This is the company name to display in the feedback modal
                        currentBin: bin.dataset.bin, // This is the bin where the source is currently placed (wrong)
                        src: img.src // This is the image source to show the outlet logo
                    });
                }
            });
        });

        return incorrect; // We return the list of incorrect placements
    }



    // EVENT WIRING


    // This attaches button handlers after HTML loads and initializes the game immediately so sources appear without waiting for images. 
    window.addEventListener('DOMContentLoaded', () => {

        // We build the first round immediately after the page HTML is parsed.
        startGame();

        // Reset Button: This clears the current board and starts a brand new game round (input=click)
        const resetBtn = document.getElementById('reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                // It rebuilds the tray, bins, and timer
                startGame();
            });
        }

        // Autofill Button: This automatically places every source into its correct bin
        const autofillBtn = document.getElementById('autofill-images');
        if (autofillBtn) {
            autofillBtn.addEventListener('click', () => {
                autofill(true);   // We pass true in order to signal the button was actually pressed (input=click)
            });
        }

        // Submit Button: This validates the current board and submits the score if correct (input=click)
        const submitBtn = document.getElementById('submit-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {

                // Checkpoint 1: Every source must be in a bin before other things like correctness, autofill usage, or started timer are checked

                if (!checkPlaced(placed)) return;

                // Checkpoint 2: All placed sources must be in their correct bins and if they aren't the feedback modal is displayed to show which sources are wrongly placed
                const incorrect = getWrong(document.querySelectorAll('.bin'));
                // If there are any mistakes, we show the feedback alert and stop submission
                if (incorrect.length > 0) {
                    showWrong(incorrect);
                    return; // Prevent further processing (score submission)
                }

                // Checkpoint 3: Autofill stops this run from appearing on the leaderboard and stops the timer
                if (autofilled) {
                    autofillWarn();
                    startGame();   // This start a fresh round after the player exists from the warning
                    return;
                }

                // Checkpoint 4: The timer must have been started by actual player interaction like dragging an icon to a bin
                if (!timer) {
                    alert("Timer not started. Please play the game first!");
                    return;
                }

                // All four gates passed: We stop the clock and capture the final time
                const elapsed = timer.stop();
                const username = window.currentPlayerUid || 'Guest';

                // We submit the score to the backend and refresh the leaderboard
                submitTime(username, elapsed);

                // We show the congratulations screen and immediately reset for a new round
                showCongrats(elapsed);
                startGame();
            });
        }
    });

    // PAGE SETUP

    // This runs after the full page loads. Window.onload sets up the player, draws the game board, loads the leaderboard, and refreshes scores every 30 seconds automatically.

    window.onload = () => {

        // We pull the authenticated username into currentPlayer
        getUser();
        // We show current top 5 standings as soon as the page is fully ready
        fetchLeaderboard(5);

        // We poll for updated standings every 30 seconds so new scores appear automatically
        setInterval(fetchLeaderboard, 30000, 5);
    };
</script>




