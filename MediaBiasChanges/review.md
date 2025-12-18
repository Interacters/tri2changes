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

# AI Source Intel Chatbox

## AP CSP Component A Requirements

A comprehensive demonstration of fundamental computer science principles working together to create a functional AI chatbot for news analysis.

---

## Core Requirements

### 1. User Input

**Description:** Flask API receives POST requests from users clicking prompts

**Code Implementation:**

```python
# User clicks trigger events
class _IncrementClick(Resource):
    def post(self, id):
        prompt = increment_prompt_click(id)
        return jsonify(prompt)
```

**Impact:** Users interact with the AI chatbot by selecting pre-defined prompts, triggering real-time API calls

---

### 2. List Collection

**Description:** List stores 5 AI prompts, manages complexity of tracking user interactions

**Code Implementation:**

```python
prompt_list = [
    "What is the political bias of {source}?",
    "Show me recent top stories from {source}",
    # ... 3 more prompts
]
```

**Impact:** The list structure enables dynamic prompt management and scalability

---

### 3. Custom Procedure

**Description:** increment_prompt_click() with parameters, return type, and algorithm

**Code Implementation:**

```python
def increment_prompt_click(id):
    """Atomically increment clicks"""
    with open(PROMPTS_FILE, 'r+') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        prompts = json.load(f)
        
        for prompt in prompts:
            if prompt['id'] == id:
                prompt['clicks'] += 1
                break
        
        f.seek(0)
        json.dump(prompts, f)
        f.truncate()
    
    return getPrompt(id)
```

**Impact:** Uses file locking for thread-safe operations, preventing data corruption

---

### 4. Algorithm (Sequencing, Selection, Iteration)

**Description:** Complete algorithm with all three components

**Code Implementation:**

```python
# SEQUENCING: Step-by-step execution
fcntl.flock(f, fcntl.LOCK_EX)
prompts = json.load(f)

# ITERATION: Loop through prompts
for prompt in prompts:
    # SELECTION: Conditional check
    if prompt['id'] == id:
        prompt['clicks'] += 1
        break
```

**Impact:** Ensures accurate click tracking across concurrent user requests

---

### 5. Procedure Calls

**Description:** API routes call custom procedures throughout the system

**Code Implementation:**

```python
# Multiple calls to procedures
class _IncrementClick(Resource):
    def post(self, id):
        prompt = increment_prompt_click(id)
        # Calls getPrompt(id) internally
        return jsonify(prompt)

class _ReadClicks(Resource):
    def get(self):
        return jsonify(getPromptClicks())
```

**Impact:** Modular design enables code reusability and maintainability

---

### 6. Output

**Description:** JSON responses display click data and prompt information

**Code Implementation:**

```python
# Returns visual/textual output
return jsonify({
    "id": 1,
    "text": "What is the political bias?",
    "clicks": 8
})
```

**Impact:** Real-time feedback shows users which prompts are most popular

---

## Development & Debugging Journey using Postman

### Common Errors Encountered and Fixed

#### 1. Function Name Mismatch

**Error:** Called `_increment_prompt_click()` in `prompt.py` but function was named `increment_prompt_click()` in `prompts.py`

- **Symptom:** Function not found error
- **Fix:** Removed underscore prefix to make it public

#### 2. Missing Blueprint Registration

**Error:** Forgot to register `prompt_api` in `main.py`

- **Symptom:** 404 Not Found when testing `/api/prompts`
- **Fix:** Added `app.register_blueprint(prompt_api)`

#### 3. Missing Initialization

**Error:** Didn't call `initPrompts()` on server startup

- **Symptom:** `prompts.json` file never created
- **Fix:** Added `initPrompts()` to the `with app.app_context():` block

#### 4. Wrong Import Order

**Error:** Imported `initPrompts` before `prompt_api` in `main.py`

- **Symptom:** Potential circular import or function not defined
- **Fix:** Organized imports properly (data functions before API blueprints)

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

