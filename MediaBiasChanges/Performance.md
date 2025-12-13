<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .survey-container {
            background: rgba(113, 117, 193, 0.82);
            backdrop-filter: blur(20px);
            padding: 60px 50px;
            border-radius: 30px;
            max-width: 800px;
            width: 100%;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.4);
            position: relative;
            overflow: hidden;
        }

        .survey-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 8px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #4facfe);
            background-size: 300% 300%;
            animation: gradientShift 4s ease infinite;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .survey-header {
            text-align: center;
            margin-bottom: 45px;
        }

        .survey-header h2 {
            font-size: 2.5rem;
            background: #fff
            background-clip: text;
            margin-bottom: 15px;
            font-weight: 800;
        }

        .survey-header p {
            color: #4a5568;
            font-size: 1.1rem;
            line-height: 1.7;
            animation: fadeIn 1s ease-out 0.3s backwards;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .rating-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }

        .rating-option {
            position: relative;
            cursor: pointer;
            animation: fadeInUp 0.6s ease-out backwards;
        }

        .rating-option:nth-child(1) { animation-delay: 0.1s; }
        .rating-option:nth-child(2) { animation-delay: 0.2s; }
        .rating-option:nth-child(3) { animation-delay: 0.3s; }
        .rating-option:nth-child(4) { animation-delay: 0.4s; }
        .rating-option:nth-child(5) { animation-delay: 0.5s; }

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

        .rating-option input {
            display: none;
        }

        .rating-label {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px 15px;
            border: 3px solid #e2e8f0;
            border-radius: 20px;
            background: white;
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
            overflow: hidden;
        }

        .rating-label::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, #667eea, #764ba2);
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 0;
        }

        .rating-label > * {
            position: relative;
            z-index: 1;
        }

        .rating-number {
            font-size: 3rem;
            font-weight: 800;
            color: #667eea;
            transition: all 0.3s;
            margin-bottom: 10px;
        }

        .rating-text {
            font-size: 0.9rem;
            color: #718096;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s;
        }

        .rating-option:hover .rating-label {
            border-color: #667eea;
            transform: translateY(-8px) scale(1.05);
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        }

        .rating-option input:checked + .rating-label {
            border-color: #667eea;
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
            transform: scale(1.05);
        }

        .rating-option input:checked + .rating-label::before {
            opacity: 1;
        }

        .rating-option input:checked + .rating-label .rating-number,
        .rating-option input:checked + .rating-label .rating-text {
            color: white;
        }

        .submit-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 15px;
            font-size: 1.2rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            position: relative;
            overflow: hidden;
        }

        .submit-btn::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .submit-btn span {
            position: relative;
            z-index: 1;
        }

        .submit-btn:hover::before {
            opacity: 1;
        }

        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
        }

        .submit-btn:active {
            transform: translateY(-1px);
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

        /* Modal Styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 10000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            animation: fadeIn 0.3s ease-out;
            overflow-y: auto;
        }

        .modal-content {
            background: #9281b3ff
            margin: 3% auto;
            padding: 50px;
            border-radius: 30px;
            width: 90%;
            max-width: 700px;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.5);
            animation: slideInScale 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
        }

        @keyframes slideInScale {
            from {
                transform: translateY(-100px) scale(0.8);
                opacity: 0;
            }
            to {
                transform: translateY(0) scale(1);
                opacity: 1;
            }
        }

        .modal-close {
            position: absolute;
            right: 25px;
            top: 25px;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #f3f4f6;
            border: none;
            font-size: 24px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
            color: #4a5568;
        }

        .modal-close:hover {
            background: #e2e8f0;
            transform: rotate(90deg);
        }

        .result-badge {
            display: inline-block;
            padding: 12px 30px;
            border-radius: 50px;
            font-weight: 700;
            font-size: 1rem;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .badge-underprepared {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }

        .badge-average {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
        }

        .badge-overprepared {
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            color: white;
        }

        .result-title {
            font-size: 2.2rem;
            color: #1a202c;
            margin-bottom: 20px;
            font-weight: 800;
        }

        .result-message {
            font-size: 1.2rem;
            color: #4a5568;
            line-height: 1.8;
            margin-bottom: 35px;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 35px;
        }

        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
        }

        .stat-value {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .resources-section {
            background: #7973a8ff;
            padding: 30px;
            border-radius: 20px;
            margin-top: 30px;
            border: 2px solid #e2e8f0;
        }

        .resources-title {
            font-size: 1.5rem;
            color: #667eea;
            margin-bottom: 15px;
            font-weight: 700;
        }

        .resources-intro {
            color: #4a5568;
            margin-bottom: 20px;
            font-style: italic;
        }

        .resource-item {
            padding: 15px 20px;
            margin-bottom: 10px;
            background: white;
            border-radius: 10px;
            border-left: 4px solid #667eea;
            transition: all 0.3s;
        }

        .resource-item:hover {
            transform: translateX(8px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .resource-item a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            display: block;
        }

        .resource-item a:hover {
            color: #764ba2;
        }

        .modal-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 15px;
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 25px;
        }

        .modal-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }

        @media (max-width: 768px) {
            .survey-container {
                padding: 40px 30px;
            }

            .survey-header h2 {
                font-size: 2rem;
            }

            .rating-grid {
                grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
                gap: 15px;
            }

            .rating-number {
                font-size: 2.5rem;
            }

            .modal-content {
                padding: 35px 25px;
                width: 95%;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="survey-container">
        <div class="survey-header">
            <h2>Performance Reflection</h2>
            <p>Rate your understanding and performance on the English skill building activities of media bias, thesis writing, and understanding citations. Let's see how your peers felt, and how you can improve next time.</p>
        </div>

        <form id="survey-form">
            <div class="rating-grid">
                <div class="rating-option">
                    <input type="radio" id="rating-1" name="rating" value="1">
                    <label for="rating-1" class="rating-label">
                        <span class="rating-number">1</span>
                        <span class="rating-text">Poor</span>
                    </label>
                </div>
                <div class="rating-option">
                    <input type="radio" id="rating-2" name="rating" value="2">
                    <label for="rating-2" class="rating-label">
                        <span class="rating-number">2</span>
                        <span class="rating-text">Fair</span>
                    </label>
                </div>
                <div class="rating-option">
                    <input type="radio" id="rating-3" name="rating" value="3">
                    <label for="rating-3" class="rating-label">
                        <span class="rating-number">3</span>
                        <span class="rating-text">Good</span>
                    </label>
                </div>
                <div class="rating-option">
                    <input type="radio" id="rating-4" name="rating" value="4">
                    <label for="rating-4" class="rating-label">
                        <span class="rating-number">4</span>
                        <span class="rating-text">Excellent</span>
                    </label>
                </div>
                <div class="rating-option">
                    <input type="radio" id="rating-5" name="rating" value="5">
                    <label for="rating-5" class="rating-label">
                        <span class="rating-number">5</span>
                        <span class="rating-text">Superior</span>
                    </label>
                </div>
            </div>

            <button type="submit" class="submit-btn" id="submit-btn">
                <span>Submit Rating</span>
            </button>
        </form>
    </div>

    <div id="results-modal" class="modal">
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            
            <div id="result-badge"></div>
            <h2 class="result-title" id="result-title"></h2>
            <p class="result-message" id="result-message"></p>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value" id="your-rating">-</div>
                    <div class="stat-label">Your Rating</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="class-avg">-</div>
                    <div class="stat-label">Class Average</div>
                </div>
            </div>

            <div class="resources-section">
                <h3 class="resources-title" id="resources-title"></h3>
                <p class="resources-intro" id="resources-intro"></p>
                <div id="resources-list"></div>
            </div>

            <button class="modal-btn" onclick="closeModal()">Got it, thanks!</button>
        </div>
    </div>

    <script>
        const resourcesByTier = {
            1: {
                title: 'Building Foundations',
                intro: 'Start with these fundamentals to strengthen your English skills:',
                items: [
                    { text: 'Grammarly Handbook - Grammar Basics', url: 'https://www.grammarly.com/blog/category/handbook/' },
                    { text: 'Khan Academy Grammar Course (Free)', url: 'https://www.khanacademy.org/humanities/grammar' },
                    { text: 'Basic Essay Structure (YouTube)', url: 'https://www.youtube.com/watch?v=sQEr5D1sSrU' },
                    { text: 'Purdue OWL - Writing Process Guide', url: 'https://owl.purdue.edu/owl/general_writing/the_writing_process/index.html' },
                    { text: 'Quizlet - Vocabulary Building', url: 'https://quizlet.com/subject/english-vocabulary/' }
                ]
            },
            2: {
                title: 'Developing Skills',
                intro: "You're on the right track! These resources will help you improve:",
                items: [
                    { text: 'MLA Citation Guide - Purdue OWL', url: 'https://owl.purdue.edu/owl/research_and_citation/mla_style/mla_formatting_and_style_guide/mla_formatting_and_style_guide.html' },
                    { text: 'Hemingway Editor - Improve Clarity', url: 'https://www.hemingwayapp.com/' },
                    { text: 'How to Write a Thesis Statement', url: 'https://www.youtube.com/watch?v=AzcJP7WS_5A' },
                    { text: 'UNC Writing Center - Essay Tips', url: 'https://writingcenter.unc.edu/tips-and-tools/' },
                    { text: 'Coursera - Academic English Writing (Free)', url: 'https://www.coursera.org/learn/writing-skills' }
                ]
            },
            3: {
                title: 'Solidifying Skills',
                intro: "You're right on track! Strengthen your skills with these:",
                items: [
                    { text: 'APA Format Guide - Research Papers', url: 'https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/general_format.html' },
                    { text: 'Thesaurus.com - Vocabulary Enhancement', url: 'https://www.thesaurus.com/' },
                    { text: 'Literary Analysis Techniques', url: 'https://www.youtube.com/watch?v=mhHfnhh-pB4' },
                    { text: 'Harvard Writing Center - Essay Strategies', url: 'https://writingcenter.fas.harvard.edu/pages/strategies-essay-writing' },
                    { text: 'edX - Advanced Grammar Course', url: 'https://www.edx.org/learn/english-grammar' }
                ]
            },
            4: {
                title: 'Advancing Excellence',
                intro: 'Great work! Take your skills to the next level:',
                items: [
                    { text: 'The New Yorker - Literary Journalism', url: 'https://www.newyorker.com/culture/culture-desk' },
                    { text: 'Literary Devices Guide - Advanced Analysis', url: 'https://literarydevices.net/' },
                    { text: 'Advanced Rhetorical Analysis', url: 'https://www.youtube.com/watch?v=QUF-5UDtRJs' },
                    { text: 'MLA Style Center - Advanced Citations', url: 'https://style.mla.org/' },
                    { text: 'MasterClass - Creative Writing (Paid)', url: 'https://www.masterclass.com/classes/margaret-atwood-teaches-creative-writing' }
                ]
            },
            5: {
                title: '🚀 Mastery Level',
                intro: 'Exceptional! Challenge yourself with these advanced resources:',
                items: [
                    { text: 'London Review of Books - Critical Essays', url: 'https://www.lrb.co.uk/' },
                    { text: 'JSTOR - Academic Research Database', url: 'https://www.jstor.org/' },
                    { text: 'Yale Lecture Series - Literary Theory', url: 'https://www.youtube.com/watch?v=8y8BXcjUNVU' },
                    { text: 'Chicago Manual of Style - Professional Writing', url: 'https://www.chicagomanualofstyle.org/home.html' },
                    { text: 'Poetry Foundation - Advanced Literary Forms', url: 'https://www.poets.org/poetsorg/text/learning-guide-poetry-terms' },
                    { text: 'Stanford Philosophy - Critical Thinking', url: 'https://philosophy.stanford.edu/teaching-guide' }
                ]
            }
        };

        document.getElementById('survey-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const rating = document.querySelector('input[name="rating"]:checked');
            if (!rating) {
                alert('Please select a rating before submitting.');
                return;
            }

            const submitBtn = document.getElementById('submit-btn');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<div class="loading"></div>';

            try {
                const response = await fetch('http://localhost:8001/api/performance/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ rating: parseInt(rating.value) })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    showResults(data);
                } else {
                    alert('Error: ' + (data.error || 'Unknown error occurred'));
                }
            } catch (error) {
                alert('Failed to submit. Please ensure your Flask server is running on port 8001.');
                console.error(error);
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<span>Submit Rating</span>';
            }
        });

        function showResults(data) {
            const badgeColors = {
                'underprepared': 'badge-underprepared',
                'average': 'badge-average',
                'overprepared': 'badge-overprepared'
            };

            const titles = {
                'underprepared': "Let's Build Your Skills!",
                'overprepared': 'Excellent Work!',
                'average': "You're On Track!"
            };

            document.getElementById('result-badge').innerHTML = 
                `<span class="result-badge ${badgeColors[data.status]}">${data.status.toUpperCase()}</span>`;
            document.getElementById('result-title').textContent = titles[data.status] || 'Your Results';
            document.getElementById('result-message').textContent = data.message;
            document.getElementById('your-rating').textContent = data.your_rating;
            document.getElementById('class-avg').textContent = data.average_rating;

            const resources = resourcesByTier[data.your_rating];
            document.getElementById('resources-title').textContent = resources.title;
            document.getElementById('resources-intro').textContent = resources.intro;
            
            const resourcesList = document.getElementById('resources-list');
            resourcesList.innerHTML = resources.items.map(item => 
                `<div class="resource-item">
                    <a href="${item.url}" target="_blank">${item.text}</a>
                </div>`
            ).join('');

            document.getElementById('results-modal').style.display = 'block';
        }

        function closeModal() {
            document.getElementById('results-modal').style.display = 'none';
        }

        window.onclick = function(event) {
            const modal = document.getElementById('results-modal');
            if (event.target === modal) {
                closeModal();
            }
        }
    </script>
</body>
</html>