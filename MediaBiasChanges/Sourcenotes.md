<style>
  /* Import modern, readable font matching thesis generator */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

   .cite-card { 
    background: #a7a0d4; 
    color:#ffffff; 
    padding:18px; 
    border-radius:12px; 
    margin:20px 0;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  }
  
  .cite-row { 
    display: flex; 
    gap: 10px;
    flex-wrap: wrap;
    align-items: center;
    margin-top: 8px;
  }
  
  .cite-label { 
    min-width: 110px;
    font-weight:700; 
    color: #0b0839;
    font-size: 0.9rem;
  }
  
  .cite-input, .cite-select { 
    flex: 1;
    padding:8px; 
    border-radius:6px; 
    border:1px solid rgba(255,255,255,0.2); 
    background:rgba(255,255,255,0.15); 
    color:#ffffff;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
  }
  
  .cite-input::placeholder {
    color: rgba(255, 255, 255, 0.6);
  }
  
  .cite-select option {
    background: #564ea0ff;
    color: #ffffff;
  }
  
  .cite-actions { 
    display:flex; 
    gap:10px; 
    margin-top:12px; 
    justify-content:flex-end;
    flex-wrap: wrap;
  }
  
  .cite-btn { 
    padding:8px 12px; 
    border-radius:8px; 
    border:none; 
    cursor:pointer; 
    font-weight:700;
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
  }
  
  .cite-btn.primary { 
    background:#7ad2f9; 
    color:#082033; 
  }
  
  .cite-btn.ghost { 
    background:rgba(255,255,255,0.15); 
    color: #292745ad; 
    border:1px solid rgba(255,255,255,0.2); 
  }

  .cite-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }
  
  .cite-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
  
  .btn-hint {
    font-size: 0.7rem;
    color: rgba(255, 255, 255, 0.8);
    font-weight: 400;
  }
  
  .cite-output { 
    margin-top:12px; 
    background:rgba(0,0,0,0.25); 
    padding:12px; 
    border-radius:8px; 
    font-family: 'Inter', sans-serif;
    color:#ffffff;
    font-size: 0.9rem;
  }
  
  .cite-output:empty::before {
    content: 'Your citation will appear here...';
    color: rgba(255, 255, 255, 0.6);
    font-style: italic;
  }
  
  .cite-small { 
    font-size:0.9rem; 
    color:rgba(255, 255, 255, 0.75); 
    margin-top:6px;
  }
  
  .works-cited-section {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid rgba(255,255,255,0.2);
  }
  
  .works-cited-section h3 {
    font-size: 1.2rem;
    color: #ffffff;
    margin-bottom: 12px;
    font-family: 'Inter', sans-serif;
  }
  
  .works-cited-list {
    background: rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 10px;
    padding: 12px;
    max-height: 320px;
    overflow-y: auto;
  }
  
  .works-cited-list:empty::before {
    content: 'No saved citations yet. Click "Save" to add citations to your Works Cited list.';
    color: rgba(255, 255, 255, 0.7);
    font-style: italic;
    display: block;
    text-align: center;
    padding: 20px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
  }
  
  .citation-item {
    padding: 10px;
    margin-bottom: 10px;
    background: rgba(255,255,255,0.1);
    border-left: 4px solid #7ad2f9;
    border-radius: 6px;
    position: relative;
    padding-right: 80px;
  }
  
  .citation-item:last-child {
    margin-bottom: 0;
  }
  
  .citation-text {
    color: #ffffff;
    font-size: 0.85rem;
    line-height: 1.45;
    font-family: 'Inter', sans-serif;
  }

  .citation-actions {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    gap: 4px;
  }

  .citation-note-btn {
    background: rgba(122, 210, 249, 0.8);
    color: white;
    border: none;
    border-radius: 6px;
    width: 28px;
    height: 28px;
    cursor: pointer;
    font-weight: bold;
    font-size: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    font-family: 'Inter', sans-serif;
  }

  .citation-note-btn:hover {
    background: rgba(122, 210, 249, 1);
    transform: scale(1.1);
  }
  
  .citation-delete {
    background: rgba(248, 113, 113, 0.8);
    color: white;
    border: none;
    border-radius: 6px;
    width: 28px;
    height: 28px;
    cursor: pointer;
    font-weight: bold;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    font-family: 'Inter', sans-serif;
  }
  
  .citation-delete:hover {
    background: rgba(248, 113, 113, 1);
    transform: scale(1.1);
  }

  .cite-input.missing {
    border: 2px solid #f87171 !important;
    background: rgba(248, 113, 113, 0.2) !important;
  }

  .cite-warning {
    margin-top: 10px;
    padding: 10px;
    border-radius: 8px;
    background: rgba(248, 113, 113, 0.15);
    color: #fff;
    font-size: 0.85rem;
    font-family: 'Inter', sans-serif;
  }

  /* Source Notes Panel - FIXED WIDTH */
  .notes-panel {
    position: fixed;
    right: -320px;
    top: 0;
    width: 300px;
    max-width: 90vw;
    height: 100vh;
    background: linear-gradient(160deg, #564ea0ee, #3b3666ee);
    color: #fff;
    box-shadow: -8px 0 40px rgba(0,0,0,0.5);
    padding: 20px;
    transition: right 0.3s ease;
    z-index: 10000;
    overflow-y: auto;
    font-family: 'Inter', sans-serif;
  }
  
  .notes-panel.open { 
    right: 0; 
  }
  
  .notes-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 2px solid rgba(255,255,255,0.2);
  }

  .notes-header h3 { 
    margin: 0;
    font-size: 1.2rem;
    color: #fff;
  }

  .notes-close-btn {
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff;
    padding: 6px 12px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 600;
    font-size: 0.85rem;
    transition: all 0.2s;
  }

  .notes-close-btn:hover {
    background: rgba(255,255,255,0.25);
  }
  
  .notes-intro { 
    font-size: 0.85rem;
    color: rgba(255,255,255,0.85);
    margin-bottom: 16px;
    line-height: 1.5;
  }
  
  .notes-section {
    margin-bottom: 20px;
  }

  .notes-section h4 {
    font-size: 1rem;
    color: #7ad2f9;
    margin-bottom: 10px;
  }

  .source-select {
    width: 100%;
    padding: 8px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.2);
    background: rgba(255,255,255,0.15);
    color: #fff;
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    margin-bottom: 10px;
  }

  .source-select option {
    background: #3b3666;
    color: #fff;
  }

  .note-category-select {
    width: 100%;
    padding: 8px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.2);
    background: rgba(255,255,255,0.15);
    color: #fff;
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    margin-bottom: 10px;
  }

  .note-category-select option {
    background: #3b3666;
    color: #fff;
  }

  .note-textarea {
    width: 100%;
    min-height: 70px;
    padding: 8px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.2);
    background: rgba(255,255,255,0.15);
    color: #fff;
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    resize: vertical;
    margin-bottom: 10px;
  }

  .note-textarea::placeholder {
    color: rgba(255,255,255,0.6);
  }

  .add-note-btn {
    width: 100%;
    padding: 8px;
    background: #7ad2f9;
    color: #082033;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.2s;
  }

  .add-note-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(122, 210, 249, 0.4);
  }

  .add-note-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .notes-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .note-item {
    background: rgba(255,255,255,0.1);
    padding: 10px;
    border-radius: 8px;
    border-left: 3px solid #7ad2f9;
    position: relative;
    padding-right: 35px;
  }

  .note-category {
    display: inline-block;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.7rem;
    font-weight: 600;
    margin-bottom: 4px;
  }

  .note-category.supports {
    background: rgba(155, 231, 196, 0.3);
    color: #9be7c4;
  }

  .note-category.contradicts {
    background: rgba(248, 113, 113, 0.3);
    color: #fca5a5;
  }

  .note-category.background {
    background: rgba(122, 210, 249, 0.3);
    color: #7ad2f9;
  }

  .note-category.data {
    background: rgba(251, 191, 36, 0.3);
    color: #fbbf24;
  }

  .note-content {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.95);
    line-height: 1.4;
    margin-bottom: 6px;
  }

  .note-meta {
    font-size: 0.7rem;
    color: rgba(255,255,255,0.6);
  }

  .note-delete-btn {
    position: absolute;
    right: 8px;
    top: 8px;
    background: rgba(248, 113, 113, 0.8);
    color: white;
    border: none;
    border-radius: 4px;
    width: 22px;
    height: 22px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 600;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .note-delete-btn:hover {
    background: rgba(248, 113, 113, 1);
    transform: scale(1.1);
  }

  .empty-state {
    text-align: center;
    padding: 20px 15px;
    color: rgba(255,255,255,0.6);
    font-style: italic;
    font-size: 0.85rem;
  }
</style>

<div class="cite-card" id="citation-tool">
  <div class="cite-row">
    <div class="cite-label">Style</div>
    <select id="cite-style" class="cite-select">
      <option value="apa">APA</option>
      <option value="mla">MLA (9th ed.)</option>
      <option value="chicago">Chicago (author-date)</option>
    </select>
  </div>

  <div class="cite-row">
    <div class="cite-label">Author(s)</div>
    <input id="cite-author" class="cite-input" placeholder="e.g., Doe, J.; Last, F." />
  </div>

  <div class="cite-row">
    <div class="cite-label">Date</div>
    <input id="cite-date" class="cite-input" placeholder="e.g., 2025, May 10 or 2025" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Title</div>
    <input id="cite-title" class="cite-input" placeholder="Article title" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Source</div>
    <input id="cite-source" class="cite-input" placeholder="e.g., The New York Times" />
  </div>

  <div class="cite-row">
    <div class="cite-label">URL</div>
    <input id="cite-url" class="cite-input" placeholder="https://..." />
    <button id="cite-fetch-metadata" class="cite-btn ghost" title="Generate citation from URL" style="margin-left:8px;min-width:160px;">
      Generate from URL
    </button>
  </div>

  <div class="cite-actions">
    <button id="cite-generate" class="cite-btn primary">Generate</button>
    <button id="cite-reset" class="cite-btn ghost"> Reset <span class="btn-hint">(clear fields)</span> </button>
    <button id="cite-copy" class="cite-btn ghost">
      Copy <span class="btn-hint">(to clipboard)</span>
    </button>
    <button id="cite-save" class="cite-btn ghost" title="Save locally">
      Save <span class="btn-hint">(add to Works Cited)</span>
    </button>
    <button id="cite-load" class="cite-btn ghost" title="Load last">
      Load <span class="btn-hint">(view Works Cited)</span>
    </button>
    <button id="cite-notes-toggle" class="cite-btn ghost" title="Open notes panel">
      📝 Notes
    </button>
  </div>

  <div id="cite-output" class="cite-output" aria-live="polite"></div>
  <div id="cite-parenthetical" class="cite-output" style="margin-top:8px;"></div>
  <div id="cite-warning" class="cite-warning" style="display:none;"></div>
  <div class="cite-small">Formats: APA, MLA (9th ed.), Chicago (author-date). Saved citations are stored locally in your browser.</div>

  <div class="works-cited-section" id="works-cited-section" style="display: none;">
    <h3>Works Cited</h3>
    <div id="works-cited-list" class="works-cited-list"></div>
  </div>
</div>

<!-- Source Notes Panel -->
<div id="notes-panel" class="notes-panel">
  <div class="notes-header">
    <h3>📝 Source Notes</h3>
    <button id="notes-close" class="notes-close-btn">Close</button>
  </div>
  
  <div class="notes-intro">
    Add quick notes to your saved citations. Notes are linked to specific sources from your Works Cited list.
  </div>

  <div class="notes-section">
    <h4>Add Note</h4>
    <select id="note-source-select" class="source-select">
      <option value="">Select a source...</option>
    </select>
    <select id="note-category-select" class="note-category-select">
      <option value="">Category (optional)</option>
      <option value="supports">Supports</option>
      <option value="contradicts">Contradicts</option>
      <option value="background">Background</option>
      <option value="data">Data</option>
    </select>
    <textarea id="note-textarea" class="note-textarea" placeholder="Write your note here..."></textarea>
    <button id="add-note-btn" class="add-note-btn" disabled>Add Note</button>
  </div>

  <div class="notes-section">
    <h4>Your Notes</h4>
    <div id="notes-list" class="notes-list">
      <div class="empty-state">No notes yet. Add a source to your Works Cited and create a note for it.</div>
    </div>
  </div>
</div>

<script type="module">
import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

(function(){
  // ===== COLLEGE BOARD REQUIREMENTS DOCUMENTATION =====
  
  /* 
   * STUDENT-DEVELOPED PROCEDURE: processCitationList
   * Purpose: Process and filter a list of saved citations based on style and date range
   * Parameters:
   *   - citationList (array): List of citation objects to process
   *   - filterStyle (string): Citation style to filter by (e.g., "apa", "mla", "chicago", or "all")
   *   - maxItems (number): Maximum number of items to return
   * Return type: Object containing filtered citations and statistics
   * 
   * This procedure demonstrates:
   * - LISTS/COLLECTION: Works with array of citation objects
   * - ITERATION: Loops through citation list
   * - SEQUENCING: Steps execute in specific order
   * - SELECTION: Conditional logic for filtering
   * - ALGORITHM: Complete process for filtering and counting
   * - ABSTRACTION: Encapsulates complex filtering logic
   */
  
  function processCitationList(citationList, filterStyle, maxItems) {
    // SEQUENCING: Initialize variables in order
    let filtered = [];
    let styleCount = { apa: 0, mla: 0, chicago: 0 };
    
    // ITERATION: Loop through each citation in the list
    for (let i = 0; i < citationList.length; i++) {
      let citation = citationList[i];
      
      // SELECTION: Conditional logic to filter by style
      if (filterStyle === 'all' || citation.style === filterStyle) {
        filtered.push(citation);
      }
      
      // Count citations by style
      if (citation.style && styleCount.hasOwnProperty(citation.style)) {
        styleCount[citation.style]++;
      }
      
      // SELECTION: Stop if we've reached max items
      if (filtered.length >= maxItems) {
        break;
      }
    }
    
    // Return processed data
    return {
      citations: filtered,
      totalCount: citationList.length,
      styleCounts: styleCount
    };
  }
  
  // ===== END REQUIREMENTS DOCUMENTATION =====
  
  // DOM Elements - INPUT from user interface
  const styleEl = document.getElementById('cite-style');
  const authorEl = document.getElementById('cite-author');
  const dateEl = document.getElementById('cite-date');
  const titleEl = document.getElementById('cite-title');
  const sourceEl = document.getElementById('cite-source');
  const urlEl = document.getElementById('cite-url');
  const outEl = document.getElementById('cite-output');
  const fetchBtn = document.getElementById('cite-fetch-metadata');
  const generateBtn = document.getElementById('cite-generate');
  const copyBtn = document.getElementById('cite-copy');
  const saveBtn = document.getElementById('cite-save');
  const loadBtn = document.getElementById('cite-load');
  const worksCitedSection = document.getElementById('works-cited-section');
  const worksCitedList = document.getElementById('works-cited-list');
  const notesToggleBtn = document.getElementById('cite-notes-toggle');
  const notesPanel = document.getElementById('notes-panel');
  const notesCloseBtn = document.getElementById('notes-close');
  const noteSourceSelect = document.getElementById('note-source-select');
  const noteCategorySelect = document.getElementById('note-category-select');
  const noteTextarea = document.getElementById('note-textarea');
  const addNoteBtn = document.getElementById('add-note-btn');
  const notesList = document.getElementById('notes-list');

  // Storage keys
  const CITATIONS_KEY = 'biasGame_citations_v1';
  const NOTES_KEY = 'biasGame_notes_v1';
  const SESSION_KEY = 'citation_session_v1';

  // Backend configuration
  if (!window.fetchProxyBase) {
      window.fetchProxyBase = 'http://localhost:8404/api/media';
      console.info('fetchProxyBase defaulted to', window.fetchProxyBase);
  }

  // Helper functions
  function safe(val, fallback='') { return (val || '').trim(); }

  function extractSourceName(citationText) {
    // Try to extract a readable source name from the citation
    const match = citationText.match(/<i>(.*?)<\/i>/);
    if (match) return match[1];
    
    // Fallback: take first 60 chars
    const plainText = citationText.replace(/<[^>]*>/g, '');
    return plainText.substring(0, 60) + (plainText.length > 60 ? '...' : '');
  }

  // ===== CROSS-CHECK FORMATTING =====
function validateCitationFields() {
  const style = styleEl.value;
  const warnings = [];

  // Basic checks for missing required fields
  if (!authorEl.value.trim()) warnings.push('Author is missing');
  if (!titleEl.value.trim()) warnings.push('Title is missing');
  if (!sourceEl.value.trim()) warnings.push('Source is missing');
  if (!dateEl.value.trim()) warnings.push('Date is missing');

  // Style-specific checks
  if (style === 'apa' && dateEl.value && !/\d{4}/.test(dateEl.value)) {
    warnings.push('APA date should include a year (YYYY)');
  }
  if (style === 'mla' && dateEl.value && !/\d{4}/.test(dateEl.value)) {
    warnings.push('MLA date should include a year (YYYY)');
  }
  if (style === 'chicago' && dateEl.value && !/\d{4}/.test(dateEl.value)) {
    warnings.push('Chicago date should include a year (YYYY)');
  }

  // Display warnings
  const warningEl = document.getElementById('cite-warning');
  if (warnings.length) {
    warningEl.innerHTML = `⚠️ Formatting issues:<br><b>${warnings.join('<br>')}</b>`;
    warningEl.style.display = 'block';
  } else {
    warningEl.style.display = 'none';
  }
}

// Run validation whenever an input or style changes
[authorEl, titleEl, sourceEl, dateEl, urlEl, styleEl].forEach(el => {
  el.addEventListener('input', validateCitationFields);
});
styleEl.addEventListener('change', validateCitationFields);

// Save session whenever inputs change
[authorEl, titleEl, sourceEl, dateEl, urlEl, styleEl].forEach(el => {
  el.addEventListener('input', () => {
    localStorage.setItem(SESSION_KEY, JSON.stringify({
      author: authorEl.value,
      title: titleEl.value,
      source: sourceEl.value,
      date: dateEl.value,
      url: urlEl.value,
      style: styleEl.value
    }));
  });
});

  // LIST: Storage key for citation collection
  const KEY = 'biasGame_citations_v1';

  // FIXED APA FORMAT
  function fmtAPA({ author, date, title, source, url }) {
    // APA Format: Author. (Date). Title. Source. URL
    // If no author, start with Title. (Date). then rest
    let parts = [];

    if (author) {
      parts.push(author + '.');
      if (date) {
        parts.push(`(${date}).`);
      }
      if (title) {
        parts.push(title + '.');
      }
    } else {
      // No author: Title. (Date). Source. URL
      if (title) {
        parts.push(title + '.');
      }
      if (date) {
        parts.push(`(${date}).`);
      }
    }
    
    if (source) {
      parts.push(`<i>${source}</i>.`);
    }
    
    if (url) {
      parts.push(url);
    }

    return parts.join(' ').trim();
  }

  // CORRECT MLA 9TH EDITION FORMAT
function fmtMLA9({ author, date, title, source, url }) {
  // MLA format:
  // Author. "Title." Source, Day Mon. Year, URL.

  let parts = [];

  // Author
  if (author) {
    parts.push(author.trim() + '.');
  }

  // Title (required if no author)
  if (title) {
    parts.push(`"${title.trim()}."`);
  }

  // Source (italicized)
  if (source) {
    parts.push(`<i>${source.trim()}</i>,`);
  }

  // Date → MLA format (Day Mon. Year)
  if (date) {
    let mlaDate = date;

    const parsed = Date.parse(date);
    if (!isNaN(parsed)) {
      const d = new Date(parsed);
      const day = d.getUTCDate();
      const year = d.getUTCFullYear();
      const months = [
        'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June',
        'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.'
      ];
      const month = months[d.getUTCMonth()];
      mlaDate = `${day} ${month} ${year}`;
    }

    parts.push(mlaDate + ',');
  }

  // URL (no https:// removal in MLA 9 unless teacher says so)
  if (url) {
    parts.push(url.trim() + '.');
  }

  return parts.join(' ').replace(/\s+/g, ' ').trim();
}

  // CORRECT CHICAGO (AUTHOR–DATE) FORMAT
function fmtChicago({ author, date, title, source, url }) {
  // Chicago author-date:
  // Author. (Date). "Title." Source. URL.
  // No author → "Title." (Date). Source. URL.

  let parts = [];

  // Author (if present)
  if (author) {
    parts.push(author.trim() + '.');
  }

  // Title (always quoted)
  if (title) {
    parts.push(`"${title.trim()}."`);
  }

  // Date in parentheses (after title if no author)
  if (date) {
    parts.push(`(${date.trim()}).`);
  }

  // Source (italicized)
  if (source) {
    parts.push(`<i>${source.trim()}</i>.`);
  }

  // URL (no trailing period in Chicago author-date)
  if (url) {
    parts.push(url.trim());
  }

  return parts.join(' ').replace(/\s+/g, ' ').trim();
}

function buildParenthetical({ author, title, date, style = 'apa' }) {
  // Extract year if possible
  let year = '';
  if (date) {
    const match = date.match(/\d{4}/);
    if (match) year = match[0];
  }

  // Short title for no-author cases
  const shortTitle = title
    ? title.split(' ').slice(0, 3).join(' ')
    : '';

  // ---- MLA parenthetical
  if (style === 'mla') {
    if (author) {
      // MLA: only author last name
      const last = author.split(',')[0].trim();
      return `(${last})`;
    }
    if (shortTitle) {
      // MLA: shortened title in quotes (no year)
      return `("${shortTitle}…")`;
    }
    return '';
  }

  // ---- APA parenthetical
  if (style === 'apa') {
    if (author) {
      const last = author.split(',')[0].trim();
      // APA: (Author, Year)
      return year ? `(${last}, ${year})` : `(${last})`;
    }
    if (shortTitle) {
      // APA: (Short Title, Year) if no author
      return year
        ? `(${shortTitle}, ${year})`
        : `(${shortTitle})`;
    }
    return '';
  }

  // ---- Chicago (author-date) parenthetical
  if (style === 'chicago') {
    if (author) {
      const last = author.split(',')[0].trim();
      // Chicago: (Author Year) — **no comma**
      return year ? `(${last} ${year})` : `(${last})`;
    }
    if (shortTitle) {
      // Chicago: (Short Title Year) — no comma
      return year
        ? `(${shortTitle} ${year})`
        : `(${shortTitle})`;
    }
    return '';
  }

  // Default fallback
  return '';
}

  // OUTPUT: Generate and display citation
  function generate() {
  const payload = {
    author: safe(authorEl.value),
    date: safe(dateEl.value),
    title: safe(titleEl.value),
    source: safe(sourceEl.value),
    url: safe(urlEl.value)
  };

  const missing = [];
  const fields = [
    { el: authorEl, key: 'author', label: 'Author' },
    { el: titleEl, key: 'title', label: 'Title' },
    { el: sourceEl, key: 'source', label: 'Source / Website' },
    { el: dateEl, key: 'date', label: 'Publication Date' }
  ];

  // Reset previous highlights
  fields.forEach(f => f.el.classList.remove('missing'));

  // Detect missing fields
  fields.forEach(f => {
    if (!payload[f.key]) {
      missing.push(f.label);
      f.el.classList.add('missing');
    }
  });

const style = styleEl.value; // 'apa', 'mla', or 'chicago'

let citation = '';
if (style === 'mla') citation = fmtMLA9(payload);
else if (style === 'chicago') citation = fmtChicago(payload);
else citation = fmtAPA(payload);

outEl.innerHTML = citation;

// Pass style to buildParenthetical!
const parentheticalEl = document.getElementById('cite-parenthetical');
const parenthetical = buildParenthetical({ ...payload, style });

if (parentheticalEl) {
  parentheticalEl.innerHTML = parenthetical
    ? `<b>Parenthetical citation:</b> ${parenthetical}`
    : '';
}

  // Warning message
  const warningEl = document.getElementById('cite-warning');
  if (missing.length > 0) {
    warningEl.innerHTML =
      `⚠️ Missing citation info: <b>${missing.join(', ')}</b><br>
       Please manually enter these fields for a complete citation.`;
    warningEl.style.display = 'block';
  } else {
    warningEl.style.display = 'none';
  }

  return citation;
}

  // OUTPUT: Copy to clipboard (tactile/visual feedback)
  function copyToClipboard(text) {
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = text;
    const plainText = tempDiv.textContent || tempDiv.innerText || '';

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(plainText).then(() => {
        alert('✓ Citation copied to clipboard!');
      }).catch(() => { 
        fallbackCopy(plainText);
      });
    } else {
      fallbackCopy(plainText);
    }
  }

  function fallbackCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { 
      document.execCommand('copy');
      alert('✓ Citation copied to clipboard!');
    } catch (e) {
      alert('Copy failed. Please manually copy the citation.');
    }
    ta.remove();
  }

  // LIST: Save citation to collection
  function saveToWorksCited() {
    const citation = generate();
    if (!citation || citation.length < 5) {
      alert('Please generate a citation first.');
      return;
    }
    
    // Get existing list from storage
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    const newCitation = { 
      citation, 
      style: styleEl.value,
      at: Date.now(),
      source: safe(sourceEl.value),
      title: safe(titleEl.value),
      url: safe(urlEl.value)
    };
    saved.push(newCitation);
    localStorage.setItem(KEY, JSON.stringify(saved));
    alert('✓ Citation saved to Works Cited!');
    
    loadWorksCited();
    updateNotesSourceSelect();
  }

  // PROCEDURE CALL: Use student-developed procedure to process citations
  // OUTPUT: Display filtered and processed citations
  function loadWorksCited() {
    // Get list from storage
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    
    if (saved.length === 0) {
      worksCitedSection.style.display = 'none';
      return;
    }

    // PROCEDURE CALL: Process citation list
    const result = processCitationList(saved, 'all', 100);
    
    // Display results
    worksCitedSection.style.display = 'block';
    worksCitedList.innerHTML = '';

    // ITERATION: Display each citation
    result.citations.forEach((item, index) => {
      const citationDiv = document.createElement('div');
      citationDiv.className = 'citation-item';
      
      const textDiv = document.createElement('div');
      textDiv.className = 'citation-text';
      textDiv.innerHTML = item.citation;
      
      const actionsDiv = document.createElement('div');
      actionsDiv.className = 'citation-actions';
      
      const noteBtn = document.createElement('button');
      noteBtn.className = 'citation-note-btn';
      noteBtn.innerHTML = '📝';
      noteBtn.title = 'Add note to this source';
      noteBtn.onclick = () => openNotesForSource(index);
      
      const deleteBtn = document.createElement('button');
      deleteBtn.className = 'citation-delete';
      deleteBtn.innerHTML = '×';
      deleteBtn.title = 'Delete this citation';
      deleteBtn.onclick = () => deleteCitation(index);
      
      actionsDiv.appendChild(noteBtn);
      actionsDiv.appendChild(deleteBtn);
      citationDiv.appendChild(textDiv);
      citationDiv.appendChild(actionsDiv);
      worksCitedList.appendChild(citationDiv);
    });

    worksCitedSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function deleteCitation(index) {
    if (!confirm('Delete this citation from Works Cited?')) return;
    
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    saved.splice(index, 1);
    localStorage.setItem(KEY, JSON.stringify(saved));
    loadWorksCited();
    updateNotesSourceSelect();
  }

  // Notes functionality
  function updateNotesSourceSelect() {
    const saved = JSON.parse(localStorage.getItem(CITATIONS_KEY) || '[]');
    noteSourceSelect.innerHTML = '<option value="">Select a source...</option>';
    
    saved.forEach((item, index) => {
      const option = document.createElement('option');
      option.value = index;
      option.textContent = extractSourceName(item.citation);
      noteSourceSelect.appendChild(option);
    });

    // Enable/disable add button
    addNoteBtn.disabled = saved.length === 0;
  }

  function loadNotes() {
    const notes = JSON.parse(localStorage.getItem(NOTES_KEY) || '[]');
    const saved = JSON.parse(localStorage.getItem(CITATIONS_KEY) || '[]');
    
    if (notes.length === 0) {
      notesList.innerHTML = '<div class="empty-state">No notes yet. Add a source to your Works Cited and create a note for it.</div>';
      return;
    }

    notesList.innerHTML = '';
    notes.reverse().forEach((note, reverseIndex) => {
      const actualIndex = notes.length - 1 - reverseIndex;
      const citation = saved[note.sourceIndex];
      if (!citation) return; // Skip if citation was deleted

      const noteDiv = document.createElement('div');
      noteDiv.className = 'note-item';
      
      let categoryHTML = '';
      if (note.category) {
        categoryHTML = `<span class="note-category ${note.category}">${note.category}</span>`;
      }
      
      noteDiv.innerHTML = `
        ${categoryHTML}
        <div class="note-content">${note.content}</div>
        <div class="note-meta">
          <strong>${extractSourceName(citation.citation)}</strong> • ${new Date(note.timestamp).toLocaleString()}
        </div>
        <button class="note-delete-btn" onclick="deleteNote(${actualIndex})">×</button>
      `;
      
      notesList.appendChild(noteDiv);
    });
  }

  window.deleteNote = function(index) {
    if (!confirm('Delete this note?')) return;
    
    const notes = JSON.parse(localStorage.getItem(NOTES_KEY) || '[]');
    notes.splice(index, 1);
    localStorage.setItem(NOTES_KEY, JSON.stringify(notes));
    loadNotes();
  };

  function openNotesForSource(sourceIndex) {
    notesPanel.classList.add('open');
    noteSourceSelect.value = sourceIndex;
    noteTextarea.focus();
  }

  // Enable add note button when source and text are filled
  noteSourceSelect.addEventListener('change', () => {
    addNoteBtn.disabled = !noteSourceSelect.value || !noteTextarea.value.trim();
  });

  noteTextarea.addEventListener('input', () => {
    addNoteBtn.disabled = !noteSourceSelect.value || !noteTextarea.value.trim();
  });

  addNoteBtn.addEventListener('click', () => {
    const sourceIndex = parseInt(noteSourceSelect.value);
    const content = noteTextarea.value.trim();
    const category = noteCategorySelect.value;
    
    if (!content || isNaN(sourceIndex)) {
      alert('Please select a source and write a note.');
      return;
    }

    const notes = JSON.parse(localStorage.getItem(NOTES_KEY) || '[]');
    notes.push({
      sourceIndex: sourceIndex,
      content: content,
      category: category,
      timestamp: Date.now()
    });
    localStorage.setItem(NOTES_KEY, JSON.stringify(notes));
    
    noteTextarea.value = '';
    noteCategorySelect.value = '';
    noteSourceSelect.value = '';
    addNoteBtn.disabled = true;
    
    loadNotes();
    alert('✓ Note added successfully!');
  });

  // Notes panel toggle
  notesToggleBtn.addEventListener('click', () => {
    notesPanel.classList.toggle('open');
    if (notesPanel.classList.contains('open')) {
      updateNotesSourceSelect();
      loadNotes();
    }
  });

  notesCloseBtn.addEventListener('click', () => {
    notesPanel.classList.remove('open');
  });

  // Close panel when clicking outside
  document.addEventListener('click', (e) => {
    if (notesPanel.classList.contains('open') && 
        !notesPanel.contains(e.target) && 
        e.target !== notesToggleBtn &&
        !notesToggleBtn.contains(e.target) &&
        !e.target.classList.contains('citation-note-btn')) {
      notesPanel.classList.remove('open');
    }
  });

  // INPUT: Fetch data from online source (URL)
  async function tryFetchHtml(url) {
    try {
      const r = await fetch(url, { method: 'GET', mode: 'cors' });
      if (r.ok) return await r.text();
    } catch (err) {
      console.warn('Direct fetch failed (CORS?), will try proxy', err);
    }
    try {
      const proxy = 'https://api.allorigins.win/raw?url=' + encodeURIComponent(url);
      const r2 = await fetch(proxy);
      if (r2.ok) return await r2.text();
    } catch (err) {
      console.warn('Proxy fetch failed', err);
    }
    return null;
    }

  function parseMetadataFromHtml(html, url) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const getMeta = (name, prop) => {
      const byName = doc.querySelector(`meta[name="${name}"]`);
      if (byName && byName.content) return byName.content;
      const byProp = doc.querySelector(`meta[property="${prop}"]`);
      if (byProp && byProp.content) return byProp.content;
      const byLink = doc.querySelector(`link[rel="canonical"]`);
      if (name === 'url' && byLink && byLink.href) return byLink.href;
      return null;
    };

    const title = getMeta('title','og:title') || doc.querySelector('title')?.textContent || getMeta('twitter:title','twitter:title');
    const site = getMeta('site_name','og:site_name') || (new URL(url)).hostname.replace(/^www\./,'');
    const author = getMeta('author','article:author') || getMeta('author','og:author') || getMeta('byline','byline');
    const published = getMeta('date','article:published_time') || getMeta('publication_date','publication_date') || getMeta('date','og:updated_time') || getMeta('pubdate','pubdate');

    return { title, site, author, published, url };
  }

  function formatPublishedDate(raw) {
    if (!raw) return null;
    const ms = Date.parse(raw);
    if (isNaN(ms)) {
      return { apa: raw, mla: raw, chicago: raw };
    }
    const d = new Date(ms);
    const year = d.getUTCFullYear();
    const monthIdx = d.getUTCMonth();
    const day = d.getUTCDate();
    const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const monthName = months[monthIdx];
    return {
      apa: `${year}, ${monthName} ${day}`,
      mla: `${day} ${monthName} ${year}`,
      chicago: `${year}`
    };
  }

  async function fetchMetadataFromServer(targetUrl) {
    const base = (pythonURI || '').replace(/\/$/, '');
    if (!base) {
      console.warn('No pythonURI set; skipping server fetch');
      return null;
    }

    try {
      const endpoint = `${base}/api/media/fetch_meta?url=${encodeURIComponent(targetUrl)}`;
      console.info('Calling server metadata endpoint:', endpoint);
      
      // Use fetchOptions from config.js
      const requestOptions = {
        ...fetchOptions,
        method: 'GET'  // Override to GET for this specific endpoint
      };
      
      const res = await fetch(endpoint, requestOptions);

      const ct = res.headers.get('content-type') || '';
      const body = ct.includes('application/json') ? await res.json().catch(()=>null) : await res.text().catch(()=>null);

      if (!res.ok) {
        console.warn('Server fetch_meta returned non-OK', res.status, body);
        return null;
      }

      console.info('Server metadata response', body);
      return body;
    } catch (err) {
      console.warn('Server metadata fetch failed (network)', err);
      return null;
    }
  }

  // INPUT: Process URL and fetch metadata
  async function fetchAndFill() {
    const url = (urlEl.value || '').trim();
    if (!url) { alert('Enter a URL first.'); return; }
    fetchBtn.textContent = 'Fetching…';
    fetchBtn.disabled = true;
    try {
      let meta = await fetchMetadataFromServer(url);

      if (!meta) {
        const html = await tryFetchHtml(url);
        if (!html) {
          alert('Failed to fetch page. CORS or proxy error. Consider enabling your Flask proxy.');
          return;
        }
        meta = parseMetadataFromHtml(html, url);
      }

      // Fill form inputs with fetched data
      if (meta.author) authorEl.value = meta.author;
      if (meta.published) {
        const fmt = formatPublishedDate(meta.published);
        const style = (styleEl && styleEl.value) ? styleEl.value : 'apa';
        dateEl.value = (fmt && fmt[style]) ? fmt[style] : meta.published;
      }
      if (meta.title) titleEl.value = meta.title;
      if (meta.site) sourceEl.value = meta.site;
      urlEl.value = meta.url || url;
      generate();
    } catch (err) {
      console.warn(err);
      alert('Error fetching metadata.');
    } finally {
      fetchBtn.textContent = 'Generate from URL';
      fetchBtn.disabled = false;
    }
  }

  // INPUT: Event listeners for user actions
  fetchBtn.addEventListener('click', fetchAndFill);
  generateBtn.addEventListener('click', generate);
  const resetBtn = document.getElementById('cite-reset');

resetBtn.addEventListener('click', () => {
  // Clear all input fields
  [authorEl, dateEl, titleEl, sourceEl, urlEl].forEach(el => el.value = '');
  
  // Clear outputs
  outEl.innerHTML = '';
  document.getElementById('cite-parenthetical').innerHTML = '';
  document.getElementById('cite-warning').style.display = 'none';
  
  // Remove missing highlights
  [authorEl, dateEl, titleEl, sourceEl].forEach(el => el.classList.remove('missing'));
});
  copyBtn.addEventListener('click', () => {
    const citation = outEl.innerHTML;
    if (!citation || citation === 'Your citation will appear here...') {
      alert('Generate a citation first.');
      return;
    }
    copyToClipboard(citation);
  });
  saveBtn.addEventListener('click', saveToWorksCited);
  loadBtn.addEventListener('click', () => {
    if (JSON.parse(localStorage.getItem(CITATIONS_KEY) || '[]').length === 0) {
      alert('No saved citations yet. Click "Save" to add citations to your Works Cited list.');
      return;
    }
    loadWorksCited();
  });

  // Initialize
  updateNotesSourceSelect();
  loadWorksCited();
})();
</script>