| Requirement | Location | Specific Code Lines | Explanation |
|---|---|---|---|
| **Input from user** | `citation-generator.html` | `<input id="cite-author">` `<input id="cite-title">` `<select id="cite-style">` `document.getElementById('generate-btn').addEventListener('click', generate)` | Users enter author, title, date, source, and URL fields; select citation style from dropdown (APA/MLA/Chicago); click generate button |
| **Input from online source** | Flask backend + frontend fetch | `const response = await fetch('/api/media/fetch_meta?url=' + encodeURIComponent(url))` `const data = await response.json()` | Fetches article metadata (title, author, date) from real URLs via Flask proxy endpoint |
| **List/Collection Type** | Frontend JavaScript | `JSON.parse(localStorage.getItem(KEY) || '[]')` `let saved = getSavedCitations();` | Citations stored as array of objects in localStorage; each citation object contains style, formatted text, and metadata |
| **List manages complexity** | Frontend JavaScript | `processCitationList(saved, 'all', 100)` `const result = processCitationList(saved, filterValue, 100);` | Abstracts filtering by citation style, limits display items, and counts citations per style without exposing implementation details |
| **Procedure name** | Frontend JavaScript | `function processCitationList(citationList, filterStyle, maxItems)` `let filtered = [];` `let styleCount = { apa: 0, mla: 0, chicago: 0 };` | Function named `processCitationList` |
| **Procedure parameters** | Frontend JavaScript | `function processCitationList(citationList, filterStyle, maxItems)` | Three parameters: citationList (array of citation objects), filterStyle (string for filtering), maxItems (number for display limit) |
| **Procedure return type** | Frontend JavaScript | `return { citations: filtered, totalCount: citationList.length, styleCounts: styleCount };` | Returns object containing filtered array, total count number, and style counts object |
| **Algorithm: Sequencing** | `generate()` function | `const payload = { author: safe(authorEl.value), date: safe(dateEl.value), ... };` `if (!payload.title) { warnings.push('Missing title') }` `if (style === 'mla') citation = fmtMLA9(payload);` `outputEl.innerHTML = citation;` | Steps execute in order: read input → validate fields → format citation → display output → show parenthetical → display warnings |
| **Algorithm: Selection** | Formatting logic | `if (style === 'mla') citation = fmtMLA9(payload);` `else if (style === 'chicago') citation = fmtChicago(payload);` `else citation = fmtAPA(payload);` | Conditional logic switches between citation styles; also handles missing authors with fallback to title |
| **Algorithm: Iteration** | Rendering saved citations | `result.citations.forEach((item, index) => { const citationDiv = document.createElement('div'); citationDiv.innerHTML = item.citation; savedList.appendChild(citationDiv); });` | Loops through filtered citations array to create and display multiple citation cards |
| **Procedure calls** | `loadSavedCitations()` function | `const result = processCitationList(saved, filterValue, 100);` `result.citations.forEach((item) => { ... })` | Calls processCitationList to filter/process citations, then iterates result to render UI |
| **Output: Visual** | DOM manipulation | `outputEl.innerHTML = citation;` `parentheticalEl.textContent = parenthetical;` `savedList.appendChild(citationDiv);` | Displays formatted citation in styled div, shows parenthetical reference, renders Works Cited list |
| **Output: Textual** | Status messages | `warningsEl.textContent = warnings.join('; ');` `statusEl.textContent = '✅ Citation copied to clipboard!';` `alert('Citation saved!')` | Shows validation warnings, clipboard confirmation, save notifications |
| **Output based on input** | Formatting functions | `function fmtAPA(p) { ... }` `function fmtMLA9(p) { ... }` `function fmtChicago(p) { ... }` | Output format varies based on user's selected citation style and entered metadata fields |

---

## Input from User
Input is collected through multiple form interaction methods:
1. Text input fields capture author, title, publication date, source, and URL strings
2. Dropdown selection for citation style (APA, MLA 9, Chicago)
3. Button clicks trigger different actions: Generate (formats citation), Save (stores to localStorage), Reset (clears form), Load (displays saved citations)
4. URL input triggers automatic metadata fetch from online sources

---

## Student-Developed Procedure (Abstraction)

### Function: `processCitationList`

**Purpose:**  
Processes a list of saved citations by filtering them by citation style, limiting the number displayed, and counting how many citations exist for each style. This abstraction prevents repeated logic and simplifies rendering the Works Cited list.

```javascript
function processCitationList(citationList, filterStyle, maxItems) {
    let filtered = [];
    let styleCount = { apa: 0, mla: 0, chicago: 0 };

    for (let i = 0; i < citationList.length; i++) {
        let citation = citationList[i];

        // Count all citations by style
        if (citation.style && styleCount.hasOwnProperty(citation.style)) {
            styleCount[citation.style]++;
        }

        // Filter by selected style
        if (filterStyle === 'all' || citation.style === filterStyle) {
            filtered.push(citation);
        }

        // Limit display items
        if (filtered.length >= maxItems) {
            break;
        }
    }

    return {
        citations: filtered,
        totalCount: citationList.length,
        styleCounts: styleCount
    };
}
```

