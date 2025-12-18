---
layout: post
title: Review 12/17
permalink: /review/
date: 2025-12-17
---

## College Board Component A Requirements: Media

| Requirement | Location | Specific Code Lines | Explanation |
|---|---|---|---|
| **Input from user** | `Mediachat.md` | `img.addEventListener('dragstart', (e) => { ... })` `document.getElementById('login-btn').addEventListener('click', async () => { ... })` `document.getElementById('submit-btn')` | User drags images (trigger events), enters login credentials, clicks buttons |
| **Input from file** | `api/user.py` lines 35-40 | `body = request.get_json()` `name = body.get('name')` `uid = body.get('uid')` `password = body.get('password')` | Reads JSON data from HTTP request body containing user signup information |
| **List/Collection Type** | `Mediachat.md` | `const imageFiles = [ { src: "atlanticL.png", company: "Atlantic", bin: "Left" }, ... ]` `let placedImages = new Set();` | Array of 30+ objects storing media source data; Set tracking placed images |
| **List manages complexity** | `Mediachat.md` | `const leftImages = imageFiles.filter(img => img.bin === "Left");` `selectedImages = [ ...getRandomSubset(leftImages, 7), ... ]` | Filters sources by bias category, randomly selects 21 images per game, manages game state |
| **Procedure name** | `Mediachat.md` | `function createImageCard(file, index)` `const img = document.createElement('img');` `img.src = IMAGE_BASE + file.src;` `img.alt = file.company;` `img.className = 'image';` `img.draggable = true;` `img.dataset.bin = file.bin;` `img.dataset.company = file.company;` `img.dataset.id = slugify(file.company);` | Function named `createImageCard` |
| **Procedure parameters** | `Mediachat.md` | `function createImageCard(file, index)` | Two parameters: file (object with image data), index (number) |
| **Procedure return type** | `Mediachat.md` | `return img;` (line in createImageCard) | Returns HTMLImageElement (img DOM node) |
| **Algorithm: Sequencing** | `Mediachat.md` createImageCard | `const img = document.createElement('img');` `img.src = IMAGE_BASE + file.src;` `img.alt = file.company;` `img.className = 'image';` `img.draggable = true;` | Steps execute in specific order: create element, set source, set alt text, add class, enable dragging |
| **Algorithm: Selection** | `Mediachat.md` createImageCard | `if (!gameStarted) { gameStarted = true; timerHandle = startTimer(); }` | Conditional logic - only starts timer on first drag interaction |
| **Algorithm: Iteration** | `Mediachat.md` | `selectedImages.forEach((file) => { const card = createImageCard(file); imagesArea.appendChild(card); });` | Loops through selected images array to create cards |
| **Procedure calls** | `Mediachat.md` initGame | `const card = createImageCard(file);` (inside forEach loop) | Called for each image in selectedImages array during game initialization |
| **Output: Visual** | `Mediachat.md` | `imagesArea.appendChild(card);` `bin.querySelector('.bin-content').appendChild(img);` `timerDisplay.textContent = 'Time: ${minutes}:${secs}'` | Displays draggable images, updates timer, shows leaderboard |
| **Output: Textual** | `Mediachat.md` | `playerDisplay.textContent = 'Player: ${currentPlayer}';` `alert('Completed in ${minutes}:${seconds}!');` | Shows player name, completion time messages |
| **Output based on input** | `Mediachat.md` submitBtn handler | `if (img.dataset.bin !== bin.dataset.bin) { incorrectImages.push(...) }` `showIncorrectFeedback(incorrectImages);` | Validates user placements, provides feedback based on drag-and-drop actions |

#### **Input from User**
Input is collected through multiple user interaction methods: 
1.  Drag-and-drop events trigger game timer and move images between bins, passing image IDs through dataTransfer API 
2. Text input from login/signup forms captures username and password strings 
3. Button clicks on Submit, Reset, Autofill, and Sign In trigger different game actions and API calls. 

#### **Procedure**
Function named createImageCard 
- It takes a media source object and adds visual properties, drag functionality, data attributes for validation, and event handlers. 
- The procedure manages 9+ property assignments and 2 event listeners
- This allows the game to create 21 unique image cards by calling createImageCard(file) instead of duplicating 15+ lines of code 21 times

```javascript
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

```

### Debugging Evidence: API Endpoint Development

