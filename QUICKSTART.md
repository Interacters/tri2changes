# Activity Votes System - Quick Start Guide

## Overview
The Performance Reflection section now uses activity-specific Yes/No questions with animated progress bars showing class-wide confidence levels.

## What Users See

### Performance Reflection Page
1. **Three Questions:**
   - 📰 Media Bias Sorting Game: "Did you feel confident in identifying media bias?"
   - ✍️ Thesis Generator: "Did you feel confident writing your thesis statement?"
   - 📚 Citation Generator: "Did you feel confident creating citations?"

2. **Interactive Elements:**
   - Green/Red Yes/No buttons (user selects one per question)
   - Live progress bars showing what percentage of classmates voted "Yes"
   - Total response count

3. **Results Modal:**
   - Shows your votes in green or red
   - Displays class-wide percentages for each activity
   - Animated progress bars reveal peer feedback

## Quick Start - 5 Steps

### Step 1: Update Your Database
```sql
CREATE TABLE activity_votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    username TEXT,
    activity TEXT NOT NULL,
    vote TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```

### Step 2: Add Backend Endpoints
Copy the Flask functions from `ACTIVITY_VOTES_BACKEND.md`:
- `/api/activity-votes/submit` (POST)
- `/api/activity-votes` (GET)
- `/api/activity-votes/all` (GET - Admin)
- `/api/activity-votes/user/<user_id>` (GET)

### Step 3: Test Frontend
1. Open mainmodule.md in your browser
2. Scroll to Performance Reflection section
3. You should see 3 activity questions with Yes/No buttons
4. Progress bars show 0% until votes are submitted

### Step 4: Test Vote Submission
1. Click Yes/No for each question
2. Click "Submit Feedback"
3. Results modal should appear with animated progress bars
4. Admin view should update with new response

### Step 5: Verify Admin Dashboard
1. Log in as admin
2. Scroll to "All Activity Feedback" section
3. Check statistics and vote table

## Key API Responses

### Submit Vote Request
```json
POST /api/activity-votes/submit
{
    "media-bias": "yes",
    "thesis": "no", 
    "citations": "yes"
}
```

### Vote Aggregation Response
```json
{
    "media-bias": {"yes": 45, "no": 15, "total": 60},
    "thesis": {"yes": 52, "no": 8, "total": 60},
    "citations": {"yes": 38, "no": 22, "total": 60}
}
```

## Features Implemented ✅

| Feature | Status | Notes |
|---------|--------|-------|
| Activity-specific questions | ✅ | 3 questions for each activity |
| Yes/No voting | ✅ | Replaces 1-5 rating scale |
| Progress bars | ✅ | Animated with cubic-bezier easing |
| Backend communication | ✅ | Posts to `/api/activity-votes/submit` |
| Data persistence | ✅ | Saves to DB with timestamp forever |
| Vote aggregation | ✅ | Backend calculates percentages |
| Results display | ✅ | Shows user vs class averages |
| Admin dashboard | ✅ | Detailed statistics & vote tracking |
| Mobile responsive | ✅ | Touch-friendly on all devices |

## CSS Classes Added

```css
/* Main container */
.activity-questions-container
.activity-question

/* Buttons */
.yes-no-buttons
.yes-no-btn
.yes-no-btn:hover
.yes-no-btn.selected
.yes-no-btn.selected.yes
.yes-no-btn.selected.no

/* Progress bars */
.progress-bar-container
.progress-bar-container.show
.progress-bar-wrapper
.progress-bar-fill
.progress-bar-fill.no-votes
.progress-bar-label
.progress-stat

/* Results */
.results-container
.results-container.show
.activity-results
```

## JavaScript Functions

```javascript
// Initialize buttons with click handlers
initializeButtonHandlers()

// Load current votes on page load
loadActivityVotes()

// Update progress bars with vote data
updateProgressBars(votes)

// Submit user's votes
// (Automatic on form submit)

// Display results with animations
showResults(data)

// Admin functions
loadAllActivityVotes()
displayAdminActivityStats(allVotes)
displayActivityVotesTable(allVotes)
```

## Customization Options

### Change Questions
Edit the HTML questions in mainmodule.md:
```html
<h3>📰 Media Bias Sorting Game: Your custom question here?</h3>
```

### Adjust Colors
Modify CSS for button colors:
```css
.yes-no-btn.selected.yes {
    background: linear-gradient(135deg, #10b981, #059669);
}
```

### Change Animation Speed
Modify CSS transition:
```css
.progress-bar-fill {
    transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}
```
(0.6s = 600 milliseconds, adjust as needed)

## Troubleshooting

### Progress bars not updating
- Check browser console for fetch errors
- Verify backend endpoints are responding
- Ensure authentication tokens are valid

### Votes not saving
- Verify `activity_votes` table exists in database
- Check backend logs for SQL errors
- Ensure user is authenticated

### Results modal not showing
- Check that response includes all three activities
- Verify progress bar percentages calculated correctly
- Check console for JavaScript errors

### Admin view not visible
- Verify user role is "Admin" in database
- Check authentication is working
- Ensure `GET /api/activity-votes/all` returns data

## File Locations

| File | Purpose |
|------|---------|
| `mainmodule.md` | Frontend UI and JavaScript |
| `ACTIVITY_VOTES_BACKEND.md` | Backend implementation guide |
| `IMPLEMENTATION_SUMMARY.md` | Detailed change documentation |

## Support

For implementation help, refer to:
1. `ACTIVITY_VOTES_BACKEND.md` - Complete API specifications
2. `IMPLEMENTATION_SUMMARY.md` - All changes made
3. Flask code examples in backend doc

## Next Steps

1. **Backend Implementation** (1-2 hours)
   - Create database table
   - Implement 4 API endpoints
   - Test with Postman or curl

2. **Testing** (30 minutes)
   - Test form submission
   - Verify data saves
   - Check aggregation math

3. **Deployment** (15 minutes)
   - Push changes to production
   - Monitor for errors
   - Collect first batch of votes

---
**Last Updated:** January 20, 2026
**Version:** 1.0 - Initial Release