**Parameters:**
- `citationList` (array): Complete list of saved citation objects
- `filterStyle` (string): Citation style to filter by ('all', 'apa', 'mla', 'chicago')
- `maxItems` (number): Maximum number of citations to return

**Returns:** Object containing:
- `citations`: Filtered array of citation objects
- `totalCount`: Total number of saved citations
- `styleCounts`: Object with counts for each citation style

---

## Algorithms in the Program

### Sequencing
Seen clearly in `generate()` function:

```javascript
// 1. Read user input
const payload = {
    author: safe(authorEl.value),
    date: safe(dateEl.value),
    title: safe(titleEl.value),
    source: safe(sourceEl.value),
    url: safe(urlEl.value)
};

// 2. Validate missing fields
let warnings = [];
if (!payload.title) warnings.push('Missing title');
if (!payload.author) warnings.push('Missing author');

// 3. Format citation based on style
let citation;
if (style === 'mla') citation = fmtMLA9(payload);
else if (style === 'chicago') citation = fmtChicago(payload);
else citation = fmtAPA(payload);

// 4. Display citation
outputEl.innerHTML = citation;

// 5. Display parenthetical citation
parentheticalEl.textContent = parenthetical;

// 6. Show warnings if needed
if (warnings.length > 0) {
    warningsEl.textContent = warnings.join('; ');
}
```

### Selection
Used to switch citation styles and handle missing authors:

```javascript
// Style selection
if (style === 'mla') citation = fmtMLA9(payload);
else if (style === 'chicago') citation = fmtChicago(payload);
else citation = fmtAPA(payload);

// Missing author handling
if (!author) {
    return `<i>${title}</i>. (${date}). ${source}.`;
}
```

### Iteration
Used to render saved citations and process lists:

```javascript
result.citations.forEach((item, index) => {
    const citationDiv = document.createElement('div');
    citationDiv.className = 'saved-citation';
    citationDiv.innerHTML = item.citation;
    savedList.appendChild(citationDiv);
});
```

---

## Backend Integration (Flask)

The Flask backend provides a proxy metadata endpoint to avoid browser CORS restrictions:

```python
@media_api.route('/fetch_meta')
def fetch_meta():
    target = request.args.get('url')
    if not target:
        return jsonify({'error': 'missing url'}), 400
    
    try:
        response = requests.get(target, timeout=5)
        # Parse metadata from HTML
        # Return title, author, date
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

---

## Debugging & Iterative Development

### Problem 1: CORS Errors
**Issue:** Direct fetch from news sites failed; browser blocked cross-origin requests (security policy)

**Fix:**
- Added Flask proxy endpoint (backend)
- Added `flask_cors.CORS` to allow frontend requests
- Added AllOrigins fallback in case server fetch fails

```python
from flask_cors import CORS
CORS(media_api, resources={r"/*": {"origins": "http://localhost:4600"}})
```

### Postman Debugging
**Process:**
- Used Postman to confirm problem was NOT with the URL
- Repeated testing of GET request to verify article metadata was received from article URL
- Identified error handling issues:
  - **400 Bad Request** (Missing or invalid JSON)
  - Code assumed `request.get_json()` always returned a dictionary
  - When no JSON body was sent, `None.get()` caused server error

<p align="center">
  <img src="../images/Debugging-evidence.png" alt="Debugging Evidence: Postman" width="600">
</p>

<p align="center">
  <img src="../images/Postman-success.png" alt="Postman Success: 200 OK" width="600">
</p>

**Fix:**
```python
body = request.get_json()

if not body:
    return {'message': 'Request body is required'}, 400
```

### Console Debugging - Verifying Logic Flow
Used `console.log()` statements throughout to:
- Confirm button clicks were firing
- Verify URLs were being passed correctly to the fetch call
- Inspect data returned from server before formatting citations

**Example:**
```javascript
console.log("Fetching metadata for:", url);
fetch('/api/media/fetch_meta?url=' + encodeURIComponent(url))
    .then(response => response.json())
    .then(data => {
        console.log("Received metadata:", data);
        // Populate form fields
    });
