---
layout: post
title: Game Features Improvement Plan
permalink: /mediabias_plans
author: Interacters
---

# Game Features Improvement Plan

*Transforming Media Bias Game into an Engaging, Interactive Experience*

---

## Backend-Driven Leaderboard System

*A robust, competitive leaderboard that tracks player performance in real-time, encouraging replayability and social competition.*

### **Key Benefits**
- Fair Competition: Server-side validation prevents cheating
- Real-time Updates: Instant leaderboard refresh after each game
- Persistent Records: Historical tracking of all player attempts
- Time-based Ranking: Fastest completion times rise to the top

---

### Frontend Submission (time-based, using javaURI)

*Integration Point: Call this function when the player successfully completes the game.*

Use the javaURI import already on the page (or replace with relative path if needed):

```javascript
// Example to POST time-based score (seconds)
// Use this form in the frontend where you finalize the game
async function submitFinalTime(username, seconds) {
  // Path-param style (matches mediabias_sub2's current pattern if you want to keep it)
  await fetch(`${javaURI}/api/media/score/${encodeURIComponent(username)}/${seconds}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }
  });

  // OR: JSON body style (backend should accept either)
  // await fetch(`${javaURI}/api/media/score`, {
  //   method: 'POST',
  //   headers: { 'Content-Type': 'application/json' },
  //   body: JSON.stringify({ user: username, time: seconds })
  // });
}
```

---

### Backend Storage 

*Implementation Note: Choose the API style that best fits your existing backend architecture. Both approaches are equally valid.*

Two types of backend approaches. Although provided by AI we did our research on how this works.

```javascript
// Express examples
// Path-param style
app.post('/api/media/score/:user/:time', async (req, res) => {
  const user = req.params.user;
  const time = Number(req.params.time);
  if (!user || isNaN(time) || time < 0) return res.status(400).json({ error: 'Invalid data' });

  await db.leaderboard.insertOne({ username: user, time, date: new Date() });
  res.json({ ok: true });
});

// JSON body style
app.post('/api/media/score', async (req, res) => {
  const { user, time } = req.body;
  if (!user || typeof time !== 'number' || time < 0) return res.status(400).json({ error: 'Invalid data' });

  await db.leaderboard.insertOne({ username: user, time, date: new Date() });
  res.json({ ok: true });
});
```

---

### Frontend Leaderboard Display (fetch sorted by fastest time)

*Display Strategy: Update the leaderboard after each game completion, highlighting the current player's rank if they made the top 10.*

```javascript
// GET top 10 fastest times (lower time is better)
const res = await fetch(`${javaURI}/api/media/leaderboard`);
const scores = await res.json(); // expect sorted by time ascending
render(scores);
```

---

### Backend Leaderboard Route (sorted by time ascending)

*Performance Tip: Consider adding database indexing on the time field for faster queries as your leaderboard grows.*

```javascript
app.get('/api/media/leaderboard', async (req, res) => {
  const top = await db.leaderboard.find().sort({ time: 1 }).limit(10).toArray();
  res.json(top);
});
```

---

## Timed Win Condition 

*Add urgency and competitive depth by tracking how quickly players can correctly categorize all news sources.*

**Goal:** Start a timer when the round begins (or on first drag), stop when every source is placed correctly, send seconds to backend.

### Implementation Strategy
1. **Timer Start** — Trigger on game initialization or first user interaction
2. **Timer Stop** — Trigger when all sources are correctly placed
3. **Data Submission** — Immediately send time to backend for leaderboard consideration
4. **User Feedback** — Display completion time prominently in success screen

---

### Timer Utility Function

```javascript
// Timer helper (drop into existing script)
// startTimer() -> returns stopTimer() which resolves to elapsed seconds
function startTimer() {
  let seconds = 0;
  const interval = setInterval(() => seconds++, 1000);
  const startedAt = Date.now();
  return {
    stop: () => {
      clearInterval(interval);
      // compute final seconds more precisely if desired
      const total = Math.round((Date.now() - startedAt) / 1000);
      return total;
    },
    getSeconds: () => seconds
  };
}

