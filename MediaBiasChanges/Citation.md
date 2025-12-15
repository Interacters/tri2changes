<style>
  /* Import modern, readable font matching thesis generator */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

  .cite-card { 
    background: linear-gradient(160deg,  #555dc2d2, #564ea0ff); 
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
    color:#ffffff;
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
  }
  
  .cite-btn.primary { 
    background:#7ad2f9; 
    color:#082033; 
  }
  
  .cite-btn.ghost { 
    background:rgba(255,255,255,0.15); 
    color:#ffffff; 
    border:1px solid rgba(255,255,255,0.2); 
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
    padding-right: 40px;
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
  
  .citation-delete {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(248, 113, 113, 0.8);
    color: white;
    border: none;
    border-radius: 50%;
    width: 24px;
    height: 24px;
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
    transform: translateY(-50%) scale(1.1);
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
</style>

<div class="intro-text">
   <h2>Citation Generator</h2>
    <p>It's important to include correct citations for your work. There are many types of formats for citations including: MLA, APA, Chicago. This tool can help you create citations for your sources.</p>
</div>

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
    <input id="cite-title" class="cite-input" placeholder="Article title (no italics markup)" />
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
    <button id="cite-copy" class="cite-btn ghost">
      Copy <span class="btn-hint">(to clipboard)</span>
    </button>
    <button id="cite-save" class="cite-btn ghost" title="Save locally">
      Save <span class="btn-hint">(add to Works Cited)</span>
    </button>
    <button id="cite-load" class="cite-btn ghost" title="Load last">
      Load <span class="btn-hint">(view Works Cited)</span>
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

<script>
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

  // Backend configuration
  if (!window.fetchProxyBase) {
      window.fetchProxyBase = 'http://localhost:8001/api/media';
      console.info('fetchProxyBase defaulted to', window.fetchProxyBase);
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


  // ===== AUTO-SAVE LAST SESSION =====
const SESSION_KEY = 'biasGame_lastSession';

// Load last session on page load
const lastSession = JSON.parse(localStorage.getItem(SESSION_KEY) || '{}');
if (lastSession) {
  if (lastSession.author) authorEl.value = lastSession.author;
  if (lastSession.title) titleEl.value = lastSession.title;
  if (lastSession.source) sourceEl.value = lastSession.source;
  if (lastSession.date) dateEl.value = lastSession.date;
  if (lastSession.url) urlEl.value = lastSession.url;
  if (lastSession.style) styleEl.value = lastSession.style;
  generate();
}

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

  function safe(val, fallback='') { return (val || '').trim(); }

  function fmtAPA({author, date, title, source, url}) {
    let parts = [];
    if (author) parts.push(author);
    if (date) parts.push(`(${date})`);
    if (title) parts.push(title ? `<i>${title}</i>` : null);
    if (source) parts.push(`${source}.`);
    if (url) parts.push(url);
    return parts.filter(Boolean).join(' ').trim();
  }

  function fmtMLA9({author, date, title, source, url}) {
    let parts = [];
    if (author) parts.push(`${author}.`);
    if (title) parts.push(title ? `"${title}."` : null);
    if (source) parts.push(source + ',');
    if (date) parts.push(date + ',');
    if (url) parts.push(url);
    return parts.filter(Boolean).join(' ').replace(/\s+/g,' ').trim();
  }

  function fmtChicago({author, date, title, source, url}) {
    let parts = [];
    if (author) parts.push(author);
    if (date) parts.push(date);
    if (title) parts.push(title ? `"${title}."` : null);
    if (source) parts.push(source ? source + '.' : null);
    if (url) parts.push(url);
    return parts.filter(Boolean).join(' ').replace(/\s+/g,' ').trim();
  }
function buildParenthetical({ author, title, date }) {
  let year = '';

  if (date) {
    const match = date.match(/\d{4}/);
    if (match) year = match[0];
  }

  // Extract last name if possible
  if (author) {
    const last = author.split(',')[0].trim();
    return year ? `(${last}, ${year})` : `(${last})`;
  }

  // Fallback to shortened title
  if (title) {
    const shortTitle = title.split(' ').slice(0, 3).join(' ');
    return year ? `("${shortTitle}…", ${year})` : `("${shortTitle}…")`;
  }

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

  const style = styleEl.value;
  let citation = '';
  if (style === 'mla') citation = fmtMLA9(payload);
  else if (style === 'chicago') citation = fmtChicago(payload);
  else citation = fmtAPA(payload);
  
outEl.innerHTML = citation;

const parentheticalEl = document.getElementById('cite-parenthetical');
const parenthetical = buildParenthetical(payload);

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
    saved.push({ 
      citation, 
      style: styleEl.value,
      at: Date.now() 
    });
    localStorage.setItem(KEY, JSON.stringify(saved));
    alert('✓ Citation saved to Works Cited!');
    
    loadWorksCited();
  }

  // PROCEDURE CALL: Use student-developed procedure to process citations
  // OUTPUT: Display filtered and processed citations
  function loadWorksCited() {
    // Get list from storage
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    
    if (saved.length === 0) {
      worksCitedSection.style.display = 'none';
      alert('No saved citations yet. Click "Save" to add citations to your Works Cited list.');
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
      
      const deleteBtn = document.createElement('button');
      deleteBtn.className = 'citation-delete';
      deleteBtn.innerHTML = '×';
      deleteBtn.title = 'Delete this citation';
      deleteBtn.onclick = () => deleteCitation(index);
      
      citationDiv.appendChild(textDiv);
      citationDiv.appendChild(deleteBtn);
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
  }

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
    const base = (window.fetchProxyBase || '').replace(/\/$/, '');
    if (!base) {
      console.warn('No fetchProxyBase set; skipping server fetch');
      return null;
    }

    try {
      const endpoint = `${base}/fetch_meta?url=${encodeURIComponent(targetUrl)}`;
      console.info('Calling server metadata endpoint:', endpoint);
      const res = await fetch(endpoint, { method: 'GET' });

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
  copyBtn.addEventListener('click', () => {
    const citation = outEl.innerHTML;
    if (!citation || citation === 'Your citation will appear here...') {
      alert('Generate a citation first.');
      return;
    }
    copyToClipboard(citation);
  });
  saveBtn.addEventListener('click', saveToWorksCited);
  loadBtn.addEventListener('click', loadWorksCited);

  styleEl.addEventListener('change', () => {
    if (authorEl.value || titleEl.value || sourceEl.value) {
      generate();
    }
  });
})();
</script>
