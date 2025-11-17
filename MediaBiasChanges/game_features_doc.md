---
layout: post
title: Game Features Improvement Plan
permalink: /mediabias_plan
author: Interacters
---

## Game Features Improvement plan

## Backend-Driven Leaderboard 

### Frontend Submission (time-based, using javaURI)
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

### Backend Storage (Express + Mongo example)
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

### Frontend Leaderboard Display (fetch sorted by fastest time)
```javascript
// GET top 10 fastest times (lower time is better)
const res = await fetch(`${javaURI}/api/media/leaderboard`);
const scores = await res.json(); // expect sorted by time ascending
render(scores);
```

### Backend Leaderboard Route (sorted by time ascending)
```javascript
app.get('/api/media/leaderboard', async (req, res) => {
  const top = await db.leaderboard.find().sort({ time: 1 }).limit(10).toArray();
  res.json(top);
});
```

---

## Timed Win Condition (integrate into mediabias_sub2 easily)

Goal: Start a timer when the round begins (or on first drag), stop when every source is placed correctly, send seconds to backend.

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

Integrate with the existing completion logic (a small snippet you can drop into the final-check area):

```javascript
// After you confirm all images are placed and correct:
const elapsed = timerHandle.stop();
await submitFinalTime(currentPlayer, elapsed);
// show congrats, reset, etc.
```

Adding a count-based score as well. Include it as an additional field when posting:
{ username, timeSeconds, countCorrect }.

---

## Planet-vs-Saucer Animation on Correct Placement
When the user sorts a news icon in the correct bin, we play the animation of the planet shooting at the invading alien saucer.

```html
<!-- Add this once in the page template (example placement) -->
<canvas id="attackCanvas" style="position:fixed;pointer-events:none;top:0;left:0;width:100vw;height:100vh;z-index:999"></canvas>
```

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
Add to pre-existing success logic
```javascript
if (img.dataset.bin === bin.dataset.bin) {
  // ...existing success logic...
  playAttackAnimation();
}
```

---

## Improved Backend Source Delivery (recommended)

Instead of hardcoding image lists on the client, deliver a randomized set from the backend so we can add/remove sources without touching the client.

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

Frontend (use this to replace the static imageFiles block if you want):
```javascript
const newsSources = await fetch(`${javaURI}/api/media/sources`).then(r => r.json());
// newsSources should be an array of { src, company, bin } and can be used exactly like imageFiles
```

---

## AI Chatbox Expansion 

Use the same javaURI pattern for chat helpers:

Frontend:
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