// Example usage:
// let timerHandle = startTimer(); // call at initGame or on first interaction
// const elapsed = timerHandle.stop(); // call when all correct, then submitFinalTime(player, elapsed)
```

---

### Integration with Game Completion Logic

Integrate with the existing completion logic (a small snippet you can drop into the final-check area):

```javascript
// After you confirm all images are placed and correct:
const elapsed = timerHandle.stop();
await submitFinalTime(currentPlayer, elapsed);
// show congrats, reset, etc.
```

*Advanced Scoring:* Adding a count-based score as well. Include it as an additional field when posting:
{ username, timeSeconds, countCorrect }.

---

## Planet-vs-Saucer Animation on Correct Placement

*Reward players instantly with an exciting animation when they make a correct placement, enhancing the game's satisfaction factor.*

**When to Trigger:** When the user sorts a news icon in the correct bin, we play the animation of the planet shooting at the invading alien saucer.

### Canvas Setup

Add this canvas element once in your page template:

```html
<!-- Add this once in the page template (example placement) -->
<canvas id="attackCanvas" style="position:fixed;pointer-events:none;top:0;left:0;width:100vw;height:100vh;z-index:999"></canvas>
```

---

### Animation Function

*Performance Note: Uses requestAnimationFrame for smooth, GPU-accelerated animation. Lightweight and won't impact game performance.*

Small performant animation using requestAnimationFrame (call playAttackAnimation() when a correct placement is detected):

```javascript
function playAttackAnimation() {
  const c = document.getElementById('attackCanvas');
  if (!c) return;
  // adapt canvas CSS size to device pixels
  c.width = c.clientWidth * devicePixelRatio;
  c.height = c.clientHeight * devicePixelRatio;
  const ctx = c.getContext('2d');
  const planet = { x: 60 * devicePixelRatio, y: c.height - 80 * devicePixelRatio };
  const saucer = { x: c.width - 140 * devicePixelRatio, y: 80 * devicePixelRatio };
  let laserX = planet.x;
  function frame() {
    ctx.clearRect(0, 0, c.width, c.height);
    // planet
    ctx.fillStyle = '#2b6cb0';
    ctx.beginPath();
    ctx.arc(planet.x, planet.y, 40 * devicePixelRatio, 0, Math.PI * 2);
    ctx.fill();
    // saucer
    ctx.fillStyle = '#888';
    ctx.fillRect(saucer.x, saucer.y, 80 * devicePixelRatio, 40 * devicePixelRatio);
    // laser
    ctx.fillStyle = 'red';
    ctx.fillRect(laserX, planet.y - 4 * devicePixelRatio, 8 * devicePixelRatio, 8 * devicePixelRatio);
    laserX += 22 * devicePixelRatio;
    if (laserX < saucer.x) requestAnimationFrame(frame);
    else {
      // hit explosion (simple)
      ctx.fillStyle = 'orange';
      ctx.beginPath();
      ctx.arc(saucer.x + 40 * devicePixelRatio, saucer.y + 20 * devicePixelRatio, 30 * devicePixelRatio, 0, Math.PI * 2);
      ctx.fill();
      setTimeout(() => ctx.clearRect(0, 0, c.width, c.height), 300);
    }
  }
  requestAnimationFrame(frame);
}
```

---

### Trigger Integration

Add to pre-existing success logic
```javascript
if (img.dataset.bin === bin.dataset.bin) {
  // ...existing success logic...
  playAttackAnimation();
}
```

---

## Improved Backend Source Delivery

*Manage your news sources database-side for easy updates without redeploying the frontend.*

**Optional Improvement:** Instead of hardcoding image lists on the client, deliver a randomized set from the backend so we can add/remove sources without touching the client.

### Backend Randomization

*Why Server-Side? Ensures all players get fair, unpredictable source distributions. Prevents client-side manipulation.*

Backend:
```javascript
app.get('/api/media/sources', async (req, res) => {
  const list = await db.sources.find().toArray();
  // shuffle server-side for fairness
  for (let i = list.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [list[i], list[j]] = [list[j], list[i]];
  }
  res.json(list);
});
```

---

### Frontend Integration

Frontend (use this to replace the static imageFiles block if you want):
```javascript
const newsSources = await fetch(`${javaURI}/api/media/sources`).then(r => r.json());
// newsSources should be an array of { src, company, bin } and can be used exactly like imageFiles
```

---

## AI Chatbox Expansion 

*Help players learn about unfamiliar news sources instantly through intelligent, context-aware AI assistance.*

### Core Purpose

When players encounter news sources they don't recognize, the AI chatbox provides quick, factual information to help them make informed categorization decisions without spoiling the answer.

---

### FEATURE ONE: Source Information Lookup

**What it does:** Players search for any news source name and receive neutral background information.

**Use case:** Player sees "The Epoch Times" logo but doesn't recognize it → types name into chatbox → receives factual description of ownership, founding, and general audience without revealing bias category.

**Player benefit:** Continue playing without leaving the game to Google unfamiliar sources.

---

### FEATURE TWO: Smart Hint System

**What it does:** Provides educational hints about a source's characteristics without revealing its bias placement.

**Use case:** Player asks "Give me a hint about Reuters" → AI responds with clues like "Consider their funding model and international reputation for fact-checking" rather than stating bias category.

**Player benefit:** Develop critical thinking skills instead of memorizing answers.

---

### FEATURE THREE: General Media Literacy Questions

**What it does:** Answer broader questions about media bias concepts and terminology.

**Use case:** Player asks "What does 'editorial slant' mean?" → AI explains the concept clearly and concisely, helping player understand the game's educational purpose.

**Player benefit:** Learn media literacy principles while playing, making the game more educational.

---

### FEATURE FOUR: Compare Sources (Advanced)

**What it does:** Help players understand subtle differences between similar sources.

**Use case:** Player asks "What's the difference between BBC and NPR?" → AI explains ownership structure, funding models, and target audiences without stating bias categories.

**Player benefit:** Understand nuanced differences that aren't obvious from logos alone.

---

### FEATURE FIVE: Post-Game Explanation Mode

**What it does:** After completing the game, players can ask why sources were categorized as they were.

**Use case:** Player finishes game and asks "Why is Fox News categorized as right-leaning?" → AI provides detailed, factual explanation with examples and research citations.

**Player benefit:** Deep learning after gameplay, reinforcing lessons and satisfying curiosity.

---

### Technical Implementation

Use the same javaURI pattern for chat helpers:

#### Frontend Implementation

```javascript
async function askAboutSource(name) {
  const res = await fetch(`${javaURI}/api/media/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ sourceName: name })
  });
  return res.json();
}
```

#### Backend Implementation

Backend (example using an LLM provider):
```javascript
app.post('/api/media/chat', async (req, res) => {
  const { sourceName, hintOnly } = req.body;
  // call your AI provider here (openai/gemini wrapper)
  // keep the prompt neutral and avoid giving the answer away if hintOnly === true
  const prompt = hintOnly
    ? `Give a short neutral description of the news outlet named "${sourceName}" without revealing political category.`
    : `Explain this news source factually: ${sourceName}`;
  const info = await aiClient.generate({ prompt });
  res.json({ text: info.text });
});
```

---

### User Interface Recommendations

**Placement:** Fixed chat icon in bottom-right corner that opens overlay modal when clicked.

**Visual Design:**
- Clean, minimal interface that doesn't distract from gameplay
- Message bubbles with subtle shadows for depth
- Typing indicator animation when AI is generating response
- Auto-scroll to newest messages

**Interaction Flow:**
1. Player clicks chat icon
2. Modal opens with search/question input field
3. Player types source name or question
4. AI responds within 2-3 seconds
5. Conversation history preserved during session
6. Player closes modal and continues playing

**Mobile Optimization:**
- Full-screen chat modal on mobile devices
- Large touch targets for buttons
- Keyboard auto-focuses when modal opens
- Swipe-down gesture to close

---

### Content Safety & Guidelines

**Input Filtering:** Block inappropriate language and prevent attempts to manipulate AI into revealing answers during active gameplay.

**Output Validation:** Ensure AI responses remain neutral and educational, never revealing bias categories when hintOnly mode is active.

**Privacy:** Don't store personally identifiable information. Anonymize conversation logs if used for improving prompts.

---

## Summary: Transformation Impact

By implementing these features, the Media Bias Game evolves from a simple sorting exercise into a comprehensive, engaging, educational platform that combines:

**Competition** — Leaderboards and timed challenges create replay value  
**Feedback** — Visual animations reward correct placements  
**Education** — AI-powered learning assistant builds genuine media literacy  
**Scalability** — Backend-driven content allows easy updates  
**Retention** — Multiple features provide reasons to return  

The AI Chatbox transforms passive gameplay into active learning, helping players develop critical thinking skills that extend far beyond the game itself.

---

*Last Updated: November 2024 | Author: Interacters Team*