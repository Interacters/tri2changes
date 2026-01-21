# Activity Votes Backend Implementation

## Overview
This document describes the backend API endpoints required to support the activity-based feedback system with animated progress bars.

## Database Schema

### activity_votes Table
```sql
CREATE TABLE activity_votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    username TEXT,
    activity TEXT NOT NULL,
    vote TEXT NOT NULL,  -- 'yes' or 'no'
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```

## API Endpoints

### 1. Submit Activity Votes
**Endpoint:** `POST /api/activity-votes/submit`

**Authentication:** Required

**Request Body:**
```json
{
    "media-bias": "yes",
    "thesis": "no",
    "citations": "yes"
}
```

**Response (200 OK):**
```json
{
    "media-bias": {
        "yes": 45,
        "no": 15,
        "total": 60
    },
    "thesis": {
        "yes": 52,
        "no": 8,
        "total": 60
    },
    "citations": {
        "yes": 38,
        "no": 22,
        "total": 60
    }
}
```

**Description:**
- Accepts user's Yes/No votes for each of the three activities
- Saves votes to database with timestamp and user information
- Returns aggregated vote counts for all activities
- Only allows one vote per activity per user (updates if user votes again)

### 2. Get Current Activity Votes
**Endpoint:** `GET /api/activity-votes`

**Authentication:** Optional

**Response (200 OK):**
```json
{
    "media-bias": {
        "yes": 45,
        "no": 15,
        "total": 60
    },
    "thesis": {
        "yes": 52,
        "no": 8,
        "total": 60
    },
    "citations": {
        "yes": 38,
        "no": 22,
        "total": 60
    }
}
```

**Description:**
- Returns current vote counts and percentages for all activities
- Used to populate progress bars on page load
- No authentication required for viewing aggregate data

### 3. Get All Activity Votes (Admin)
**Endpoint:** `GET /api/activity-votes/all`

**Authentication:** Required (Admin only)

**Response (200 OK):**
```json
{
    "media-bias": {
        "yes": 45,
        "no": 15,
        "total": 60,
        "yes_percent": 75,
        "no_percent": 25
    },
    "thesis": {
        "yes": 52,
        "no": 8,
        "total": 60,
        "yes_percent": 87,
        "no_percent": 13
    },
    "citations": {
        "yes": 38,
        "no": 22,
        "total": 60,
        "yes_percent": 63,
        "no_percent": 37
    }
}
```

**Description:**
- Admin endpoint showing detailed vote breakdown
- Used for admin dashboard statistics

### 4. Get User's Activity Votes
**Endpoint:** `GET /api/activity-votes/user/<user_id>`

**Authentication:** Required (Admin or self)

**Response (200 OK):**
```json
{
    "user_id": 123,
    "username": "john_doe",
    "votes": [
        {
            "activity": "media-bias",
            "vote": "yes",
            "timestamp": "2025-01-20T14:30:00"
        },
        {
            "activity": "thesis",
            "vote": "no",
            "timestamp": "2025-01-20T14:31:00"
        },
        {
            "activity": "citations",
            "vote": "yes",
            "timestamp": "2025-01-20T14:32:00"
        }
    ]
}
```

**Description:**
- Returns all votes submitted by a specific user
- Shows activity, vote choice, and timestamp for each vote

## Flask Implementation Example