```
<p align="center">
  <img src="../images/Console-debug-fetch-success.png" alt="Console Debug Fetch Success" width="600">
</p>

<p align="center">
  <img src="../images/Network-debug-fetch-from-endpoint.png" alt="Network Debug Fetch from Endpoint" width="600">
</p>


## College Board Component A Requirements: Performance Rater

College Board Component A Requirements: Performance Rater
Overview
The Performance Rater collects student self-assessments (ratings 1-5), stores responses in a database, calculates class averages, and provides personalized feedback with educational resources. It allows users to submit ratings through a frontend interface. Those inputs are sent to a backend system that processes and stores the data. The program then analyzes the collected ratings and displays aggregated results back to the user. This demonstrates College Board requirements by using input, data storage, processing, and output working together in one system.

| Requirement | Location | Specific Code Lines | Explanation |
|-------------|----------|---------------------|-------------|
| **Input from user** | `mediabias_sub2.md` | `document.getElementById('survey-form').addEventListener('submit', async (e) => { ... })` `const rating = document.querySelector('input[name="rating"]:checked');` | User selects rating (1-5) via radio buttons, clicks "Submit Rating" button |
| **Input from file** | `api/performance_api.py` | `body = request.get_json()` `rating = body.get('rating')` | Reads JSON data from HTTP request body containing student's performance rating |
| **List/Collection Type** | `mediabias_sub2.md` | `const resourcesByTier = { 1: { title: "Building Foundations", items: [{ text: "Grammarly Handbook", url: "..." }] } }` | Nested dictionary containing 5 tiers, each with array of 5-6 resource objects (30+ total resources) |
| **List manages complexity** | `mediabias_sub2.md` | `const resources = resourcesByTier[data.your_rating];` `resourcesList.innerHTML = resources.items.map(item => '<div>...</div>').join('');` | Direct dictionary lookup retrieves tier; single map() generates HTML for all resources dynamically |
| **Procedure name** | `mediabias_sub2.md` | `function showResults(data)` `const badgeColors = { ... };` `document.getElementById('result-badge').innerHTML = ...;` | Function named `showResults` |
| **Procedure parameters** | `mediabias_sub2.md` | `function showResults(data)` | One parameter: data (object containing status, your_rating, average_rating, message) |
| **Procedure return type** | `mediabias_sub2.md` | No explicit return statement | Returns `undefined` (performs DOM manipulation side effects) |
| **Algorithm: Sequencing** | `mediabias_sub2.md` | `const badgeColors = { ... };` → `document.getElementById('result-badge').innerHTML = ...;` → `document.getElementById('results-modal').style.display = 'block';` | Steps execute in order: map colors → set badge → set title → load resources → render HTML → show modal |
| **Algorithm: Selection** | `mediabias_sub2.md` | `if (!rating) { alert('Please select a rating'); return; }` | Conditional logic validates form completion before allowing submission |
| **Algorithm: Iteration** | `mediabias_sub2.md` | `resources.items.map(item => '<div class="resource-item"><a href="${item.url}">${item.text}</a></div>').join('')` | Loops through resources.items array (5-6 items) to generate HTML for each resource link |
| **Procedure calls** | `mediabias_sub2.md` | `const data = await response.json();` `if (response.ok) { showResults(data); }` | Calls showResults procedure with API response data after successful submission |
| **Output: Visual** | `mediabias_sub2.md` | `document.getElementById('results-modal').style.display = 'block';` `<span class="result-badge ${badgeColors[data.status]}">` | Displays modal overlay, color-coded badges (red/yellow/green), statistics cards, resource links |
| **Output: Textual** | `mediabias_sub2.md` | `document.getElementById('result-title').textContent = titles[data.status];` `document.getElementById('result-message').textContent = data.message;` | Shows performance title ("Let's Build Your Skills!"), personalized feedback message |
| **Output based on input** | Backend + Frontend | Backend: `if rating < avg_rating - 0.5: status = 'underprepared'` Frontend: `const resources = resourcesByTier[data.your_rating];` | Backend determines status based on rating comparison; frontend displays tier-specific resources |

List/Collection Type
The Performance Rater uses a nested dictionary structure to organize educational resources by performance tier:

```javascript
const resourcesByTier = {
    1: {
        title: 'Building Foundations',
        intro: 'Start with these fundamentals to strengthen your English skills:',
        items: [
            { text: 'Grammarly Handbook - Grammar Basics', url: 'https://www.grammarly.com/blog/category/handbook/' },
            { text: 'Khan Academy Grammar Course (Free)', url: 'https://www.khanacademy.org/humanities/grammar' },
            { text: 'Basic Essay Structure (YouTube)', url: 'https://www.youtube.com/watch?v=sQEr5D1sSrU' }
        ]
    },
    2: {
        title: 'Developing Skills',
        items: [
            { text: 'MLA Citation Guide - Purdue OWL', url: 'https://owl.purdue.edu/...' },
            { text: 'Hemingway Editor - Improve Clarity', url: 'https://www.hemingwayapp.com/' }
        ]
    }
    // ... tiers 3-5
};
```

**Why this is a collection:**

- Main dictionary contains 5 performance tiers (keys: 1-5)
- Each tier has an items array containing 5-6 resource objects
- Each resource object has text and url properties
- Total: 30+ resources organized hierarchically

List Manages Complexity

```javascript
function showResults(data) {
    const resources = resourcesByTier[data.your_rating];
    
    const resourcesList = document.getElementById('resources-list');
    resourcesList.innerHTML = resources.items.map(item => 
        `<div class="resource-item">
            <a href="${item.url}" target="_blank">${item.text}</a>
        </div>`
    ).join('');
}
```
**Benefits:**

- No conditional chains - Direct dictionary access instead of 5 if-else blocks
- Scalable - Adding tiers requires only data updates, no code changes
- Dynamic rendering - Single .map() handles 5-30 links regardless of tier
- Maintainable - Resource updates happen in data structure, not logic

The list approach reduces 150+ lines of repeated code to 5 lines that handle all 30+ resources dynamically.

**Debugging Process**
Example 1: Missing JSON Key Error
Problem: Frontend received 400 Bad Request error from backend
Tool Used: Chrome DevTools Network Tab
Brief Explanation:
When submitting the rating form, the backend rejected the request with a 400 error. Using Chrome DevTools Network tab, I inspected the POST request payload and discovered the frontend was sending { value: 3 } while the backend expected { rating: 3 }. The backend's validation logic checked for a rating key, so when it received value instead, it returned an error message "rating is required". Changing the JSON key from value to rating in the frontend code resolved the issue.
Fix:

```javascript
// Before (WRONG):
body: JSON.stringify({ value: parseInt(rating.value) })

