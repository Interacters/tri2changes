---
permalink: /english_help/
author: Interactors
date: 2025-12-12
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English Essay Help - Media Literacy Module</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            background: linear-gradient(135deg, #1e3a8a 0%, #312e81 50%, #1e293b 100%);
            font-family: 'Inter', system-ui, sans-serif;
            color: #e2e8f0;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        /* Progress Tracker */
        .progress-tracker {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 30px;
            border: 1px solid rgba(148, 163, 184, 0.1);
        }

        .progress-header {
            text-align: center;
            margin-bottom: 30px;
        }

        .progress-header h1 {
            font-size: 2rem;
            background: linear-gradient(90deg, #60a5fa, #a78bfa, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }

        .progress-subtitle {
            color: #94a3b8;
            font-size: 1rem;
        }

        .progress-steps {
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            margin-bottom: 20px;
        }

        .progress-line {
            position: absolute;
            top: 20px;
            left: 0;
            right: 0;
            height: 4px;
            background: rgba(148, 163, 184, 0.2);
            z-index: 0;
        }

        .progress-line-fill {
            height: 100%;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            transition: width 0.5s ease;
            border-radius: 2px;
        }

        .step {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            z-index: 1;
            flex: 1;
        }

        .step-circle {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: rgba(15, 23, 42, 0.9);
            border: 3px solid rgba(148, 163, 184, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1rem;
            transition: all 0.3s ease;
            margin-bottom: 12px;
        }

        .step.active .step-circle {
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            border-color: #60a5fa;
            box-shadow: 0 0 20px rgba(96, 165, 250, 0.5);
            transform: scale(1.1);
        }

        .step.completed .step-circle {
            background: linear-gradient(135deg, #10b981, #059669);
            border-color: #10b981;
        }

        .step.completed .step-circle::before {
            content: '✓';
            font-size: 1.2rem;
        }

        .step-label {
            font-size: 0.85rem;
            color: #94a3b8;
            text-align: center;
            font-weight: 500;
            max-width: 120px;
        }

        .step.active .step-label {
            color: #60a5fa;
            font-weight: 600;
        }

        .step.completed .step-label {
            color: #10b981;
        }

        /* Section Container */
        .section-container {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 40px;
            margin-bottom: 30px;
            border: 1px solid rgba(148, 163, 184, 0.1);
            display: none;
        }

        .section-container.active {
            display: block;
            animation: fadeIn 0.5s ease;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .section-header {
            margin-bottom: 30px;
        }

        .section-title {
            font-size: 2rem;
            margin-bottom: 12px;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .section-description {
            color: #cbd5e1;
            font-size: 1.05rem;
            line-height: 1.6;
        }

        /* Navigation Buttons */
        .navigation-buttons {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin-top: 40px;
        }

        .nav-btn {
            padding: 14px 32px;
            border: none;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .nav-btn-prev {
            background: rgba(148, 163, 184, 0.2);
            color: #e2e8f0;
        }

        .nav-btn-prev:hover:not(:disabled) {
            background: rgba(148, 163, 184, 0.3);
            transform: translateX(-4px);
        }

        .nav-btn-next {
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            color: white;
            margin-left: auto;
        }

        .nav-btn-next:hover:not(:disabled) {
            transform: translateX(4px);
            box-shadow: 0 8px 20px rgba(96, 165, 250, 0.4);
        }

        .nav-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        /* Placeholder for game content */
        .content-placeholder {
            background: rgba(30, 41, 59, 0.5);
            border: 2px dashed rgba(148, 163, 184, 0.3);
            border-radius: 12px;
            padding: 60px 40px;
            text-align: center;
            color: #94a3b8;
        }

        .content-placeholder h3 {
            font-size: 1.5rem;
            margin-bottom: 10px;
            color: #cbd5e1;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .progress-steps {
                flex-wrap: wrap;
                gap: 20px;
            }

            .step {
                min-width: 80px;
            }

            .progress-line {
                display: none;
            }

            .navigation-buttons {
                flex-direction: column;
            }

            .nav-btn-next {
                margin-left: 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Progress Tracker -->
        <div class="progress-tracker">
            <div class="progress-header">
                <h1>English Essay Skills Module</h1>
                <p class="progress-subtitle">Master media bias, thesis writing, citations, and more!</p>
            </div>

            <div class="progress-steps">
                <div class="progress-line">
                    <div class="progress-line-fill" id="progress-fill"></div>
                </div>
                
                <div class="step active" data-step="1">
                    <div class="step-circle">1</div>
                    <div class="step-label">Media Bias Game</div>
                </div>
                
                <div class="step" data-step="2">
                    <div class="step-circle">2</div>
                    <div class="step-label">Citation Generator</div>
                </div>
                
                <div class="step" data-step="3">
                    <div class="step-circle">3</div>
                    <div class="step-label">Thesis Generator</div>
                </div>
                
                <div class="step" data-step="4">
                    <div class="step-circle">4</div>
                    <div class="step-label">Performance Review</div>
                </div>
            </div>
        </div>

        <!-- Section 1: Media Bias Game (with AI Chatbox) -->
        <div class="section-container active" id="section-1">
            <div class="section-header">
                <h2 class="section-title">Media Bias Sorting Game</h2>
                <p class="section-description">
                    When writing a paper, checking the bias of sources is very important. 
                    Drag the news sources to the correct bins. Use the AI chatbox below if you need help!
                </p>
            </div>

            <div class="content-placeholder">
                <h3>🎮 Media Bias Game Content</h3>
                <p>Insert your media bias sorting game component here</p>
                <p style="margin-top: 20px; font-size: 0.9rem;">
                    (All game logic, drag-drop functionality, timer, leaderboard, and authentication)
                </p>
            </div>

            <div style="margin-top: 40px;">
                <div class="content-placeholder">
                    <h3>💬 AI Chatbox with History</h3>
                    <p>Insert your AI chatbox component here</p>
                    <p style="margin-top: 20px; font-size: 0.9rem;">
                        (Chat interface, conversation history, hint/information modes)
                    </p>
                </div>
            </div>

            <div class="navigation-buttons">
                <button class="nav-btn nav-btn-prev" disabled>
                    ← Previous
                </button>
                <button class="nav-btn nav-btn-next" onclick="nextSection()">
                    Next Section →
                </button>
            </div>
        </div>

        <!-- Section 2: Citation Generator -->
        <div class="section-container" id="section-2">
            <div class="section-header">
                <h2 class="section-title">Citation Generator</h2>
                <p class="section-description">
                    It's important to include correct citations for your work. 
                    There are many formats including MLA, APA, and Chicago. 
                    This tool helps you create proper citations for your sources.
                </p>
            </div>

            <div class="content-placeholder">
                <h3>📚 Citation Generator Tool</h3>
                <p>Insert your citation generator component here</p>
                <p style="margin-top: 20px; font-size: 0.9rem;">
                    (Citation form, format selector, metadata fetching, save/load functionality)
                </p>
            </div>

            <div class="navigation-buttons">
                <button class="nav-btn nav-btn-prev" onclick="prevSection()">
                    ← Previous
                </button>
                <button class="nav-btn nav-btn-next" onclick="nextSection()">
                    Next Section →
                </button>
            </div>
        </div>

        <!-- Section 3: Thesis Generator -->
        <div class="section-container" id="section-3">
            <div class="section-header">
                <h2 class="section-title">Thesis Generator</h2>
                <p class="section-description">
                    Starting your essay can be challenging. Use this AI-powered tool to 
                    generate strong thesis statements that outline your argument effectively.
                </p>
            </div>

            <div class="content-placeholder">
                <h3>✍️ Thesis Generator Tool</h3>
                <p>Insert your thesis generator component here</p>
                <p style="margin-top: 20px; font-size: 0.9rem;">
                    (Thesis form, supporting points, AI generation, strength ratings)
                </p>
            </div>

            <div class="navigation-buttons">
                <button class="nav-btn nav-btn-prev" onclick="prevSection()">
                    ← Previous
                </button>
                <button class="nav-btn nav-btn-next" onclick="nextSection()">
                    Next Section →
                </button>
            </div>
        </div>

        <!-- Section 4: Performance Survey -->
        <div class="section-container" id="section-4">
            <div class="section-header">
                <h2 class="section-title">Performance Reflection</h2>
                <p class="section-description">
                    Rate your understanding and performance on these English skill-building activities. 
                    See how your peers felt and discover resources to help you improve!
                </p>
            </div>

            <div class="content-placeholder">
                <h3>⭐ Performance Survey</h3>
                <p>Insert your performance survey component here</p>
                <p style="margin-top: 20px; font-size: 0.9rem;">
                    (Rating system, class comparison, personalized resources)
                </p>
            </div>

            <div class="navigation-buttons">
                <button class="nav-btn nav-btn-prev" onclick="prevSection()">
                    ← Previous
                </button>
                <button class="nav-btn nav-btn-next" disabled>
                    Complete ✓
                </button>
            </div>
        </div>
    </div>

    <script>
        let currentSection = 1;
        const totalSections = 4;

        function updateProgress() {
            // Update step indicators
            document.querySelectorAll('.step').forEach((step, index) => {
                const stepNum = index + 1;
                step.classList.remove('active', 'completed');
                
                if (stepNum < currentSection) {
                    step.classList.add('completed');
                } else if (stepNum === currentSection) {
                    step.classList.add('active');
                }
            });

            // Update progress line
            const progressPercent = ((currentSection - 1) / (totalSections - 1)) * 100;
            document.getElementById('progress-fill').style.width = progressPercent + '%';

            // Show/hide sections
            document.querySelectorAll('.section-container').forEach((section, index) => {
                section.classList.remove('active');
                if (index + 1 === currentSection) {
                    section.classList.add('active');
                }
            });

            // Scroll to top smoothly
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function nextSection() {
            if (currentSection < totalSections) {
                currentSection++;
                updateProgress();
            }
        }

        function prevSection() {
            if (currentSection > 1) {
                currentSection--;
                updateProgress();
            }
        }

        // Allow direct navigation by clicking steps
        document.querySelectorAll('.step').forEach((step) => {
            step.addEventListener('click', function() {
                const targetStep = parseInt(this.dataset.step);
                // Only allow going to completed or current step
                if (targetStep <= currentSection) {
                    currentSection = targetStep;
                    updateProgress();
                }
            });
        });

        // Initialize
        updateProgress();
    </script>
</body>
</html>