```python
from flask import request, jsonify
from datetime import datetime
import sqlite3

@app.route('/api/activity-votes/submit', methods=['POST'])
def submit_activity_votes():
    """Submit votes for all activities"""
    if not is_user_authenticated():
        return jsonify({'error': 'Not authenticated'}), 401
    
    user = get_current_user()
    data = request.get_json()
    
    # Validate votes
    activities = ['media-bias', 'thesis', 'citations']
    for activity in activities:
        if activity not in data or data[activity] not in ['yes', 'no']:
            return jsonify({'error': f'Invalid vote for {activity}'}), 400
    
    # Save votes to database
    for activity, vote in data.items():
        save_activity_vote(user['id'], user['username'], activity, vote)
    
    # Return aggregated data
    return get_all_activity_votes_with_aggregation()


@app.route('/api/activity-votes', methods=['GET'])
def get_activity_votes():
    """Get current vote counts for all activities"""
    return get_all_activity_votes_with_aggregation()


@app.route('/api/activity-votes/all', methods=['GET'])
def get_all_activity_votes():
    """Get detailed vote breakdown (admin only)"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    return get_all_activity_votes_with_aggregation(include_percentages=True)


@app.route('/api/activity-votes/user/<int:user_id>', methods=['GET'])
def get_user_activity_votes(user_id):
    """Get all votes submitted by a user"""
    current_user = get_current_user()
    
    # Allow users to view only their own votes, admins can view any
    if not is_admin() and current_user['id'] != user_id:
        return jsonify({'error': 'Forbidden'}), 403
    
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    votes = get_user_votes_from_db(user_id)
    
    return jsonify({
        'user_id': user_id,
        'username': user['username'],
        'votes': votes
    })


def save_activity_vote(user_id, username, activity, vote):
    """Save or update activity vote in database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if user already voted for this activity
    cursor.execute(
        'SELECT id FROM activity_votes WHERE user_id = ? AND activity = ?',
        (user_id, activity)
    )
    existing = cursor.fetchone()
    
    if existing:
        # Update existing vote
        cursor.execute(
            'UPDATE activity_votes SET vote = ?, timestamp = ? WHERE id = ?',
            (vote, datetime.now(), existing[0])
        )
    else:
        # Insert new vote
        cursor.execute(
            'INSERT INTO activity_votes (user_id, username, activity, vote, timestamp) VALUES (?, ?, ?, ?, ?)',
            (user_id, username, activity, vote, datetime.now())
        )
    
    conn.commit()
    conn.close()


def get_all_activity_votes_with_aggregation(include_percentages=False):
    """Calculate aggregate vote counts for all activities"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    result = {}
    activities = ['media-bias', 'thesis', 'citations']
    
    for activity in activities:
        cursor.execute(
            'SELECT vote, COUNT(*) FROM activity_votes WHERE activity = ? GROUP BY vote',
            (activity,)
        )
        votes = dict(cursor.fetchall())
        
        yes_count = votes.get('yes', 0)
        no_count = votes.get('no', 0)
        total = yes_count + no_count
        
        result[activity] = {
            'yes': yes_count,
            'no': no_count,
            'total': total
        }
        
        if include_percentages:
            result[activity]['yes_percent'] = int((yes_count / total * 100)) if total > 0 else 0
            result[activity]['no_percent'] = int((no_count / total * 100)) if total > 0 else 0
    
    conn.close()
    return jsonify(result)


def get_user_votes_from_db(user_id):
    """Retrieve all votes from a specific user"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT activity, vote, timestamp FROM activity_votes WHERE user_id = ? ORDER BY timestamp DESC',
        (user_id,)
    )
    
    votes = []
    for row in cursor.fetchall():
        votes.append({
            'activity': row[0],
            'vote': row[1],
            'timestamp': row[2]
        })
    
    conn.close()
    return votes
```

## Frontend Integration

The frontend will:
1. Load current vote aggregates on page load with `GET /api/activity-votes`
2. Display progress bars with animated width transitions
3. On form submission, send votes to `POST /api/activity-votes/submit`
4. Display individual results with animated progress bars in the results modal
5. Admins see the admin view with detailed statistics from `GET /api/activity-votes/all`

## Notes

- All timestamps should be stored in UTC
- Votes are permanently saved (forever, as requested)
- Users can update their votes by submitting again
- Vote data is persistent across sessions
- Progress bars animate with cubic-bezier timing for smooth visual effect
- Percentages are calculated as integer values (no decimals)
