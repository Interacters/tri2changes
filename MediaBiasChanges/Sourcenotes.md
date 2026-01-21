<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        .source-tools-container {
            display: grid;
            grid-template-columns: 55% 45%;
            gap: 15px;
            margin-top: 25px;
            font-family: 'Inter', sans-serif;
        }

        .tool-card {
            background: linear-gradient(160deg, #555dc2d2, #564ea0ff);
            border-radius: 12px;
            padding: 18px;
            color: #ffffff;
        }

        .tool-card h3 {
            margin: 0 0 12px 0;
            font-size: 1.2rem;
            color: #ffffff;
        }

        .tool-card-description {
            font-size: 0.85rem;
            color: rgba(255,255,255,0.8);
            margin-bottom: 15px;
        }

        .source-item {
            background: rgba(255,255,255,0.1);
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 10px;
            position: relative;
        }

        .source-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }

        .source-title {
            font-weight: 600;
            font-size: 0.95rem;
            color: #ffffff;
        }

        .source-meta {
            font-size: 0.8rem;
            color: rgba(255,255,255,0.7);
            margin-bottom: 8px;
        }

        .source-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 8px;
        }

        .tag {
            background: rgba(255,255,255,0.2);
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.75rem;
            color: #ffffff;
        }

        .btn-small {
            padding: 4px 10px;
            border-radius: 6px;
            border: none;
            font-size: 0.75rem;
            cursor: pointer;
            font-weight: 600;
            background: rgba(255,255,255,0.2);
            color: #ffffff;
            transition: all 0.2s;
        }

        .btn-small:hover {
            background: rgba(255,255,255,0.3);
        }

        .btn-delete {
            background: rgba(248, 113, 113, 0.3);
        }

        .btn-delete:hover {
            background: rgba(248, 113, 113, 0.5);
        }

        .add-source-form {
            display: grid;
            gap: 8px;
            margin-bottom: 12px;
        }

        .form-input {
            padding: 8px;
            border-radius: 6px;
            border: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.15);
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
        }

        .form-input::placeholder {
            color: rgba(255,255,255,0.6);
        }

        .form-textarea {
            min-height: 60px;
            resize: vertical;
        }

        .form-select {
            padding: 8px;
            border-radius: 6px;
            border: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.15);
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            cursor: pointer;
        }

        .form-select option {
            background: #564ea0ff;
            color: #ffffff;
        }

        .synthesis-panel {
            background: rgba(0,0,0,0.2);
            border-radius: 8px;
            padding: 12px;
            margin-top: 12px;
        }

        .synthesis-panel h4 {
            margin: 0 0 8px 0;
            font-size: 0.95rem;
            color: #7ad2f9;
        }

        .synthesis-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .synthesis-list li {
            padding: 6px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            font-size: 0.8rem;
            color: rgba(255,255,255,0.9);
        }

        .notes-sidebar {
            position: fixed;
            right: -350px;
            top: 0;
            width: 350px;
            height: 100vh;
            background: linear-gradient(160deg, #555dc2d2, #564ea0ff);
            box-shadow: -5px 0 15px rgba(0,0,0,0.3);
            transition: right 0.3s ease;
            z-index: 1000;
            overflow-y: auto;
            padding: 20px;
            color: #ffffff;
        }

        .notes-sidebar.open {
            right: 0;
        }

        .notes-toggle {
            position: fixed;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            background: linear-gradient(160deg, #555dc2d2, #564ea0ff);
            color: #ffffff;
            padding: 15px 10px;
            border-radius: 8px 0 0 8px;
            cursor: pointer;
            z-index: 999;
            font-weight: 600;
            font-size: 0.9rem;
            border: none;
            box-shadow: -3px 0 10px rgba(0,0,0,0.2);
        }

        .notes-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .notes-header h3 {
            margin: 0;
            font-size: 1.2rem;
        }

        .note-item {
            background: rgba(255,255,255,0.1);
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 12px;
        }

        .note-source {
            font-weight: 600;
            color: #7ad2f9;
            margin-bottom: 6px;
            font-size: 0.9rem;
        }

        .note-content {
            font-size: 0.85rem;
            line-height: 1.5;
            color: rgba(255,255,255,0.9);
        }

        .note-date {
            font-size: 0.7rem;
            color: rgba(255,255,255,0.6);
            margin-top: 8px;
        }

        .empty-state {
            text-align: center;
            padding: 40px 20px;
            color: rgba(255,255,255,0.6);
            font-style: italic;
        }

        @media (max-width: 1024px) {
            .source-tools-container {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 768px) {
            .source-tools-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="source-tools-container">
        <!-- Source Synthesis Helper -->
        <div class="tool-card">
            <h3>Source Tracker</h3>
            <p class="tool-card-description">
                Track your sources and identify trends, gaps, and contradictions
            </p>

            <form class="add-source-form" id="add-source-form">
                <input type="text" class="form-input" id="source-url" placeholder="Source URL" required>
                <select class="form-select" id="source-category">
                    <option value="">Select category...</option>
                    <option value="supports">Supports my argument</option>
                    <option value="contradicts">Contradicts my argument</option>
                    <option value="background">Background/Context</option>
                    <option value="methodology">Methodology</option>
                    <option value="data">Data/Statistics</option>
                </select>
                <textarea class="form-input form-textarea" id="source-key-point" placeholder="Key point or quote"></textarea>
                <button type="submit" class="btn-small" style="background: #7ad2f9; color: #082033;">Add Source</button>
            </form>

            <div id="sources-list"></div>

            <div class="synthesis-panel">
                <h4>Synthesis Insights</h4>
                <ul class="synthesis-list" id="synthesis-insights">
                    <li>Add sources to see patterns and insights</li>
                </ul>
            </div>
        </div>

        <!-- Quick References -->
        <div class="tool-card">
            <h3>References Tracker</h3>
            <p class="tool-card-description">
                Track what your sources are referencing
            </p>

            <form class="add-source-form" id="add-reference-form">
                <select class="form-select" id="ref-parent-source">
                    <option value="">Select parent source...</option>
                </select>
                <input type="text" class="form-input" id="ref-url" placeholder="Reference URL" required>
                <input type="text" class="form-input" id="ref-title" placeholder="Reference title">
                <button type="submit" class="btn-small" style="background: #7ad2f9; color: #082033;">Add Reference</button>
            </form>

            <div id="references-list"></div>
        </div>
    </div>

    <!-- Notes Sidebar -->
    <button class="notes-toggle" id="notes-toggle">📝 Notes</button>
    <div class="notes-sidebar" id="notes-sidebar">
        <div class="notes-header">
            <h3>Source Notes</h3>
            <button class="btn-small" id="close-notes">✕</button>
        </div>

        <form class="add-source-form" id="add-note-form">
            <select class="form-select" id="note-source-select">
                <option value="">Select source...</option>
            </select>
            <textarea class="form-input form-textarea" id="note-content" placeholder="Write your notes here..." required></textarea>
            <button type="submit" class="btn-small" style="background: #7ad2f9; color: #082033;">Save Note</button>
        </form>

        <div id="notes-list"></div>
    </div>

    <script>
        const STORAGE_KEY = 'essay_sources_v1';
        const NOTES_KEY = 'essay_notes_v1';

        // Load data from localStorage
        function loadData() {
            const sources = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
            const notes = JSON.parse(localStorage.getItem(NOTES_KEY) || '[]');
            return { sources, notes };
        }

        function saveData(sources, notes) {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(sources));
            if (notes) localStorage.setItem(NOTES_KEY, JSON.stringify(notes));
        }

        function renderSources() {
            const { sources } = loadData();
            const container = document.getElementById('sources-list');
            const parentSelect = document.getElementById('ref-parent-source');
            const noteSelect = document.getElementById('note-source-select');

            if (!sources.length) {
                container.innerHTML = '<div class="empty-state">No sources added yet</div>';
                parentSelect.innerHTML = '<option value="">No sources available</option>';
                noteSelect.innerHTML = '<option value="">No sources available</option>';
                updateSynthesis([]);
                return;
            }

            // Render sources list
            container.innerHTML = sources.map((source, index) => `
                <div class="source-item">
                    <div class="source-header">
                        <div class="source-title">${extractDomain(source.url)}</div>
                        <button class="btn-small btn-delete" onclick="deleteSource(${index})">✕</button>
                    </div>
                    ${source.keyPoint ? `<div style="font-size: 0.8rem; color: rgba(255,255,255,0.9); margin-top: 6px;">${source.keyPoint}</div>` : ''}
                    <div class="source-tags">
                        ${source.category ? `<span class="tag">${source.category}</span>` : ''}
                        ${source.references?.length ? `<span class="tag">${source.references.length} refs</span>` : ''}
                    </div>
                </div>
            `).join('');

            // Update dropdowns
            const options = sources.map((s, i) => `<option value="${i}">${extractDomain(s.url)}</option>`).join('');
            parentSelect.innerHTML = '<option value="">Select parent source...</option>' + options;
            noteSelect.innerHTML = '<option value="">Select source...</option>' + options;

            updateSynthesis(sources);
        }

        function extractDomain(url) {
            try {
                const domain = new URL(url).hostname.replace('www.', '');
                return domain;
            } catch {
                return url.substring(0, 30) + (url.length > 30 ? '...' : '');
            }
        }

        function updateSynthesis(sources) {
            const container = document.getElementById('synthesis-insights');
            if (!sources.length) {
                container.innerHTML = '<li>Add sources to see patterns and insights</li>';
                return;
            }

            const insights = [];
            const categories = {};
            sources.forEach(s => {
                if (s.category) categories[s.category] = (categories[s.category] || 0) + 1;
            });

            const totalRefs = sources.reduce((sum, s) => sum + (s.references?.length || 0), 0);

            insights.push(`<strong>${sources.length}</strong> sources tracked`);
            if (totalRefs) insights.push(`<strong>${totalRefs}</strong> total references found`);
            
            Object.entries(categories).forEach(([cat, count]) => {
                insights.push(`<strong>${count}</strong> ${cat} sources`);
            });

            if (categories.supports && categories.contradicts) {
                insights.push('⚠️ You have both supporting and contradicting sources - good for synthesis!');
            }

            container.innerHTML = insights.map(i => `<li>${i}</li>`).join('');
        }

        document.getElementById('add-source-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const { sources, notes } = loadData();

            const newSource = {
                id: Date.now(),
                url: document.getElementById('source-url').value,
                category: document.getElementById('source-category').value,
                keyPoint: document.getElementById('source-key-point').value,
                references: [],
                addedAt: new Date().toISOString()
            };

            sources.push(newSource);
            saveData(sources, notes);
            renderSources();
            renderNotes();
            e.target.reset();
        });

        document.getElementById('add-reference-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const { sources, notes } = loadData();
            const parentIndex = document.getElementById('ref-parent-source').value;

            if (parentIndex === '') {
                alert('Please select a parent source');
                return;
            }

            const reference = {
                url: document.getElementById('ref-url').value,
                title: document.getElementById('ref-title').value
            };

            if (!sources[parentIndex].references) {
                sources[parentIndex].references = [];
            }
            sources[parentIndex].references.push(reference);

            saveData(sources, notes);
            renderSources();
            renderReferences();
            e.target.reset();
        });

        function renderReferences() {
            const { sources } = loadData();
            const container = document.getElementById('references-list');

            const sourcesWithRefs = sources.filter(s => s.references?.length);
            if (!sourcesWithRefs.length) {
                container.innerHTML = '<div class="empty-state">No references tracked yet</div>';
                return;
            }

            container.innerHTML = sourcesWithRefs.map(source => `
                <div class="source-item">
                    <div class="source-title" style="margin-bottom: 8px;">${extractDomain(source.url)}</div>
                    ${source.references.map(ref => `
                        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.8); padding-left: 12px; margin-top: 4px;">
                            → <a href="${ref.url}" target="_blank" style="color: #7ad2f9; text-decoration: none;">${ref.title || extractDomain(ref.url)}</a>
                        </div>
                    `).join('')}
                </div>
            `).join('');
        }

        window.deleteSource = function(index) {
            if (!confirm('Delete this source?')) return;
            const { sources, notes } = loadData();
            sources.splice(index, 1);
            saveData(sources, notes);
            renderSources();
            renderReferences();
            renderNotes();
        };

        // Notes sidebar
        document.getElementById('notes-toggle').addEventListener('click', () => {
            document.getElementById('notes-sidebar').classList.add('open');
        });

        document.getElementById('close-notes').addEventListener('click', () => {
            document.getElementById('notes-sidebar').classList.remove('open');
        });

        document.getElementById('add-note-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const { sources, notes } = loadData();
            const sourceIndex = document.getElementById('note-source-select').value;

            if (sourceIndex === '') {
                alert('Please select a source');
                return;
            }

            const newNote = {
                sourceId: sources[sourceIndex].id,
                sourceTitle: extractDomain(sources[sourceIndex].url),
                content: document.getElementById('note-content').value,
                createdAt: new Date().toISOString()
            };

            notes.push(newNote);
            saveData(sources, notes);
            renderNotes();
            e.target.reset();
        });

        function renderNotes() {
            const { notes } = loadData();
            const container = document.getElementById('notes-list');

            if (!notes.length) {
                container.innerHTML = '<div class="empty-state">No notes yet. Select a source and start writing!</div>';
                return;
            }

            container.innerHTML = notes.reverse().map((note, index) => `
                <div class="note-item">
                    <div class="note-source">${note.sourceTitle}</div>
                    <div class="note-content">${note.content}</div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div class="note-date">${new Date(note.createdAt).toLocaleDateString()}</div>
                        <button class="btn-small btn-delete" onclick="deleteNote(${notes.length - 1 - index})">Delete</button>
                    </div>
                </div>
            `).join('');
        }

        window.deleteNote = function(index) {
            if (!confirm('Delete this note?')) return;
            const { sources, notes } = loadData();
            notes.splice(index, 1);
            saveData(sources, notes);
            renderNotes();
        };

        // Initialize
        renderSources();
        renderReferences();
        renderNotes();
    </script>
</body>
</html>