---
permalink: /sloanetestmodule/
author: Interactors
date: 2025-12-12
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Performance Reflection Survey</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }

        .survey-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 50px 40px;
            border-radius: 30px;
            max-width: 900px;
            width: 100%;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.4);
            margin: 0 auto 40px;
        }

        .survey-header {
            text-align: center;
            margin-bottom: 40px;
        }

        .survey-header h2 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
            font-weight: 800;
        }

        .survey-header p {
            color: #4a5568;
            font-size: 1.1rem;
            line-height: 1.7;
        }

        .question-block {
            margin-bottom: 50px;
            opacity: 0;
            animation: fadeInUp 0.6s ease-out forwards;
        }

        .question-block:nth-child(1) { animation-delay: 0.1s; }
        .question-block:nth-child(2) { animation-delay: 0.2s; }
        .question-block:nth-child(3) { animation-delay: 0.3s; }
        .question-block:nth-child(4) { animation-delay: 0.4s; }
        .question-block:nth-child(5) { animation-delay: 0.5s; }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .question-text {
            font-size: 1.2rem;
            font-weight: 600;
            color: #2d3748;
            margin-bottom: 20px;
        }

        .rating-buttons {
            display: flex;
            gap: 12px;
            margin-bottom: 25px;
            justify-content: center;
        }

        .rating-btn {
            width: 70px;
            height: 70px;
            border: 3px solid #e2e8f0;
            border-radius: 15px;
            background: white;
            font-size: 1.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
            overflow: hidden;
            color: #667eea;
        }

        .rating-btn::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 0;
        }

        .rating-btn span {
            position: relative;
            z-index: 1;
        }

        .rating-btn:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
            border-color: #667eea;
        }

        .rating-btn.selected {
            border-color: #667eea;
            color: white;
            transform: scale(1.1);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        }

        .rating-btn.selected::before {
            opacity: 1;
        }

        .rating-labels {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            padding: 0 10px;
        }

        .rating-label {
            font-size: 0.85rem;
            color: #718096;
            font-weight: 600;
        }

        .average-display {
            display: none;
            margin-top: 25px;
            padding: 25px;
            background: #f7fafc;
            border-radius: 15px;
            border-left: 5px solid #667eea;
        }

        .average-display.show {
            display: block;
            animation: slideDown 0.5s ease-out;
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                max-height: 0;
            }
            to {
                opacity: 1;
                max-height: 300px;
            }
        }

        .average-label {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .average-label-text {
            font-weight: 700;
            color: #2d3748;
            font-size: 1rem;
        }

        .average-value {
            font-size: 1.8rem;
            font-weight: 800;
            color: #667eea;
        }

        .progress-bar-container {
            height: 50px;
            background: #e2e8f0;
            border-radius: 25px;
            overflow: hidden;
            position: relative;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .progress-bar {
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 1.1rem;
            transition: width 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
        }

        .stats-row {
            display: flex;
            justify-content: space-around;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 2px solid #e2e8f0;
        }

        .stat-item {
            text-align: center;
        }

        .stat-label {
            font-size: 0.75rem;
            color: #718096;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 5px;
        }

        .stat-value {
            font-size: 1.3rem;
            font-weight: 700;
            color: #667eea;
        }

        .submit-btn {
            width: 100%;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 15px;
            font-size: 1.3rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            margin-top: 30px;
        }

        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
        }

        .submit-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            border-top-color: white;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Admin View */
        .admin-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 40px;
            border-radius: 30px;
            max-width: 1400px;
            width: 100%;
            margin: 40px auto;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.4);
        }

        .admin-header {
            margin-bottom: 30px;
            text-align: center;
        }

        .admin-header h2 {
            font-size: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        .responses-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }

        .responses-table th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
            font-size: 0.9rem;
        }

        .responses-table td {
            padding: 15px;
            border-bottom: 1px solid #e2e8f0;
            color: #4a5568;
        }

        .responses-table tr:hover {
            background: #f7fafc;
        }

        .rating-badge {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 1rem;
        }

        .rating-1 { background: #fee; color: #c53030; }
        .rating-2 { background: #fef5e7; color: #d97706; }
        .rating-3 { background: #fef3c7; color: #b45309; }
        .rating-4 { background: #e0f2fe; color: #0369a1; }
        .rating-5 { background: #d1fae5; color: #047857; }

        @media (max-width: 768px) {
            .survey-container {
                padding: 30px 20px;
            }

            .survey-header h2 {
                font-size: 2rem;
            }

            .rating-buttons {
                gap: 8px;
            }

            .rating-btn {
                width: 55px;
                height: 55px;
                font-size: 1.4rem;
            }

            .question-text {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="survey-container">
        <div class="survey-header">
            <h2>Performance Reflection</h2>
            <p>Rate your understanding and performance across five key English skill-building tasks. See how your ratings compare with the class average.</p>
        </div>

        <form id="survey-form">
            <div class="question-block" data-question="1">
                <div class="question-text">1. How well did you perform on understanding media bias?</div>
                <div class="rating-labels">
                    <span class="rating-label">Poor</span>
                    <span class="rating-label">Superior</span>
                </div>
                <div class="rating-buttons">
                    <button type="button" class="rating-btn" data-rating="1">
                        <span>1</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="2">
                        <span>2</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="3">
                        <span>3</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="4">
                        <span>4</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="5">
                        <span>5</span>
                    </button>
                </div>
                <div class="average-display">
                    <div class="average-label">
                        <span class="average-label-text">Class Average</span>
                        <span class="average-value">-</span>
                    </div>
                    <div class="progress-bar-container">
                        <div class="progress-bar" style="width: 0%">
                            <span class="bar-text"></span>
                        </div>
                    </div>
                    <div class="stats-row">
                        <div class="stat-item">
                            <div class="stat-label">Total Responses</div>
                            <div class="stat-value total-count">0</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Your Rating</div>
                            <div class="stat-value your-rating">-</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="question-block" data-question="2">
                <div class="question-text">2. How well did you perform on thesis writing?</div>
                <div class="rating-labels">
                    <span class="rating-label">Poor</span>
                    <span class="rating-label">Superior</span>
                </div>
                <div class="rating-buttons">
                    <button type="button" class="rating-btn" data-rating="1">
                        <span>1</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="2">
                        <span>2</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="3">
                        <span>3</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="4">
                        <span>4</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="5">
                        <span>5</span>
                    </button>
                </div>
                <div class="average-display">
                    <div class="average-label">
                        <span class="average-label-text">Class Average</span>
                        <span class="average-value">-</span>
                    </div>
                    <div class="progress-bar-container">
                        <div class="progress-bar" style="width: 0%">
                            <span class="bar-text"></span>
                        </div>
                    </div>
                    <div class="stats-row">
                        <div class="stat-item">
                            <div class="stat-label">Total Responses</div>
                            <div class="stat-value total-count">0</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Your Rating</div>
                            <div class="stat-value your-rating">-</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="question-block" data-question="3">
                <div class="question-text">3. How well did you perform on understanding citations?</div>
                <div class="rating-labels">
                    <span class="rating-label">Poor</span>
                    <span class="rating-label">Superior</span>
                </div>
                <div class="rating-buttons">
                    <button type="button" class="rating-btn" data-rating="1">
                        <span>1</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="2">
                        <span>2</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="3">
                        <span>3</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="4">
                        <span>4</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="5">
                        <span>5</span>
                    </button>
                </div>
                <div class="average-display">
                    <div class="average-label">
                        <span class="average-label-text">Class Average</span>
                        <span class="average-value">-</span>
                    </div>
                    <div class="progress-bar-container">
                        <div class="progress-bar" style="width: 0%">
                            <span class="bar-text"></span>
                        </div>
                    </div>
                    <div class="stats-row">
                        <div class="stat-item">
                            <div class="stat-label">Total Responses</div>
                            <div class="stat-value total-count">0</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Your Rating</div>
                            <div class="stat-value your-rating">-</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="question-block" data-question="4">
                <div class="question-text">4. How well did you perform on analyzing argumentative techniques?</div>
                <div class="rating-labels">
                    <span class="rating-label">Poor</span>
                    <span class="rating-label">Superior</span>
                </div>
                <div class="rating-buttons">
                    <button type="button" class="rating-btn" data-rating="1">
                        <span>1</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="2">
                        <span>2</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="3">
                        <span>3</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="4">
                        <span>4</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="5">
                        <span>5</span>
                    </button>
                </div>
                <div class="average-display">
                    <div class="average-label">
                        <span class="average-label-text">Class Average</span>
                        <span class="average-value">-</span>
                    </div>
                    <div class="progress-bar-container">
                        <div class="progress-bar" style="width: 0%">
                            <span class="bar-text"></span>
                        </div>
                    </div>
                    <div class="stats-row">
                        <div class="stat-item">
                            <div class="stat-label">Total Responses</div>
                            <div class="stat-value total-count">0</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Your Rating</div>
                            <div class="stat-value your-rating">-</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="question-block" data-question="5">
                <div class="question-text">5. How well did you perform on research and source evaluation?</div>
                <div class="rating-labels">
                    <span class="rating-label">Poor</span>
                    <span class="rating-label">Superior</span>
                </div>
                <div class="rating-buttons">
                    <button type="button" class="rating-btn" data-rating="1">
                        <span>1</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="2">
                        <span>2</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="3">
                        <span>3</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="4">
                        <span>4</span>
                    </button>
                    <button type="button" class="rating-btn" data-rating="5">
                        <span>5</span>
                    </button>
                </div>
                <div class="average-display">
                    <div class="average-label">
                        <span class="average-label-text">Class Average</span>
                        <span class="average-value">-</span>
                    </div>
                    <div class="progress-bar-container">
                        <div class="progress-bar" style="width: 0%">
                            <span class="bar-text"></span>
                        </div>
                    </div>
                    <div class="stats-row">
                        <div class="stat-item">
                            <div class="stat-label">Total Responses</div>
                            <div class="stat-value total-count">0</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Your Rating</div>
                            <div class="stat-value your-rating">-</div>
                        </div>
                    </div>
                </div>
            </div>

            <button type="submit" class="submit-btn" id="submit-btn">
                <span>Submit My Ratings</span>
            </button>
        </form>
    </div>

    <div class="admin-container" id="admin-section" style="display: none;">
        <div class="admin-header">
            <h2>📊 All Student Responses</h2>
        </div>

        <table class="responses-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Username</th>
                    <th>Q1</th>
                    <th>Q2</th>
                    <th>Q3</th>
                    <th>Q4</th>
                    <th>Q5</th>
                    <th>Average</th>
                    <th>Timestamp</th>
                </tr>
            </thead>
            <tbody id="responses-tbody"></tbody>
        </table>
    </div>

    <script type="module">
        import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';
        const API_BASE = `${pythonURI}/api`;

        const ratings = {};

        // Handle rating button clicks
        document.querySelectorAll('.rating-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const questionBlock = this.closest('.question-block');
                const questionNum = questionBlock.dataset.question;
                const rating = parseInt(this.dataset.rating);
                
                // Remove selected from siblings
                questionBlock.querySelectorAll('.rating-btn').forEach(b => {
                    b.classList.remove('selected');
                });
                
                // Add selected to this button
                this.classList.add('selected');
                
                // Store rating
                ratings[`q${questionNum}`] = rating;
                
                // Update "Your Rating" in the stats
                const yourRatingElem = questionBlock.querySelector('.your-rating');
                if (yourRatingElem) {
                    yourRatingElem.textContent = rating;
                }
            });
        });

        // Check authentication
        async function checkAuth() {
            try {
                const response = await fetch(`${API_BASE}/id`, {
                    ...fetchOptions
                });
                
                if (response.ok) {
                    const userData = await response.json();
                    return userData;
                }
            } catch (error) {
                console.error('Auth check failed:', error);
            }
            return null;
        }

        // Load statistics for all questions
        async function loadStats() {
            try {
                const response = await fetch(`${API_BASE}/multirating/stats`, {
                    credentials: 'include'
                });
                
                if (response.ok) {
                    const stats = await response.json();
                    displayStats(stats);
                }
            } catch (error) {
                console.error('Failed to load stats:', error);
            }
        }

        // Display statistics
        function displayStats(stats) {
            for (let i = 1; i <= 5; i++) {
                const questionBlock = document.querySelector(`[data-question="${i}"]`);
                const averageDisplay = questionBlock.querySelector('.average-display');
                
                const questionStats = stats[`q${i}`];
                const average = questionStats.average;
                const total = questionStats.total;
                
                // Calculate percentage for progress bar (out of 5)
                const percentage = (average / 5) * 100;
                
                // Update average value
                averageDisplay.querySelector('.average-value').textContent = average.toFixed(1);
                
                // Update total count
                averageDisplay.querySelector('.total-count').textContent = total;
                
                // Update progress bar
                const progressBar = averageDisplay.querySelector('.progress-bar');
                progressBar.style.width = `${percentage}%`;
                progressBar.querySelector('.bar-text').textContent = average > 0 ? average.toFixed(1) : '';
                
                // Show the display
                averageDisplay.classList.add('show');
            }
        }

        // Load all responses (admin only)
        async function loadAllResponses() {
            try {
                const response = await fetch(`${API_BASE}/multirating/responses`, {
                    credentials: 'include'
                });
                
                if (response.ok) {
                    const responses = await response.json();
                    displayAllResponses(responses);
                }
            } catch (error) {
                console.error('Failed to load responses:', error);
            }
        }

        // Display all responses in table
        function displayAllResponses(responses) {
            const tbody = document.getElementById('responses-tbody');
            tbody.innerHTML = '';

            responses.reverse().forEach(resp => {
                const avg = ((resp.q1 + resp.q2 + resp.q3 + resp.q4 + resp.q5) / 5).toFixed(1);
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${resp.id}</td>
                    <td>${resp.username || 'Guest'}</td>
                    <td><span class="rating-badge rating-${resp.q1}">${resp.q1}</span></td>
                    <td><span class="rating-badge rating-${resp.q2}">${resp.q2}</span></td>
                    <td><span class="rating-badge rating-${resp.q3}">${resp.q3}</span></td>
                    <td><span class="rating-badge rating-${resp.q4}">${resp.q4}</span></td>
                    <td><span class="rating-badge rating-${resp.q5}">${resp.q5}</span></td>
                    <td><strong>${avg}</strong></td>
                    <td>${new Date(resp.timestamp).toLocaleString()}</td>
                `;
            });
        }

        // Handle form submission
        document.getElementById('survey-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Check all questions are answered
            if (Object.keys(ratings).length < 5) {
                alert('Please rate all 5 questions before submitting.');
                return;
            }

            const submitBtn = document.getElementById('submit-btn');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<div class="loading"></div>';

            try {
                const response = await fetch(`${API_BASE}/multirating/submit`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    body: JSON.stringify(ratings)
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    // Load and display stats
                    await loadStats();
                    
                    // Scroll to first question to see results
                    document.querySelector('.question-block').scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'center' 
                    });
                    
                    // Reload admin view if visible
                    if (document.getElementById('admin-section').style.display !== 'none') {
                        loadAllResponses();
                    }
                    
                    alert('✅ Your ratings have been submitted! Scroll up to see the class averages.');
                } else {
                    alert('Error: ' + (data.error || 'Unknown error occurred'));
                }
            } catch (error) {
                alert('Failed to submit. Please ensure you are logged in and your Flask server is running.');
                console.error(error);
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<span>Submit My Ratings</span>';
            }
        });

        // Initialize page
        window.addEventListener('DOMContentLoaded', async () => {
            const user = await checkAuth();
            
            if (user) {
                console.log('User logged in:', user.uid, 'Role:', user.role);
                
                // Load stats on page load
                loadStats();
                
                // Show admin section if user is admin
                if (user.role === 'Admin') {
                    document.getElementById('admin-section').style.display = 'block';
                    loadAllResponses();
                }
            } else {
                console.log('No user logged in - stats will still be visible');
                loadStats();
            }
        });
    </script>
</body>
</html>