| Screenshot | Issue | Debugging Process | Solution | Evidence of Learning |
|---|---|---|---|---|
| ![Image 1](https://github.com/user-attachments/assets/b4c63065-42ab-4db8-a850-4c42574060d5) | POST request to `/api/performance/submit` returns `500 INTERNAL SERVER ERROR` | Testing endpoint with JSON body `{"rating": 4}` in Postman reveals server error | Response: `500 INTERNAL SERVER ERROR` in 18ms - indicates backend code has bug, likely missing error handling or database issue | Initial testing reveals backend implementation problem - endpoint exists but crashes when processing request |
| ![Image 2](https://github.com/user-attachments/assets/015c4b3c-c717-4766-a197-17dcec68f648) | Same request now returns `200 OK` after debugging | Fixed backend code. Added proper error handling and validation | Returns `200 OK` in 160ms (84.59 KB) - successfully processes the rating data | Shows successful debugging and identified missing validation, added try-catch blocks, fixed database operations. Slower response time indicates more robust processing (validation + database operations) |

---

### Initial Failure (Image 1)
**What Broke:**
- Endpoint: `POST http://localhost:8001/api/performance/submit`
- Request format: JSON body with `{"rating": 4}`
- Response: `500 INTERNAL SERVER ERROR` in 160ms
- Status: Backend code exists but has implementation bug

**Backend Issues:**

```python
# Found the missing validation:
body = request.get_json()
rating = body.get('rating')  # If body is None then this crashes
# I Added:
if not body:
    return {'message': 'Request body is required'}, 400

```

## College Board Component A Requirements: AI Chatbox


## College Board Component A Requirements: Thesis Generator


| Requirement | Location | Specific Code Lines | Explanation |
|---|---|---|---|
| **Input from user** | Thesis Generator HTML/JS | `document.getElementById('thesis-topic').value.trim()` `document.getElementById('thesis-position').value.trim()` `document.getElementById('thesis-generate').addEventListener('click', generateThesis)` | User enters topic and position text, selects thesis type from dropdown, clicks generate button |
| **Input from file** | `generateThesis()` function | `const response = await fetch('${API_BASE}/api/thesis/generate', {...})` `const result = await response.json();` `if (!result.success \|\| !result.data) { throw new Error(...) }` | Reads JSON data from API response containing generated thesis statements, strength ratings, and recommendations |
| **List/Collection Type** | `generateThesis()` function | `const pointInputs = document.querySelectorAll('.thesis-supporting-point');` `const supportingPoints = Array.from(pointInputs).map(input => input.value.trim()).filter(point => point.length > 0);` | NodeList of input elements converted to Array, storing user's supporting points with filtering |
| **List manages complexity** | `displayTheses()` function | `data.theses.forEach((thesis) => { ... })` `thesis.supportingArguments.map(arg => '<li>${arg}</li>').join('')` | Iterates through multiple thesis objects, dynamically generates HTML cards for each with nested arrays for arguments |
| **Procedure name** | Thesis Generator JS | `function displayTheses(data)` `const card = document.createElement('div');` `card.className = 'thesis-card';` `card.innerHTML = '...'` `thesisOutput.appendChild(card);` | Function named `displayTheses` |
| **Procedure parameters** | `displayTheses()` | `function displayTheses(data)` | One parameter: data (object containing array of thesis objects with statements, strength ratings, and supporting/counter arguments) |
| **Procedure return type** | `displayTheses()` | No explicit return statement (returns `undefined`) | Procedure performs side effects (DOM manipulation) rather than returning a value |
| **Algorithm: Sequencing** | `displayTheses()` function | `thesisOutput.innerHTML = '';` `data.theses.forEach(...)` `const card = document.createElement('div');` `card.className = 'thesis-card';` `card.innerHTML = '...';` `thesisOutput.appendChild(card);` | Steps execute in specific order: clear output area, iterate theses, create card element, set class, populate content, append to DOM |
| **Algorithm: Selection** | `displayTheses()` function | `const strengthClass = thesis.strength >= 8 ? 'thesis-strength-high' : thesis.strength >= 6 ? 'thesis-strength-medium' : 'thesis-strength-low';` | Conditional logic using ternary operators to assign CSS class based on strength score ranges |
| **Algorithm: Iteration** | `displayTheses()` function | `data.theses.forEach((thesis) => { const card = document.createElement('div'); ... thesisOutput.appendChild(card); });` | Loops through theses array to create and display multiple thesis cards |
| **Procedure calls** | `generateThesis()` function | `displayTheses(result.data);` `showThesisStatus('✅ Thesis statements generated successfully!', 'success');` | Calls displayTheses to render results and showThesisStatus to provide user feedback after API response |
| **Output: Visual** | `displayTheses()` function | `thesisOutput.appendChild(card);` `<span class="thesis-strength-badge ${strengthClass}">Strength: ${thesis.strength}/10</span>` `outputSection.style.display = 'block';` | Displays thesis cards with color-coded strength badges, supporting arguments lists, and counterarguments |
| **Output: Textual** | `showThesisStatus()` function | `statusDiv.textContent = message;` `showThesisStatus('✅ Thesis statements generated successfully!', 'success');` `showThesisStatus('❌ Error: ' + error.message, 'error');` | Shows success/error messages, displays thesis statements, strength explanations, and recommendations |
| **Output based on input** | `generateThesis()` function | `if (!topic \|\| !position) { showThesisStatus('Please fill in both Topic and Position fields', 'error'); return; }` `body: JSON.stringify({ topic: topic, position: position, ... })` `displayTheses(result.data);` | Validates user inputs, sends to API, displays customized thesis statements based on user's topic, position, and selected type |

#### **Input from User**
Input is collected through multiple form interaction methods:
1. Text input fields capture topic and position strings that form the basis of thesis generation
2. Dynamic supporting points array allows users to add/remove bullet points via buttons
3. Dropdown selection for thesis type (Argumentative, Analytical, Expository, etc.)
4. Optional audience targeting field for tone customization
5. Generate and Clear buttons trigger API calls and form reset actions

#### **Procedure**
Function named `displayTheses`
- Takes a data object containing an array of thesis objects with strength ratings, statements, arguments, and counterarguments
- Dynamically creates HTML card elements for each thesis with color-coded strength badges
- Handles conditional rendering of supporting arguments and counterarguments lists when present
- This allows the application to display 3+ thesis variations by calling `displayTheses(data)` instead of manually writing repetitive DOM manipulation code

```javascript
function displayTheses(data) {
    const thesisOutput = document.getElementById('thesis-output');
    const recommendationsOutput = document.getElementById('thesis-recommendations');
    
    thesisOutput.innerHTML = '';

    if (!data.theses || data.theses.length === 0) {
        thesisOutput.innerHTML = '<p>No theses generated. Please try again.</p>';
        return;
    }

    data.theses.forEach((thesis) => {
        const strengthClass = thesis.strength >= 8 ? 'thesis-strength-high' : 
                             thesis.strength >= 6 ? 'thesis-strength-medium' : 'thesis-strength-low';
        
        const card = document.createElement('div');
        card.className = 'thesis-card';
        card.innerHTML = `
            <div class="thesis-statement">${thesis.statement}</div>
            <span class="thesis-strength-badge ${strengthClass}">Strength: ${thesis.strength}/10</span>
            <p style="color: #c8d7eb; margin-top: 10px; font-size: 0.9rem;">${thesis.strengthExplanation}</p>
            
            ${thesis.supportingArguments && thesis.supportingArguments.length > 0 ? `
                <div class="thesis-details">
                    <h5>Supporting Arguments</h5>
                    <ul>
                        ${thesis.supportingArguments.map(arg => `<li>${arg}</li>`).join('')}
                    </ul>
                </div>
            ` : ''}
            
            ${thesis.counterarguments && thesis.counterarguments.length > 0 ? `
                <div class="thesis-details">
                    <h5>Counterarguments to Address</h5>
                    <ul>
                        ${thesis.counterarguments.map(counter => `<li>${counter}</li>`).join('')}
                    </ul>
                </div>
            ` : ''}
            
            <button class="thesis-btn-use" data-statement="${thesis.statement.replace(/"/g, '&quot;')}">
                Use This Thesis
            </button>
        `;
        
        thesisOutput.appendChild(card);
    });

    // Add event listeners to "Use This Thesis" buttons
    document.querySelectorAll('.thesis-btn-use').forEach(btn => {
        btn.addEventListener('click', function() {
            const statement = this.getAttribute('data-statement');
            useThesis(statement);
        });
    });

    if (data.recommendations) {
        recommendationsOutput.innerHTML = `
            <div class="thesis-recommendations">
                <h5>Recommendations</h5>
                <p>${data.recommendations}</p>
            </div>
        `;
    }
}
```

## College Board Component A Requirements: Citation Generator


## College Board Component A Requirements: Performace Rater



Split it up by person, each person shows their contribution (ex: citation generator) and code that shows one/two of the collegeboard requirements (ex: lists code block, shows how your code uses lists)
Follow explanation of requirement in your code with a demo of ur tool + how it uses that collegeboard requirement
And then how you debugged, used postman, your process

Show code blocks for ALL requirements (keep this concise) but you only TALK about one, show demo for like one or talk about how your requirements come together to make ur tool 