// After (CORRECT):
body: JSON.stringify({ rating: parseInt(rating.value) })
```

Example 2: Modal Not Displaying Resources
Problem: Results modal showed up blank with no resource links
Tool Used: Console.log() debugging
Process:

Added console logs to trace data flow:

```javascript
function showResults(data) {
    console.log('Received data:', data);
    console.log('Rating tier:', data.your_rating);
    console.log('Type of rating:', typeof data.your_rating);
    
    const resources = resourcesByTier[data.your_rating];
    console.log('Resources object:', resources);
    
    if (!resources) {
        console.error('No resources found for tier:', data.your_rating);
    }
}

2. Console output revealed:
Received data: {your_rating: "3", status: "average", ...}
Rating tier: "3"
Type of rating: string
Resources object: undefined
``
```
Discovery: Backend returned your_rating as a string "3" instead of number 3. The resourcesByTier dictionary used numeric keys, so resourcesByTier["3"] returned undefined.
Fix:
```javascript
const data = await response.json();
data.your_rating = parseInt(data.your_rating); // Convert string to number
showResults(data);
```

**Postman Debugging**

1. Incorrect API Route (Endpoint Error)
Error:
The frontend was calling /api/data, but the backend route was actually /api/info.
How Postman helped:
I tested the GET request in Postman and got a 404 Not Found, which told me the route didn’t exist.
Fix:
I corrected the endpoint path in the frontend to match the backend route.

2. Wrong HTTP Method (GET vs POST)
Error:
The frontend sent a GET request to an endpoint that expected POST.
How Postman helped:
When I tried GET in Postman, the server returned an error, but POST worked correctly.
Fix:
I updated the frontend to use the correct HTTP method.

3. CORS or Credential Issues
Error:
The frontend couldn’t access the API due to CORS restrictions.
How Postman helped:
Requests worked in Postman but failed in the browser, showing it was a CORS issue.
Fix:
I enabled CORS in the backend to allow frontend requests.

<img width="318" height="718" alt="Image" src="https://github.com/user-attachments/assets/1c4fb879-6fc1-42ed-8e28-3ba27653da8a" />

<img width="262" height="306" alt="Image" src="https://github.com/user-attachments/assets/89603e03-57d0-42e7-97bd-45ef8d46f2e1" />




