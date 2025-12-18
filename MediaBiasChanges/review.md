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
#Missing validation:
body = request.get_json()
rating = body.get('rating')  # If body is None, this crashes
#Added:
if not body:
    return {'message': 'Request body is required'}, 400

```

## College Board Component A Requirements: AI Chatbox


## College Board Component A Requirements: Thesis Generator


## College Board Component A Requirements: Citation Generator


## College Board Component A Requirements: Performace Rater



Split it up by person, each person shows their contribution (ex: citation generator) and code that shows one/two of the collegeboard requirements (ex: lists code block, shows how your code uses lists)
Follow explanation of requirement in your code with a demo of ur tool + how it uses that collegeboard requirement
And then how you debugged, used postman, your process

Show code blocks for ALL requirements (keep this concise) but you only TALK about one, show demo for like one or talk about how your requirements come together to make ur tool 


